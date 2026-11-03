import csv
from io import StringIO
from typing import Optional
#37e9ad519f22e34ac61a7ba3450b867e

SALES_DATA = """date,item,quantity,price
2026-09-01,Кофе,2,250
2026-09-02,Чай,3,150
2026-09-03,Торт,1,1200
"""
QUANTITY_FIELD = "quantity"
PRICE_FIELD = "price"


# Уровень 1: CSV -> список словарей
def parse_csv(data: str) -> list[dict]:
    return list(csv.DictReader(StringIO(data)))


# Уровень 2: общая выручка
def compute_revenue(rows: list[dict]) -> float:
    return sum(
        int(row[QUANTITY_FIELD]) * float(row[PRICE_FIELD])
        for row in rows
    )


# Уровень 3: товар с максимальной выручкой
def top_item(rows: list[dict]) -> Optional[dict]:
    return max(
        rows,
        key=lambda row: int(row[QUANTITY_FIELD]) * float(row[PRICE_FIELD]),
        default=None,
    )


# Основная программа
rows = parse_csv(SALES_DATA)

print("Данные:")
print(rows)

print("\nОбщая выручка:", compute_revenue(rows))

print("\nТовар с максимальной выручкой:")
print(top_item(rows))
