from datetime import datetime
import pytest
from output_9_CoT import Schedule

class TestSchedule:
    @pytest.fixture
    def schedule(self):
        return Schedule()
    def test_add_event(self, schedule):
        event_date = datetime(2023, 12, 20, 18, 0)
        schedule.add_event("生日聚会", event_date)
        assert event_date in schedule.events
        assert "生日聚会" in schedule.events[event_date]
    def test_add_duplicate_event(self, schedule):
        event_date = datetime(2023, 12, 20, 18, 0)
        schedule.add_event("生日聚会", event_date)
        schedule.add_event("生日聚会", event_date)
        assert len(schedule.events[event_date]) == 2
    def test_view_events(self, schedule, capsys):
        schedule.add_event("生日聚会", datetime(2023, 12, 20, 18, 0))
        schedule.add_event("项目截止日期", datetime(2023, 12, 25, 23, 59))
        schedule.add_event("面试", datetime(2024, 1, 5, 14, 30))
        schedule.view_events()
        captured = capsys.readouterr()
        assert "2023-12-20 18:00:\n- 生日聚会\n\n" in captured.out
        assert "2023-12-25 23:59:\n- 项目截止日期\n\n" in captured.out
        assert "2024-01-05 14:30:\n- 面试\n\n" in captured.out
    def test_remove_event(self, schedule, capsys):
        event_date = datetime(2023, 12, 20, 18, 0)
        schedule.add_event("生日聚会", event_date)
        schedule.remove_event("生日聚会", event_date)
        schedule.view_events()
        captured = capsys.readouterr()
        assert "2023-12-20 18:00:\n" not in captured.out
    def test_remove_nonexistent_event(self, schedule, capsys):
        schedule.add_event("生日聚会", datetime(2023, 12, 20, 18, 0))
        schedule.remove_event("项目截止日期", datetime(2023, 12, 25, 23, 59))
        schedule.view_events()
        captured = capsys.readouterr()
        assert "未找到事件'项目截止日期'" in captured.out
    def test_remove_event_multiple_times(self, schedule, capsys):
        event_date = datetime(2023, 12, 20, 18, 0)
        schedule.add_event("生日聚会", event_date)
        schedule.remove_event("生日聚会", event_date)
        schedule.remove_event("生日聚会", event_date)
        schedule.view_events()
        captured = capsys.readouterr()
        assert "2023-12-20 18:00:\n" not in captured.out
    def test_remove_event_with_different_date(self, schedule, capsys):
        event_date1 = datetime(2023, 12, 20, 18, 0)
        event_date2 = datetime(2023, 12, 25, 23, 59)
        schedule.add_event("生日聚会", event_date1)
        schedule.add_event("项目截止日期", event_date2)
        schedule.remove_event("生日聚会", event_date2)
        schedule.view_events()
        captured = capsys.readouterr()
        assert "2023-12-20 18:00:\n- 生日聚会\n\n" in captured.out
        assert "2023-12-25 23:59:\n- 项目截止日期\n\n" in captured.out
    def test_remove_event_from_empty_schedule(self, schedule, capsys):
        schedule.remove_event("生日聚会", datetime(2023, 12, 20, 18, 0))
        schedule.view_events()
        captured = capsys.readouterr()
        assert "未找到事件'生日聚会'" in captured.out