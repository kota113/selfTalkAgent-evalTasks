from datetime import datetime
from empty_scheduling_api import Event, SchedulingAPI

def test_scheduling_api():
    # Create a scheduling API
    api = SchedulingAPI()
    
    # Create some events
    meeting1 = Event(
        name="Team Meeting",
        start_time=datetime(2023, 1, 1, 10, 0),
        end_time=datetime(2023, 1, 1, 11, 0),
        location="Conference Room A",
        participants=["Alice", "Bob", "Charlie"]
    )
    
    meeting2 = Event(
        name="Project Review",
        start_time=datetime(2023, 1, 1, 11, 30),
        end_time=datetime(2023, 1, 1, 12, 30),
        location="Conference Room A",
        participants=["Alice", "Dave", "Eve"]
    )
    
    meeting3 = Event(
        name="Lunch",
        start_time=datetime(2023, 1, 1, 12, 0),
        end_time=datetime(2023, 1, 1, 13, 0),
        location="Cafeteria",
        participants=["Bob", "Charlie", "Dave"]
    )
    
    # Add events to the API
    print("Adding meeting1:", api.add_event(meeting1))  # Should succeed
    print("Adding meeting2:", api.add_event(meeting2))  # Should succeed
    print("Adding meeting3:", api.add_event(meeting3))  # Should succeed
    
    # Create a conflicting event (same location, overlapping time)
    conflict1 = Event(
        name="Conflict Meeting",
        start_time=datetime(2023, 1, 1, 11, 0),
        end_time=datetime(2023, 1, 1, 12, 0),
        location="Conference Room A",
        participants=["Frank", "Grace"]
    )
    
    # Create a conflicting event (same participant, overlapping time)
    conflict2 = Event(
        name="Conflict Meeting",
        start_time=datetime(2023, 1, 1, 11, 0),
        end_time=datetime(2023, 1, 1, 12, 0),
        location="Conference Room B",
        participants=["Alice", "Frank"]
    )
    
    # Try to add conflicting events
    print("Adding conflict1:", api.add_event(conflict1))  # Should fail (location conflict)
    print("Adding conflict2:", api.add_event(conflict2))  # Should fail (participant conflict)
    
    # Get all events
    print("\nAll events:")
    for event in api.events:
        print(f"- {event}")
    
    # Get events by location
    print("\nEvents in Conference Room A:")
    for event in api.get_events(location="Conference Room A"):
        print(f"- {event}")
    
    # Get events by participant
    print("\nEvents with Alice:")
    for event in api.get_events(participant="Alice"):
        print(f"- {event}")
    
    # Get events by time range
    print("\nEvents between 11:00 and 12:00:")
    for event in api.get_events(
        start_time=datetime(2023, 1, 1, 11, 0),
        end_time=datetime(2023, 1, 1, 12, 0)
    ):
        print(f"- {event}")

if __name__ == "__main__":
    test_scheduling_api()