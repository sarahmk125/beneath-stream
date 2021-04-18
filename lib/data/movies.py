from datetime import datetime


def write_data():
    await stream.write({
        "title":       "Star Wars: Episode IV",
        "released_on": datetime(year=1977, month=5, day=25),
        "director":    "George Lucas",
        "budget_usd":  11000000,
        "rating":      8.6,
    })
