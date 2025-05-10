from typing import Any, Dict, List

dict_filter = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(operation: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict]:
    """Функция возвращает новый список, отфильтрованный по заданному значению"""
    return [item for item in operation if item.get("state") == state]


print(filter_by_state(dict_filter, "EXECUTED"))


dict_data = [
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]


def sort_by_date(sort_operation: List[Dict[str, Any]], rerverse: bool = True) -> List[Dict]:
    """Функция возвращает новый список, отсортированные по дате"""
    return sorted(sort_operation, key=lambda x: str(x.get("date")), reverse=rerverse)


print(sort_by_date(dict_data))
