from typing import Any, Dict, List

dict_filter = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(operation: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict]:
    """Функция возвращает новый список, отсортированный по заданному значению"""
    return [item for item in operation if item.get("state") == state]


print(filter_by_state(dict_filter, "EXECUTED"))
