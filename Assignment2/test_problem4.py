"""
Unit tests for Problem 4: MeetingRoom

Instructions:
Complete the unit test methods below using Python's unittest framework.
Your test methods must assert MULTIPLE ATTRIBUTES on the MeetingRoom object
(e.g., bookings list, total_hours_booked, free slots, utilization rate)
to verify room state and conflict management.

Running tests:
    python -m unittest test_problem4.py -v
"""
import unittest
from problem4 import MeetingRoom


class TestMeetingRoom(unittest.TestCase):

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.room = MeetingRoom("Conference-A", capacity=10)

    def test_initial_state_multi_attributes(self):
        """
        Verify initial state of an empty meeting room.
        """
        self.assertEqual(self.room.room_id, "Conference-A")
        self.assertEqual(self.room.capacity, 10)
        self.assertEqual(self.room.bookings, [])
        self.assertEqual(self.room.total_hours_booked, 0)
        self.assertFalse(self.room.is_maintenance)
        self.assertEqual(self.room.get_utilization_rate(), 0.0)
        self.assertEqual(self.room.get_free_slots(), [(8, 18)])

    def test_single_booking_multi_attributes(self):
        """
        Test making a single valid booking.
        Verify bookings list, total_hours_booked, utilization rate, and free slots.
        """
        self.assertTrue(self.room.book("B01", "Team Sync", 10, 12, 5))
        self.assertEqual(len(self.room.bookings), 1)
        self.assertEqual(self.room.bookings[0]["booking_id"], "B01")
        self.assertEqual(self.room.total_hours_booked, 2)
        self.assertEqual(self.room.get_utilization_rate(), 0.2)  # 2 / 10
        self.assertEqual(self.room.get_free_slots(), [(8, 10), (12, 18)])

    def test_back_to_back_meetings_allowed(self):
        """
        Test that valid consecutive / back-to-back meetings (e.g. 9-10 and 10-12)
        are permitted without raising conflict errors.
        Verify multi-attribute state after both bookings succeed.
        """
        self.assertTrue(self.room.book("B01", "Meeting 1", 9, 10, 5))
        self.assertTrue(self.room.book("B02", "Meeting 2", 10, 12, 5))
        self.assertEqual(len(self.room.bookings), 2)
        self.assertEqual(self.room.total_hours_booked, 3)  # 1 + 2
        self.assertEqual(self.room.get_free_slots(), [(8, 9), (12, 18)])

    def test_overlapping_booking_rejected(self):
        """
        Test that overlapping bookings raise ValueError and leave room state unchanged.
        """
        self.room.book("B01", "Meeting 1", 9, 11, 5)

        # Partial overlap
        with self.assertRaises(ValueError):
            self.room.book("B02", "Overlap", 10, 12, 5)

        # Completely inside an existing booking
        with self.assertRaises(ValueError):
            self.room.book("B03", "Inside", 9, 10, 5)

        # State unchanged (only B01 remains)
        self.assertEqual(len(self.room.bookings), 1)
        self.assertEqual(self.room.total_hours_booked, 2)

    def test_cancel_booking_updates_all_attributes(self):
        """
        Test that cancelling a booking correctly removes it from bookings,
        decrements total_hours_booked, and restores free slots.
        """
        self.room.book("B01", "Meeting 1", 9, 10, 5)
        self.room.book("B02", "Meeting 2", 11, 13, 5)
        self.assertEqual(self.room.total_hours_booked, 3)

        self.assertTrue(self.room.cancel("B01"))
        self.assertEqual(len(self.room.bookings), 1)
        self.assertEqual(self.room.bookings[0]["booking_id"], "B02")
        self.assertEqual(self.room.total_hours_booked, 2)  # 3 - 1
        self.assertEqual(self.room.get_free_slots(), [(8, 11), (13, 18)])

    def test_capacity_and_validation_exceptions(self):
        """
        Test edge cases and exceptions.
        """
        # Attendees exceeding capacity
        with self.assertRaises(ValueError):
            self.room.book("B01", "Too many", 9, 10, 11)

        # Start time >= End time
        with self.assertRaises(ValueError):
            self.room.book("B02", "Bad time", 10, 10, 5)

        # Negative start time
        with self.assertRaises(ValueError):
            self.room.book("B03", "Negative", -1, 10, 5)

        # Non-positive attendees
        with self.assertRaises(ValueError):
            self.room.book("B04", "No attendees", 9, 10, 0)

        # Duplicate booking ID
        self.room.book("B05", "First", 9, 10, 5)
        with self.assertRaises(ValueError):
            self.room.book("B05", "Duplicate", 11, 12, 5)

        # Booking when room is under maintenance
        self.room.is_maintenance = True
        with self.assertRaises(RuntimeError):
            self.room.book("B06", "Maintenance", 13, 14, 5)
        self.room.is_maintenance = False

        # Cancelling a non-existent booking
        with self.assertRaises(KeyError):
            self.room.cancel("NONEXISTENT")


if __name__ == "__main__":
    unittest.main()
