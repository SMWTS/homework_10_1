from typing import Generator, Iterator
from typing import Any, Dict, List

def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[dict]:
    for item in transactions:
        if item.get('operationAmount', {}).get('currency', {}).get('code', {}) == currency:
            yield item

    filter_curr = filter_by_currency(transactions, "USD")
    print(next(filter_curr))


def card_number_generator(start, stop) -> Any:
    """Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999"""
    start_card_number = "0000000000000000"
    nums = (num for num in range(start, stop+1))
    for num in nums:
        card_number = start_card_number[:-len(str(num))] + str(num)
        if len(card_number) > 16:
            raise ValueError ("В номере карты не может быть больше 16 цифр")
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"

