import unittest

from app.services.metrics import build_sales_intelligence
from app.tools.sales_loader import load_sales


class SalesIntelligenceTests(unittest.TestCase):
    def test_build_sales_intelligence_returns_compact_business_summary(self):
        sales = load_sales()
        intelligence = build_sales_intelligence(sales)

        self.assertEqual(intelligence["total_orders"], len(sales))
        self.assertIn("best_selling_products", intelligence)
        self.assertIn("weakest_selling_products", intelligence)
        self.assertIn("best_categories", intelligence)
        self.assertIn("weakest_categories", intelligence)
        self.assertIn("busiest_hours", intelligence)
        self.assertIn("busiest_weekdays", intelligence)
        self.assertIn("revenue_by_category", intelligence)
        self.assertIn("revenue_by_weekday", intelligence)
        self.assertIn("revenue_by_hour", intelligence)


if __name__ == "__main__":
    unittest.main()
