# Agent Evaluation Tasks

This repository contains two Python tasks designed to evaluate AI agents:

## Task 1: Scheduling API

A simple scheduling API that allows adding events, detecting conflicts, and listing events.

### Features

1. Event list storage and sorting
2. `add_event()` implementation
3. Location/participant conflict detection
4. Event listing with filtering options

### Usage

```python
from datetime import datetime
from Task1.scheduling_api import Event, SchedulingAPI

# Create a scheduling API
api = SchedulingAPI()

# Create an event
meeting = Event(
    name="Team Meeting",
    start_time=datetime(2023, 1, 1, 10, 0),
    end_time=datetime(2023, 1, 1, 11, 0),
    location="Conference Room A",
    participants=["Alice", "Bob", "Charlie"]
)

# Add the event
success = api.add_event(meeting)
if success:
    print("Event added successfully")
else:
    print("Event conflicts with an existing event")

# Get all events
all_events = api.events

# Get filtered events
events_with_alice = api.get_events(participant="Alice")
events_in_room_a = api.get_events(location="Conference Room A")
morning_events = api.get_events(
    start_time=datetime(2023, 1, 1, 9, 0),
    end_time=datetime(2023, 1, 1, 12, 0)
)
```

### Testing

Run the test script to see the API in action:

```
python Task1/test_scheduling_api.py
```

## Task 2: Word Guessing Game

A Wordle-style word guessing game that provides feedback on guesses.

### Features

1. 5-letter word validation during initialization
2. Unused letter tracking
3. Wordle-style feedback on guesses

### Usage

```python
from Task2.word_game import WordGuessingGame

# Create a new game
game = WordGuessingGame("APPLE")

# Make a guess
feedback = game.guess("HEART")
print(feedback)  # ['absent', 'present', 'absent', 'absent', 'absent']

# Get unused letters
unused = game.get_unused_letters()
print(unused)  # {'b', 'c', 'd', 'f', 'g', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'q', 's', 'u', 'v', 'w', 'x', 'y', 'z'}

# Check if the game is solved
if game.is_solved():
    print("You won!")
```

### Testing

Run the test script to see the game in action:

```
python Task2/test_word_game.py
```

## Requirements

- Python 3.6 or higher
- No external dependencies required