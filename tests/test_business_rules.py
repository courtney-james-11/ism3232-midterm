# tests/test_business_rules.py
# Author: Courtney James

from business_rules import (
    calculate_event_total,
    calculate_food_cost,
    format_event_line,
    get_event_discount,
    largest_event,
    needs_second_chef,
    needs_signoff,
    total_booked,
)


def test_calculate_food_cost():
    assert round(calculate_food_cost(50.00, 10), 2) == 500.00


def test_get_event_discount_none():
    assert get_event_discount(10) == 0.0


def test_get_event_discount_5_limit():
    assert get_event_discount(25) == 0.05


def test_get_event_discount_5():
    assert get_event_discount(99) == 0.05


def test_get_event_discount_12():
    assert get_event_discount(150, nonprofit=True) == 0.12


def test_get_event_discount_12_limit():
    assert get_event_discount(100, nonprofit=True) == 0.12


def test_get_event_discount_limit_guests_fp():
    assert get_event_discount(100) == 0.05


def test_get_event_discount_upper_fp():
    assert get_event_discount(150) == 0.05


def test_calculate_event_total_no_service_fee():
    assert round(calculate_event_total(50.00, 100), 2) == 4750.00


def test_calculate_event_total_service_fee():
    assert round(calculate_event_total(50.00, 10), 2) == 575.00


def test_needs_signoff_true():
    assert needs_signoff(3500.00) == True


def test_needs_signoff_false_limit():
    assert needs_signoff(2500.00) == False


def test_needs_signoff_false():
    assert needs_signoff(2000.00) == False


def test_needs_second_chef_guests_true():
    assert needs_second_chef(100, 2000.00) == True


def test_needs_second_chef_guests_false_limit():
    assert needs_second_chef(80, 2000.00) == False


def test_needs_second_chef_total_true_limit():
    assert needs_second_chef(50, 3000.00) == True


def test_needs_second_chef_total_false():
    assert needs_second_chef(50, 2000.00) == False


def test_total_booked():
    events = [
        {"client": "Finch Law", "guest_price": 18.00, "guests": 20, "nonprofit": False},
        {
            "client": "Garden Club",
            "guest_price": 22.00,
            "guests": 40,
            "nonprofit": True,
        },
        {
            "client": "Hilltop Gym",
            "guest_price": 30.00,
            "guests": 120,
            "nonprofit": False,
        },
    ]
    assert round(total_booked(events), 2) == 4691.00


def test_largest_event():
    events = [
        {"client": "Finch Law", "guest_price": 18.00, "guests": 20, "nonprofit": False},
        {
            "client": "Garden Club",
            "guest_price": 22.00,
            "guests": 40,
            "nonprofit": True,
        },
        {
            "client": "Hilltop Gym",
            "guest_price": 30.00,
            "guests": 120,
            "nonprofit": False,
        },
    ]
    assert largest_event(events) == "Hilltop Gym"


def test_format_event_line():
    assert (
        format_event_line("Finch Law", 435.00, False, False)
        == "Finch Law: $435.00 | sign-off: no | second chef: no"
    )
