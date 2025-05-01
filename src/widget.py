from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(string: str) -> tuple[str, str]:
    """Функция маскировки цифр карты и счета"""
    string_split = string.split()
    name_card_or_score = " ".join(string_split[:2])
    number_card_or_score = string_split[-1]

    return name_card_or_score, number_card_or_score


test_card = "Visa Platinum 7000792289606361"
name_card, card_number = mask_account_card(test_card)
masked_number = get_mask_card_number(card_number)
print(f"{name_card} {masked_number}")


test_check = "Счет 35383033474447895560"
name_check, check_number = mask_account_card(test_check)
masked_check = get_mask_account(test_check)
print(f"Счет **{masked_check}")


def get_date(date: str) -> str:
    """Функция, которая преобразовывает формат даты в "ДД.ММ.ГГГГ" """

    date_obj = datetime.fromisoformat(date)
    formatted_date = date_obj.strftime("%d.%m.%Y")
    return formatted_date


print(get_date("2024-03-11T02:26:18.671407"))
