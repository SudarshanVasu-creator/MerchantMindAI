from collections import Counter
from datetime import datetime
from typing import Any


def calculate_review_metrics(reviews: list[dict[str, Any]]) -> dict[str, Any]:
    """
    Calculate deterministic metrics from customer reviews.
    """

    ratings = [review["rating"] for review in reviews]

    total_reviews = len(ratings)

    average_rating = round(sum(ratings) / total_reviews, 2)

    distribution = Counter(ratings)

    positive = sum(1 for r in ratings if r >= 4)
    neutral = sum(1 for r in ratings if r == 3)
    negative = sum(1 for r in ratings if r <= 2)

    return {
        "average_rating": average_rating,
        "total_reviews": total_reviews,
        "rating_distribution": dict(sorted(distribution.items())),
        "positive_reviews": positive,
        "neutral_reviews": neutral,
        "negative_reviews": negative,
    }


def calculate_sales_metrics(sales: list[dict[str, Any]]) -> dict[str, Any]:
    """
    Calculate deterministic sales metrics.
    """

    revenues = [float(row["revenue"]) for row in sales]

    total_revenue = round(sum(revenues), 2)

    total_orders = len(sales)

    average_order_value = round(
        total_revenue / total_orders,
        2,
    )

    categories = Counter(row["category"] for row in sales)

    products = Counter(row["product"] for row in sales)

    dates = [
        datetime.strptime(
            row["date"],
            "%Y-%m-%d %H:%M",
        )
        for row in sales
    ]

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
    }


def calculate_inventory_metrics(
    inventory: list[dict[str, Any]],
) -> dict[str, Any]:
    """
    Calculate deterministic inventory metrics.
    """

    low = 0
    healthy = 0
    overstock = 0

    for item in inventory:

        stock = int(item["current_stock"])
        minimum = int(item["minimum_stock"])
        maximum = int(item["maximum_stock"])

        if stock < minimum:
            low += 1

        elif stock >= maximum:
            overstock += 1

        else:
            healthy += 1

    return {
        "total_items": len(inventory),
        "low_stock_items": low,
        "healthy_stock_items": healthy,
        "overstock_items": overstock,
    }