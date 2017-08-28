import multiprocessing as mp


def washer(dishes, output):
    for dish in dishes:
        print("Washing", dish, 'dish')
        output.put(dish)
