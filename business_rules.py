SERVICE_FEE_THRESHOLD = 500.00
MANAGER_SIGNOFF_THRESHOLD = 2500.00


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
