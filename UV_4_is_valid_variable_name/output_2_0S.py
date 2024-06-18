from datetime import datetime

class Schedule:
    def __init__(self):
        self.events = {}

    def add_event(self, event_name, event_date):
        event_date_str = event_date.strftime("%Y-%m-%d %H:%M")
        if event_date_str in self.events:
            self.events[event_date_str].append(event_name)
        else:
            self.events[event_date_str] = [event_name]

    def view_events(self):
        for event_date_str, event_list in self.events.items():
            print(f"{event_date_str}: {', '.join(event_list)}")

    def remove_event(self, event_name, event_date):
        event_date_str = event_date.strftime("%Y-%m-%d %H:%M")
        if event_date_str in self.events:
            try:
                self.events[event_date_str].remove(event_name)
                if not self.events[event_date_str]:
                    del self.events[event_date_str]
            except ValueError:
                print(f"Event '{event_name}' not found")
        else:
            print(f"Event '{event_name}' not found")

# Example usage
# schedule = Schedule()
# schedule.add_event("Meeting", datetime(2023, 6, 16, 14, 0))
# schedule.view_events()
# schedule.remove_event("Meeting", datetime(2023, 6, 16, 14, 0))
# schedule.view_events()
