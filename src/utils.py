def flatten(list_2d):
    try:
        return [item for sublist in list_2d for item in sublist]
    except TypeError:
        return list_2d
