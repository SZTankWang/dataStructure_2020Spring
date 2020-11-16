def find_profit(i,array):
    if i < max(array):
        return max(array)-i
    else:
        return 0

def stock_buy_sell(array):
    record = []
    for i in range(len(array)-1):
        buy_day = array[i]
        sell_days = array[i+1:]
        record.append(find_profit(buy_day,sell_days))
    return max(record)

def main():
    l1 = [7,1,5,3,6,4]
    l2 = [7,6,4,3,2,1]
    l3 = [2,9,5,2,3,1,2]
    print(stock_buy_sell(l1))
    print(stock_buy_sell(l2))
    print(stock_buy_sell(l3))

main()

'''
def stock_buy_sell(lissy):
    ## Assuming input is valid
    max_profit = 0
    minimum = lissy[0]

    for each in lissy:
        this_profit = each - minimum
        if this_profit > max_profit:
            max_profit = this_profit

        if each < minimum:
            minimum = each

    return max_profit
'''
