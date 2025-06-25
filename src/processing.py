def filter_by_state(dicts, state='EXECUTED'):
    """фильтруем функцию по State"""
    filtered_dicts =[]
    for d in dicts:
        if d['state'] == state:
            filtered_dicts.append(d)
    return filtered_dicts
