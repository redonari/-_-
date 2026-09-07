import unittest

from sales_analysis import SALES_DATA, compute_revenue, parse_csv, top_item


class SalesAnalysisTests(unittest.TestCase):
    def test_parse_csv(self) -> None:
        rows = parse_csv(SALES_DATA)

        self.assertEqual(
            rows,
            [
                {
                    "date": "2026-09-01",
                    "item": "Кофе",
                    "quantity": "2",
                    "price": "250",
                },
                {
                    "date": "2026-09-02",
                    "item": "Чай",
                    "quantity": "3",
                    "price": "150",
                },
                {
                    "date": "2026-09-03",
                    "item": "Торт",
                    "quantity": "1",
                    "price": "1200",
                },
            ],
        )

    def test_compute_revenue(self) -> None:
        rows = parse_csv(SALES_DATA)

        self.assertEqual(compute_revenue(rows), 2150.0)

    def test_top_item(self) -> None:
        rows = parse_csv(SALES_DATA)

        self.assertEqual(top_item(rows), rows[2])

    def test_empty_data(self) -> None:
        self.assertEqual(parse_csv(""), [])
        self.assertEqual(compute_revenue([]), 0)
        self.assertIsNone(top_item([]))
