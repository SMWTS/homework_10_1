def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и маскирует его"""
    card_number = card_number.replace(" ", "")
    # Проверяем хватает цифр в номере карты
    if len(card_number) != 16:
        return "Введен неверный номер карты"

    result = []
    # Список для хранения замаскированного номера карты
    counter = 0
    # Счетчик цифр в номере карты, чтобы знать, какую заменить на *
    for number in card_number:
        counter += 1
        if 6 < counter <= len(card_number) - 4:
            result.append("*")
        else:
            result.append(number)
    masked_card = "".join(result)
    masked_card_result = []

    # список для хранения по четыре цифры номера карты
    for i in range(0, len(masked_card), 4):
        masked_card_result.append(masked_card[i : i + 4])
    masked_card_result_with_space = " ".join(masked_card_result)
    return masked_card_result_with_space


def get_mask_account(card_account: str) -> str:
    """Функция принимает номер счета и маскирует его,
    видны только последние 4 цифры номера, а перед ними **"""
    card_account = card_account.replace(" ", "")
    last_part = str(card_account[-4:])
    return f"**{last_part}"

