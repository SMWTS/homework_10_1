from datetime import datetime

def mask_account_card(account_or_card: str) -> str:
    """Функция принимает тип и номер карты или счета и возвращает строку с замаскированным номером"""
    account_or_card_split = account_or_card.split()

    if "Счет" in account_or_card:
        number_mask = "**" + account_or_card[-4:]
        return f"Счет {number_mask}"
    else:
        account_or_card_splited = account_or_card.split()
        card_type_sep = " ".join(account_or_card_splited[:-1])
        card_number_sep = account_or_card_splited[-1]
        number_mask = "" + card_number_sep[0:4] + " " + card_number_sep[4:6] + "** **** " + card_number_sep[-4:]
        return f"{card_type_sep} {number_mask}"


def get_date(date: str) -> str:
    """Функция, которая преобразовывает формат даты в "ДД.ММ.ГГГГ" """

    date_obj = datetime.fromisoformat(date)
    formatted_date = date_obj.strftime("%d.%m.%Y")
    return formatted_date


print(get_date("2024-03-11T02:26:18.671407"))
