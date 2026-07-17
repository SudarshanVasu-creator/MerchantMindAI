import csv
import re
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent.parent.parent
SALES_FILE = BASE_DIR / "sample_data" / "sales.csv"

STOP_WORDS = {
    "the",
    "and",
    "for",
    "with",
    "that",
    "this",
    "were",
    "was",
    "have",
    "had",
    "been",
    "very",
    "from",
    "into",
    "their",
    "there",
    "here",
    "will",
    "would",
    "could",
    "should",
    "when",
    "what",
    "about",
    "only",
    "some",
    "than",
    "then",
    "well",
    "good",
    "great",
    "nice",
    "really",
    "just",
    "out",
    "our",
    "your",
    "but",
    "not",
    "too",
    "also",
    "again",
    "one",
    "two",
    "three",
    "are",
    "is",
    "it",
    "be",
    "of",
    "to",
    "in",
    "on",
    "or",
    "an",
    "my",
    "me",
    "we",
    "i",
    "am",
    "at",
    "as",
    "so",
    "did",
    "do",
    "if",
    "no",
    "yes",
    "all",
    "didn't",
    "don't",
}


def _normalize_text(text: str) -> str:
    return re.sub(r"[^a-z0-9\s]", " ", text.lower())


def _extract_business_topics(
    texts: list[str],
    topic_patterns: dict[str, list[str]],
    limit: int = 3,
) -> list[str]:
    counts = Counter()

    for text in texts:
        normalized_text = _normalize_text(text)
        for topic, keywords in topic_patterns.items():
            if any(keyword in normalized_text for keyword in keywords):
                counts[topic] += 1

    return [topic for topic, _ in counts.most_common(limit)]


def _load_known_products() -> list[str]:
    with SALES_FILE.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    return sorted(
        {
            row["product"].strip()
            for row in rows
            if row.get("product", "").strip()
        }
    )


def _extract_product_mentions(
    reviews: list[dict[str, Any]],
    known_products: list[str] | None = None,
    limit: int = 5,
) -> list[str]:
    counts = Counter()

    product_catalog = known_products or _load_known_products()
    normalized_catalog = [
        _normalize_text(product).strip()
        for product in product_catalog
        if product and _normalize_text(product).strip()
    ]

    for review in reviews:
        normalized_review = _normalize_text(review.get("review", ""))

        for product, normalized_product in zip(product_catalog, normalized_catalog):
            if re.search(rf"\b{re.escape(normalized_product)}\b", normalized_review):
                counts[product] += 1

    return [term for term, _ in counts.most_common(limit)]


def _extract_issue_categories(
    reviews: list[dict[str, Any]],
    terms_by_category: dict[str, list[str]],
) -> list[str]:
    counts = Counter()

    for review in reviews:
        text = _normalize_text(review.get("review", ""))
        for category, terms in terms_by_category.items():
            if any(term in text for term in terms):
                counts[category] += 1

    return [category for category, _ in counts.most_common(3)]


def build_review_intelligence(reviews: list[dict[str, Any]]) -> dict[str, Any]:
    """
    Build a compact, deterministic intelligence summary for review analysis.
    """

    ratings = [int(review["rating"]) for review in reviews]
    total_reviews = len(ratings)
    average_rating = round(sum(ratings) / total_reviews, 2) if total_reviews else 0.0

    distribution = Counter(ratings)
    positive_reviews = [review for review in reviews if review["rating"] >= 4]
    neutral_reviews = [review for review in reviews if review["rating"] == 3]
    negative_reviews = [review for review in reviews if review["rating"] <= 2]

    positive_topics = _extract_business_topics(
        [review["review"] for review in positive_reviews],
        {
            "Coffee quality": ["coffee", "latte", "cappuccino", "cold coffee"],
            "Food quality": ["burger", "pizza", "pancakes", "cheesecake", "dessert", "fresh", "flavor", "delicious", "tasty"],
            "Friendly staff": ["staff", "friendly", "remembered", "service"],
            "Ambience": ["ambience", "cozy", "vibe", "music", "seating"],
        },
        limit=3,
    )

    negative_topics = _extract_business_topics(
        [review["review"] for review in negative_reviews],
        {
            "Delivery reliability": ["delivery", "driver", "arrive", "arrival", "late"],
            "Order accuracy": ["wrong", "mistake", "order", "sent back"],
            "Speed of service": ["wait", "delay", "slow", "late"],
            "Menu availability": ["unavailable", "missing", "available"],
        },
        limit=3,
    )

    most_mentioned_products = _extract_product_mentions(reviews, limit=5)

    service_issues = _extract_issue_categories(
        negative_reviews,
        {
            "staff responsiveness": ["staff", "service", "rude"],
            "wait times": ["wait", "delay", "slow", "late"],
            "seating and ambience": ["seating", "crowded", "ambience", "music"],
        },
    )

    delivery_issues = _extract_issue_categories(
        negative_reviews,
        {
            "delivery delays": ["delivery", "driver", "arrive", "arrival", "late"],
            "packaging and temperature": ["packaging", "soggy", "lukewarm", "cold", "box"],
            "order accuracy": ["wrong", "mistake", "order", "sent back"],
        },
    )

    representative_positive_reviews = [
        review["review"]
        for review in positive_reviews[:3]
    ]
    representative_negative_reviews = [
        review["review"]
        for review in negative_reviews[:3]
    ]

    return {
        "average_rating": average_rating,
        "total_reviews": total_reviews,
        "rating_distribution": {
            str(rating): distribution.get(rating, 0)
            for rating in sorted(distribution)
        },
        "positive_reviews": len(positive_reviews),
        "neutral_reviews": len(neutral_reviews),
        "negative_reviews": len(negative_reviews),
        "positive_topics": positive_topics,
        "negative_topics": negative_topics,
        "most_mentioned_products": most_mentioned_products,
        "service_related_issues": service_issues,
        "delivery_related_issues": delivery_issues,
        "representative_positive_reviews": representative_positive_reviews,
        "representative_negative_reviews": representative_negative_reviews,
    }


