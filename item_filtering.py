#f97a59fcf0549b421647e6e586ceefd2f871ce71f282fc063b722a666aa43761
from functools import partial


filter_by = lambda key: lambda value: lambda items: [
    item for item in items if item[key] == value
]

filter_by_category = partial(
    lambda key, value, items: filter_by(key)(value)(items), "category"
)

greater_than = lambda threshold: lambda x: x > threshold


if __name__ == "__main__":
    items = [
        {"name": "Ноутбук", "category": "electronics", "price": 1000},
        {"name": "Футболка", "category": "clothes", "price": 50},
        {"name": "Телефон", "category": "electronics", "price": 800},
        {"name": "Джинсы", "category": "clothes", "price": 100},
    ]
    numbers = [1, 5, 12, 3, 20, 8, 15, 2]

    filter_clothes = partial(filter_by_category, "clothes")
    over_ten = greater_than(10)

    print("Электроника:", filter_by("category")("electronics")(items))
    print("Одежда:", filter_clothes(items))
    print("Больше 10:", list(filter(over_ten, numbers)))
    print("Больше 5:", list(filter(greater_than(5), numbers)))
