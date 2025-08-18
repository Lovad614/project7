def filter_by_currency(items: list, cur: str) -> Generator[dict]:
    """Фильтрует транзакции по валюте 'RUB'"""
    for item in items:
        if (
            "operationAmount" in item
            and "currency" in item["operationAmount"]
            and "code" in item["operationAmount"]["currency"]
        ):
            if cur == item["operationAmount"]["currency"]["code"]:
                yield item


def transaction_descriptions(items: list[dict[str, object]]) -> Generator[dict]:
    """Возвращает описание транзакции"""
    for item in items:
        yield item["description"]


def card_number_generator(start: int, stop: int) -> Generator[int]:
    """Генератор, выдает номера банковских карт в формате ХХХХ ХХХХ ХХХХ ХХХХ"""
    if start > stop:
        raise ValueError("значение start должно быть меньше или равно значению stop")
    for number in range(start, stop + 1):
        number_card = str(number).zfill(16)
        formatted_card_number = (
            number_card[0:4] + " " + number_card[4:8] + " " + number_card[8:12] + " " + number_card[12:16]
        )
        yield formatted_card_number
