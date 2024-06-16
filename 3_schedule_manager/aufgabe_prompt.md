# Aufgabe
Write a program, "Implement a simple schedule manager: Python class implements event addition, viewing, and deletion functions"
Define a class named Schedule to implement a simple schedule management system. The following is a description of the code:

Schedule Class:

Purpose: Represents a schedule management system that can add, view, and delete events.
Attributes:
events: A dictionary used to store event information, where the key is the event date and the value is the list of events on that date.
Main methods:

__init__(self):

Initialization method, creates an empty event dictionary.
add_event(self, event_name, event_date):

Method to add events, accepts event name and date, and adds the event to the event list of the corresponding date.
If the date already exists, the event is added to the existing list, otherwise a new list is created.
view_events(self):

Method to view all events, prints the event list by date.
Uses the strftime method to format the date in the form of "YYYY-MM-DD HH:MM".
remove_event(self, event_name, event_date):

Method to delete events, accepts event name and date, and deletes the specified event from the event list of the corresponding date.
If the list is empty after deletion, the entry for that date is also deleted.
If the specified event is not found, output "Event '{event_name}' not found"
Main process:

Uses the strftime method of the datetime module to format the date.
When adding an event, check if the date already exists, if it does, append it, otherwise create a new date entry.
When viewing events, traverse the dictionary by date and print the event list for each date.
When deleting an event, check if the event exists under the specified date, if it does, delete it, and check if the list is empty, if it is, delete the date entry.
This class provides a simple way to manage schedules, where users can add, view, and delete events.

# Prompt
Your task is to generate python code to solve the following problem. The generated code must be placed between the ```python and ```, and only one code block is allowed: 
Write a program, "Implement a simple schedule manager: Python class implements event addition, viewing, and deletion functions"
Define a class named Schedule to implement a simple schedule management system. The following is a description of the code:

Schedule Class:

Purpose: Represents a schedule management system that can add, view, and delete events.
Attributes:
events: A dictionary used to store event information, where the key is the event date and the value is the list of events on that date.
Main methods:

__init__(self):

Initialization method, creates an empty event dictionary.
add_event(self, event_name, event_date):

Method to add events, accepts event name and date, and adds the event to the event list of the corresponding date.
If the date already exists, the event is added to the existing list, otherwise a new list is created.
view_events(self):

Method to view all events, prints the event list by date.
Uses the strftime method to format the date in the form of ""YYYY-MM-DD HH:MM"".
remove_event(self, event_name, event_date):

Method to delete events, accepts event name and date, and deletes the specified event from the event list of the corresponding date.
If the list is empty after deletion, the entry for that date is also deleted.
If the specified event is not found, output ""Event '{event_name}' not found""
Main process:

Uses the strftime method of the datetime module to format the date.
When adding an event, check if the date already exists, if it does, append it, otherwise create a new date entry.
When viewing events, traverse the dictionary by date and print the event list for each date.
When deleting an event, check if the event exists under the specified date, if it does, delete it, and check if the list is empty, if it is, delete the date entry.
This class provides a simple way to manage schedules, where users can add, view, and delete events.

You need to follow the function names or class names in the test cases. The generated code should not contain any test cases: 
class TestSchedule:
    def test_add_event(self, schedule):
        event_date = datetime(2023, 12, 20, 18, 0)
        schedule.add_event("生日聚会", event_date)

        assert event_date in schedule.events
        assert "生日聚会" in schedule.events[event_date]