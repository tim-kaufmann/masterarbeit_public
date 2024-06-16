from datetime import datetime

class Schedule:
    def __init__(self):
        self.events = {}

    def add_event(self, event_name, event_date):
        if event_date in self.events:
            self.events[event_date].append(event_name)
        else:
            self.events[event_date] = [event_name]

    def view_events(self):
        for date in sorted(self.events):
            formatted_date = date.strftime("%Y-%m-%d %H:%M")
            print(f"Events on {formatted_date}:")
            for event in self.events[date]:
                print(f" - {event}")

    def remove_event(self, event_name, event_date):
        if event_date in self.events:
            try:
                self.events[event_date].remove(event_name)
                if not self.events[event_date]:
                    del self.events[event_date]
            except ValueError:
                print(f"Event '{event_name}' not found")
        else:
            print(f"Event '{event_name}' not found")

# Example usage:
# schedule = Schedule()
# schedule.add_event("Birthday Party", datetime(2023, 12, 20, 18, 0))
# schedule.view_events()
# schedule.remove_event("Birthday Party", datetime(2023, 12, 20, 18, 0))
# schedule.view_events()
