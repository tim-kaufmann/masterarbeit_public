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
        for date, events in sorted(self.events.items()):
            print(f"{date}: {', '.join(events)}")

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

# Example usage:
# schedule = Schedule()
# event_date = datetime(2023, 12, 20, 18, 0)
# schedule.add_event("Birthday Party", event_date)
# schedule.view_events()
# schedule.remove_event("Birthday Party", event_date)
# schedule.view_events()
