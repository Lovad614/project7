from typing import List, Dict


def filter_by_state(transactions: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Фильтрует список транзакций по их состоянию.
    """
    return [transaction for transaction in transactions if transaction["state"] == state]


def sort_by_date(transactions: List[Dict], order: bool = True) -> List[Dict]:
    """
    Сортирует список транзакций по дате.
    Возвращает:
    List[Dict]: Список транзакций, отсортированных по дате.
    """
    return sorted(transactions, key=lambda x: x["date"], reverse=order)
