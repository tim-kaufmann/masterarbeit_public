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
        for event_date in sorted(self.events):
            formatted_date = event_date.strftime("%Y-%m-%d %H:%M")
            events = ", ".join(self.events[event_date])
            print(f"{formatted_date}: {events}")

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