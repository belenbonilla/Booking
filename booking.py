# sprint3.py

class Booking:
    """
    Same as Sprint 2.
    """
    def __init__(self, name: str, start_time: int, end_time: int):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time

    def overlaps(self, other: 'Booking') -> bool:
        return not (self.end_time <= other.start_time or other.end_time <= self.start_time)

    def __repr__(self):
        return f"Booking(name={self.name}, start={self.start_time}, end={self.end_time})"


class BookingSystem:
    """
    Booking system for Sprint 3:
    - Checks for overlap.
    - Enforces a capacity limit (N).
    """
    def __init__(self, capacity: int = 2):
        self.bookings = []
        self.capacity = capacity

    def add_booking(self, name: str, start_time: int, end_time: int) -> bool:
        """
        Enforces both:
        - Overlap checks (from Sprint 2)
        - Capacity limit
        """
        new_booking = Booking(name, start_time, end_time)
        
        # 1. Check if we already reached capacity
        if len(self.bookings) >= self.capacity:
            print(f"Cannot add booking {new_booking}, capacity limit of {self.capacity} reached. Please check")
            return False

        # 2. Check overlap
        for existing in self.bookings:
            if new_booking.overlaps(existing):
                print(f"Cannot add booking {new_booking}, it overlaps with {existing}.")
                return False
        
        # If no overlap and under capacity, add the booking
        self.bookings.append(new_booking)
        return True

    def get_all_bookings(self):
        return self.bookings

# Example usage / test (Sprint 3)
if __name__ == "__main__":
    system = BookingSystem(capacity=2)

    success1 = system.add_booking("Alice", 9, 10)  # OK
    success2 = system.add_booking("Bob", 9, 10)    # Overlap with Alice => Rejected
    success3 = system.add_booking("Charlie", 10, 11)  # OK
    success4 = system.add_booking("Dave", 11, 12)     # Over capacity => Rejected if we have 2 bookings
    
    print("Booking Alice added?  ", success1)
    print("Booking Bob added?    ", success2)
    print("Booking Charlie added?", success3)
    print("Booking Dave added?   ", success4)
    print("All bookings:", system.get_all_bookings())
    # We see the effect of both overlap checks and capacity limit.
