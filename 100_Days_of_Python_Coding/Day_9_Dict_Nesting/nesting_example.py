capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a List in a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": [
        "Berlin",
        "Hamburg",
        "Stuttgart",
    ],
}

# Nesting with List and Dict in Dictionary.

detailed_travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": [
        "Berlin",
        "Hamburg",
        "Stuttgart",
    ],
}

# Nesting Dictionaries inside a List

detailed_travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": [
            "Berlin",
            "Hamburg",
            "Stuttgart",
        ],
        "total_visits": 6,
    },
]
