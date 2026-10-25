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
