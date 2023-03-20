exhibits = {500: 300, 600: 400, 200: 150, 400: 400, 800: 500}  # price: weight


def thief_greedy(exhibits: dict, n, m, k):  #экспонаты, количество экспонатов, количество заходов, максимальный вес
    exhibits_copy = exhibits.copy()
    tries = 0
    took_items = []
    if len(exhibits.keys()) < n:
        return -1
    price_for_kilo = {price / weight: price for price, weight in exhibits.items()}
    while tries < m and len(took_items) <= n:
        took_kilo = 0
        for item in sorted(price_for_kilo.keys(), reverse=True):
            if exhibits_copy[price_for_kilo[item]] + took_kilo <= k and len(took_items) < n and exhibits_copy[price_for_kilo[item]] != 0:
                took_items.append([price_for_kilo[item], exhibits_copy[price_for_kilo[item]]])
                took_kilo += exhibits_copy[price_for_kilo[item]]
                exhibits_copy[price_for_kilo[item]] = 0
        tries += 1

    return took_items


print(thief_greedy(exhibits, 4, 5, 500))