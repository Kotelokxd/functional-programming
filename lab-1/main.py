import csv
from io import StringIO
from typing import Optional


def petrov_parse_csv(data: str) -> list[dict[str, str]]:
    return list(csv.DictReader(StringIO(data)))


def petrov_compute_revenue(rows: list[dict]) -> float:
    return sum(
        map(
            lambda row: float(row["quantity"]) * float(row["price"]),
            rows
        )
    )


def petrov_top_item(rows: list[dict[str, str]]) -> Optional[dict[str, str]]:
    return max(
        rows,
        key=lambda row: float(row["quantity"]) * float(row["price"]),
        default=None
    )


data = """name,quantity,price
Хлеб,20,80
Молоко,15,120
Кофе,5,900
Шоколад,12,250
"""


print(f"Продажи: {petrov_parse_csv(data)}")

print(f"\nОбщая выручка: {petrov_compute_revenue(petrov_parse_csv(data))}")

print(f"\nСамая прибыльная позиция: {petrov_top_item(petrov_parse_csv(data))}")
