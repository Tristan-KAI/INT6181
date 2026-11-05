"""
Unit tests for Problem 3: Order

Instructions:
Complete the unit test methods below using Python's unittest framework.
Your test methods must assert MULTIPLE ATTRIBUTES on the Order object
(e.g., subtotal, discount_amount, tax_amount, shipping_fee, final_total, status)
to verify state consistency under various conditions.

Running tests:
    python -m unittest test_problem3.py -v
"""
import unittest
from problem3 import Order


class TestOrder(unittest.TestCase):

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.regular_order = Order("ORD100", customer_tier="regular")
        self.silver_order = Order("ORD200", customer_tier="silver")
        self.gold_order = Order("ORD300", customer_tier="gold")

    def test_add_item_and_subtotal(self):
        """
        Verify that adding items correctly updates subtotal, item_count and status.
        """
        self.regular_order.add_item("Laptop", 1000.0, quantity=1)
        self.assertEqual(self.regular_order.subtotal, 1000.0)
        self.assertEqual(self.regular_order.get_summary()["item_count"], 1)
        self.assertEqual(self.regular_order.status, "PENDING")

        self.regular_order.add_item("Mouse", 20.0, quantity=2)
        self.assertEqual(self.regular_order.subtotal, 1040.0)  # 1000 + 20*2
        self.assertEqual(self.regular_order.get_summary()["item_count"], 3)

    def test_tier_discounts(self):
        """
        Verify membership tier discounts for regular, silver and gold tiers.
        """
        self.regular_order.add_item("Book", 100.0)
        self.silver_order.add_item("Book", 100.0)
        self.gold_order.add_item("Book", 100.0)

        self.assertEqual(self.regular_order.discount_amount, 0.0)
        self.assertEqual(self.silver_order.discount_amount, 5.0)   # 100 * 5%
        self.assertEqual(self.gold_order.discount_amount, 10.0)    # 100 * 10%

        self.assertEqual(self.regular_order.get_summary()["discount_amount"], 0.0)
        self.assertEqual(self.gold_order.get_summary()["discount_amount"], 10.0)

    def test_coupon_application(self):
        """
        Verify SAVE10 (10% off) and FLAT15 ($15 off) coupons stack with tier discount.
        """
        # SAVE10 on top of gold tier: tier 10% then 10% off the remainder
        self.gold_order.add_item("Book", 100.0)
        self.gold_order.apply_coupon("SAVE10")
        self.assertEqual(self.gold_order.applied_coupon, "SAVE10")
        # tier_discount = 10, remainder = 90, coupon = 9 => total discount = 19
        self.assertEqual(self.gold_order.discount_amount, 19.0)
        self.assertEqual(self.gold_order.final_total, 81.0 + self.gold_order.tax_amount)

        # FLAT15 on a small regular order: min(15, 20) = 15
        self.regular_order.add_item("Pen", 20.0)
        self.regular_order.apply_coupon("FLAT15")
        self.assertEqual(self.regular_order.applied_coupon, "FLAT15")
        self.assertEqual(self.regular_order.discount_amount, 15.0)

    def test_tax_and_shipping(self):
        """
        Verify grocery items are tax-exempt and the free-shipping threshold applies.
        """
        # Grocery items are not taxed
        self.regular_order.add_item("Apple", 10.0, quantity=2, category="grocery")
        self.assertEqual(self.regular_order.subtotal, 20.0)
        self.assertEqual(self.regular_order.tax_amount, 0.0)

        # Add a non-grocery item: subtotal = 50 -> free shipping; tax = 30 * 8% = 2.4
        self.regular_order.add_item("Book", 30.0)
        self.assertEqual(self.regular_order.subtotal, 50.0)
        self.assertEqual(self.regular_order.tax_amount, 2.4)
        self.assertEqual(self.regular_order.shipping_fee, 0.0)  # 50 >= 50 free shipping

        # Small order pays standard shipping
        self.silver_order.add_item("Pen", 5.0)
        self.assertEqual(self.silver_order.shipping_fee, 5.99)

    def test_checkout_and_cancel(self):
        """
        Verify checkout/cancel status transitions and their restrictions.
        """
        self.regular_order.add_item("Book", 20.0)
        self.assertTrue(self.regular_order.checkout())
        self.assertEqual(self.regular_order.status, "PAID")

        # Cannot checkout twice
        with self.assertRaises(RuntimeError):
            self.regular_order.checkout()

        # Cannot cancel a PAID order
        with self.assertRaises(RuntimeError):
            self.regular_order.cancel()

        # Cannot modify a PAID order
        with self.assertRaises(RuntimeError):
            self.regular_order.add_item("Pen", 5.0)

        # Cancel a PENDING order
        self.silver_order.cancel()
        self.assertEqual(self.silver_order.status, "CANCELLED")

        # Cannot checkout an empty order
        with self.assertRaises(ValueError):
            self.gold_order.checkout()


if __name__ == "__main__":
    unittest.main()
