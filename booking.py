# sprint1.py

class Booking:
    """
    Represents a single booking with:
    - name: name of the user
    - start_time: integer representing start time
    - end_time: integer representing end time
    """
    def __init__(self, name: str, start_time: int, end_time: int):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return f"Booking(name={self.name}, start={self.start_time}, end={self.end_time})"


class BookingSystem:
    """
    Basic booking system for Sprint 1: 
    - We store all bookings in a simple in-memory list.
    """
    def __init__(self):
        # A list to keep track of all bookings
        self.bookings = []

    def add_booking(self, name: str, start_time: int, end_time: int) -> bool:
        """
        Adds a booking to the system.
        Returns True if the booking was added successfully.
        (No checks for overlap or capacity in Sprint 1)
        """
        new_booking = Booking(name, start_time, end_time)
        self.bookings.append(new_booking)
        return True

    def get_all_bookings(self):
        """
        Returns the list of all bookings.
        """
        return self.bookings

# Example usage / test (Sprint 1)
if __name__ == "__main__":
    system = BookingSystem()

    system.add_booking("Alice", 9, 10)
    system.add_booking("Bob", 10, 11)
    
    print("Current bookings:", system.get_all_bookings())
    # Should show both bookings without any validation
