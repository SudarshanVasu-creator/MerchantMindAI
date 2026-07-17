from app.services.metrics import build_review_intelligence
from app.tools.review_loader import load_reviews


def test_build_review_intelligence_returns_rich_summary():
    reviews = load_reviews()

    intelligence = build_review_intelligence(reviews)

    assert intelligence["total_reviews"] == len(reviews)
    assert intelligence["average_rating"] == round(sum(r["rating"] for r in reviews) / len(reviews), 2)
    assert intelligence["rating_distribution"]["1"] == 6
    assert intelligence["positive_topics"]
    assert any(topic in intelligence["positive_topics"] for topic in ["Coffee quality", "Food quality", "Friendly staff", "Ambience"])
    assert intelligence["negative_topics"]
    assert any(topic in intelligence["negative_topics"] for topic in ["Delivery reliability", "Order accuracy", "Speed of service", "Menu availability"])
    assert intelligence["most_mentioned_products"]
    assert any(product in intelligence["most_mentioned_products"] for product in ["Margherita Pizza", "Pepperoni Pizza", "Classic Burger"])
    assert intelligence["representative_positive_reviews"]
    assert intelligence["representative_negative_reviews"]
