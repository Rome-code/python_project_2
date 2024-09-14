def filter_by_state(list_of_dict: list, state: str="EXECUTED") -> list:
    """Функция, возвращающая список только тех словарей, где ключу 'state'
    соответствует аргументу state"""
    state_exec_list_dicts = []
    for dict in list_of_dict:
        if dict.get("state") == state:
            state_exec_list_dicts.append(dict)
    return state_exec_list_dicts


def sort_by_date(list_of_dict: list, sort_: bool=True) -> list:
    """Функция, возвращающая список словарей, которые сортированы по дате"""
    for dict in list_of_dict:
        list_of_dict_sort_date = sorted(list_of_dict, key=lambda dict: dict["date"], reverse=sort_)
    return list_of_dict_sort_date
