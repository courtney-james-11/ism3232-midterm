from business_rules import (
    calculate_event_total,
    calculate_food_cost,
    get_event_discount,
    needs_signoff,
)


def test_calculate_food_cost():
    assert round(calculate_food_cost(50.00, 10), 2) == 500.00


def test_get_event_discount_none():
    assert get_event_discount(10) == 0.0


def test_get_event_discount_5():
    assert get_event_discount(50) == 0.05


def test_get_event_discount_12():
    assert get_event_discount(150, nonprofit=True) == 0.12


def test_get_event_discount_100_guests_fp():
    assert get_event_discount(100) == 0.05


def test_calculate_event_total_no_service_fee():
    assert round(calculate_event_total(50.00, 100), 2) == 4750.00


def test_calculate_event_total_service_fee():
    assert round(calculate_event_total(50.00, 10), 2) == 575.00


def test_needs_signoff_true():
    assert needs_signoff(3500.00) == True


def test_needs_signoff_false():
    assert needs_signoff(2500.00) == False
