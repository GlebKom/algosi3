def make_change_greedy(coin_value_dict, change):
    collected_change = []
    coin_value_dict_copy = coin_value_dict.copy()
    while sum(collected_change) != change:
        changed = False
        for i in sorted(coin_value_dict_copy, reverse=True):
            if sum(collected_change) + i <= change and coin_value_dict_copy[i] > 0:
                collected_change.append(i)
                coin_value_dict_copy[i] -= 1
                changed = True
                break
        if not changed:
            break
    if sum(collected_change) == change:
        return collected_change
    return -1


def make_change_rec(coin_value_dict, change, known_result):
    min_coins = [None] * (change + 1)
    if change in coin_value_dict.keys():
        known_result[change] = [change]
        return [change]
    elif known_result[change] != 0:
        return known_result[change]
    else:
        for i in [c for c in coin_value_dict.keys() if c <= change and coin_value_dict[c] > 0]:
            coin_value_dict_copy = coin_value_dict.copy()
            coin_value_dict_copy[i] -= 1
            num_coins = [i] + make_change_rec(coin_value_dict_copy, change - i, known_result)
            if len(num_coins) < len(min_coins):
                min_coins = num_coins
                known_result[change] = min_coins
    return min_coins


def main():
    amount = 77
    coins = {50: 27, 20: 1, 17: 1, 10: 1, 5: 1, 1: 5}
    print('Жадный алгоритм: ', end='')
    if make_change_greedy(coins, amount) != -1:
        print(make_change_greedy(coins, amount))
    else:
        print('Нельзя сдать сдачу.')
    print('Рекурсивный алгоритм: ', end='')
    if make_change_rec(coins, amount, [0] * (amount + 1)).count(None) > 0:
        print('Нельзя сделать сдачу.')
    else:
        print(make_change_rec(coins, amount, [0] * (amount + 1)))

main()
