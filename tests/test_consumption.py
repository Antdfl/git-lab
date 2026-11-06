from consumption import compute_consumption


def test_consumption_is_difference_between_consecutive_readings():
    readings = [
        {"pdr": "A", "reading_date": "2026-01-01", "reading_value": 100.0},
        {"pdr": "A", "reading_date": "2026-02-01", "reading_value": 130.0},
    ]
    result = compute_consumption(readings)
    assert result == [{"pdr": "A", "period_end": "2026-02-01", "consumption": 30.0}]

def test_negative_consumption_is_skipped():
    readings = [
        {"pdr": "A", "reading_date": "2026-01-01", "reading_value": 900.0},
        {"pdr": "A", "reading_date": "2026-02-01", "reading_value": 5.0},
    ]
    assert compute_consumption(readings) == []