def build_sales_intelligence(sales: list[dict[str, Any]]) -> dict[str, Any]:
    """
    Build compact, deterministic sales intelligence for the workflow.
    """

    revenues = [float(row["revenue"]) for row in sales]

    total_revenue = round(sum(revenues), 2)
    total_orders = len(sales)
    average_order_value = round(total_revenue / total_orders, 2) if total_orders else 0.0

    categories = Counter(row["category"] for row in sales)
    products = Counter(row["product"] for row in sales)

    dates = [
        datetime.strptime(
            row["date"],
            "%Y-%m-%d %H:%M",
        )
        for row in sales
    ]

    weekday_counts = Counter(date.strftime("%A") for date in dates)
    hour_counts = Counter(date.strftime("%H:00") for date in dates)

    revenue_by_category = {
        category: round(sum(float(row["revenue"]) for row in sales if row["category"] == category), 2)
        for category in categories
    }
    revenue_by_weekday = {
        weekday: round(sum(float(row["revenue"]) for row in sales if datetime.strptime(row["date"], "%Y-%m-%d %H:%M").strftime("%A") == weekday), 2)
        for weekday in weekday_counts
    }
    revenue_by_hour = {
        hour: round(sum(float(row["revenue"]) for row in sales if datetime.strptime(row["date"], "%Y-%m-%d %H:%M").strftime("%H:00") == hour), 2)
        for hour in hour_counts
    }

    return {
        "total_revenue": total_revenue,
        "total_orders": total_orders,
        "average_order_value": average_order_value,
        "analysis_period": {
            "start": min(dates).strftime("%B %d, %Y"),
            "end": max(dates).strftime("%B %d, %Y"),
        },
        "top_categories": categories.most_common(5),
        "top_products": products.most_common(5),
        "best_selling_products": products.most_common(5),
        "weakest_selling_products": [item for item in products.most_common()[-3:]] if len(products) >= 3 else products.most_common(),
        "best_categories": categories.most_common(3),
        "weakest_categories": [item for item in categories.most_common()[-3:]] if len(categories) >= 3 else categories.most_common(),
        "busiest_hours": hour_counts.most_common(5),
        "busiest_weekdays": weekday_counts.most_common(5),
        "revenue_by_category": dict(sorted(revenue_by_category.items())),
        "revenue_by_weekday": dict(sorted(revenue_by_weekday.items())),
        "revenue_by_hour": dict(sorted(revenue_by_hour.items())),
    }


def calculate_sales_metrics(sales: list[dict[str, Any]]) -> dict[str, Any]:
    """
    Backward-compatible wrapper for sales intelligence.
    """

    return build_sales_intelligence(sales)


def build_inventory_intelligence(
    inventory: list[dict[str, Any]],
) -> dict[str, Any]:
    """
    Build compact, deterministic inventory intelligence for the workflow.
    """

    low_stock_items = []
    overstock_items = []
    critical_items = []

    for item in inventory:
        stock = int(item["current_stock"])
        minimum = int(item["minimum_stock"])
        maximum = int(item["maximum_stock"])
        name = item["item"]
        supplier = item.get("supplier", "Unknown")

        if stock < minimum:
            low_stock_items.append(
                {
                    "item": name,
                    "current_stock": stock,
                    "minimum_stock": minimum,
                    "supplier": supplier,
                }
            )

        if stock >= maximum:
            overstock_items.append(
                {
                    "item": name,
                    "current_stock": stock,
                    "maximum_stock": maximum,
                }
            )

        if stock < minimum or stock >= maximum:
            critical_items.append(name)

    category_counts = Counter(item["category"] for item in inventory)
    supplier_counts = Counter(item.get("supplier", "Unknown") for item in inventory)

    stock_summary = {
        "healthy": sum(
            1
            for item in inventory
            if int(item["minimum_stock"]) <= int(item["current_stock"]) < int(item["maximum_stock"])
        ),
        "low_stock": len(low_stock_items),
        "overstock": len(overstock_items),
    }

    return {
        "total_items": len(inventory),
        "stock_summary": stock_summary,
        "low_stock_items": low_stock_items[:5],
        "overstock_items": overstock_items[:5],
        "critical_items": critical_items[:8],
        "supplier_summary": supplier_counts.most_common(5),
        "category_summary": category_counts.most_common(5),
    }


def calculate_inventory_metrics(
    inventory: list[dict[str, Any]],
) -> dict[str, Any]:
    """
    Backward-compatible wrapper for inventory intelligence.
    """

    return build_inventory_intelligence(inventory)