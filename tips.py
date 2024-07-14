import random

def get_daily_car_tip():
    tips = [
        "Check your tire pressure monthly for better fuel efficiency.",
        "Change your oil every 3,000-5,000 miles for optimal engine health.",
        "Rotate your tires every 6,000-8,000 miles for even wear.",
        "Keep your gas tank at least a quarter full to prevent fuel pump damage.",
        "Clean your headlights regularly for better visibility and safety."
    ]
    return random.choice(tips)