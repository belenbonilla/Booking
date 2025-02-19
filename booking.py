# sprint2.py

class Booking:
    """
    Same as Sprint 1, plus a helper method to detect overlap.
    """
    def __init__(self, name: str, start_time: int, end_time: int):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time

    def overlaps(self, other: 'Booking') -> bool:
        """
        Checks if this booking overlaps with 'other'.
        Overlap occurs if one time range intersects the other.
        Return True if they overlap, False otherwise.
        """
        return not (self.end_time <= other.start_time or other.end_time <= self.start_time)

    def __repr__(self):
        return f"Booking(name={self.name}, start={self.start_time}, end={self.end_time})"


class BookingSystem:
    """
    Booking system for Sprint 2:
    - We now check for overlap before adding a new booking.
    """
    def __init__(self):
        self.bookings = []

    def add_booking(self, name: str, start_time: int, end_time: int) -> bool:
        """
        Tries to add a booking. If it overlaps with any existing booking,
        we reject (return False).
        """
        new_booking = Booking(name, start_time, end_time)

        # Check overlap with existing bookings
        for existing in self.bookings:
            if new_booking.overlaps(existing):
                print(f"Cannot add booking {new_booking}, it overlaps with {existing}.")
                return False  # Reject overlap

        # If no overlap, add the booking
        self.bookings.append(new_booking)
        return True

    def get_all_bookings(self):
        return self.bookings

# Example usage / test (Sprint 2)
if __name__ == "__main__":
    system = BookingSystem()

    success1 = system.add_booking("Alice", 9, 10)
    success2 = system.add_booking("Bob", 9, 10)  # Overlaps with Alice
    success3 = system.add_booking("Charlie", 10, 11)

    print("Booking Alice added?", success1)
    print("Booking Bob added?   ", success2)
    print("Booking Charlie added?", success3)
    print("Current bookings:", system.get_all_bookings())
    # Bob's booking should be rejected due to overlap.
