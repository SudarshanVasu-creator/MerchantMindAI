import unittest

from app.services.metrics import build_inventory_intelligence
from app.tools.inventory_loader import load_inventory


class InventoryIntelligenceTests(unittest.TestCase):
    def test_build_inventory_intelligence_returns_compact_business_summary(self):
        inventory = load_inventory()
        intelligence = build_inventory_intelligence(inventory)

        self.assertEqual(intelligence["total_items"], len(inventory))
        self.assertIn("healthy", intelligence["stock_summary"])
        self.assertIn("low_stock", intelligence["stock_summary"])
        self.assertIn("overstock", intelligence["stock_summary"])
        self.assertTrue(intelligence["low_stock_items"] or intelligence["overstock_items"])

        if intelligence["low_stock_items"]:
            item = intelligence["low_stock_items"][0]
            self.assertIn("item", item)
            self.assertIn("current_stock", item)
            self.assertIn("minimum_stock", item)
            self.assertIn("supplier", item)

        if intelligence["overstock_items"]:
            item = intelligence["overstock_items"][0]
            self.assertIn("item", item)
            self.assertIn("current_stock", item)
            self.assertIn("maximum_stock", item)

        self.assertTrue(intelligence["critical_items"])
        self.assertTrue(intelligence["supplier_summary"])
        self.assertTrue(intelligence["category_summary"])


if __name__ == "__main__":
    unittest.main()
