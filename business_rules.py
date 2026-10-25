SERVICE_FEE_THRESHOLD = 500.00
MANAGER_SIGNOFF_THRESHOLD = 2500.00
SECOND_CHEF_GUEST_THRESHOLD = 80
SECOND_CHEF_TOTAL_THRESHOLD = 3000.00


def calculate_food_cost(guest_price: float, guests: int) -> float:
    """Returns the food cost before any discount"""
    return guest_price * guests


def get_event_discount(guests: int, nonprofit: bool = False) -> float:
    """Returns the discount rate as a decimal, so 5% is 0.05"""
    if guests < 25:
        return 0.0
    elif guests <= 99:
        return 0.05
    elif guests >= 100 and nonprofit:
        return 0.12
    else:
        return 0.05


def calculate_event_total(
    guest_price: float, guests: int, nonprofit: bool = False
) -> float:
    """Returns the event total for one event: the discounted cost, plus the service fee when it applies"""
    food_cost = calculate_food_cost(guest_price, guests)
    discount_rate = get_event_discount(guests, nonprofit)
    discounted_cost = food_cost * (1 - discount_rate)
    service_fee = 0.0
    if discounted_cost <= SERVICE_FEE_THRESHOLD:
        service_fee = 75.00
    return discounted_cost + service_fee


def needs_signoff(total: float) -> bool:
    """Returns True when the event total needs a manager's sign-off, otherwise false"""
    return total > MANAGER_SIGNOFF_THRESHOLD


def needs_second_chef(guests: int, total: float) -> bool:
    """Returns True when the event needs a second chef, otherwise false"""
    return guests > SECOND_CHEF_GUEST_THRESHOLD or total >= SECOND_CHEF_TOTAL_THRESHOLD


def total_booked(events: list) -> float:
    """Returns the sum of the event totals for every event in the list"""
    event_totals = 0
    for event in events:
        event_totals += calculate_event_total(
            event["guest_price"], event["guests"], event["nonprofit"]
        )
    return event_totals
