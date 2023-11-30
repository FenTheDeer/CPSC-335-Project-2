import itertools

def stock_maximization (M, combos, values, stock):
    working_stock =[]
    working_combos =[]
    working_values =[]
    best = None
    y=0
    for candidate in (combos):
        # print(candidate)
        verify_combinations(M, candidate, values, stock, working_stock, working_combos, working_values)
    
    # print(working_values)
    # print(working_stock)

    for x in working_combos:
        # print(x)
        # if best != None:
        #     print("{} and {}".format(working_values[best], working_stock[best]))
        if best == None or (working_values[y] < working_values[best]) or (working_stock[y] > working_stock[best]):
            best = y
        y=1+y
    return working_stock[best], working_values[best]

def verify_combinations(M, candidate_items, values, stock, working_stock, working_combos, working_values):
    total_price = 0
    total_stock = 0
    for item in candidate_items:
        location = stock.index(item)
        total_price += values[location]
        total_stock += item

    if total_price <= M:
        working_combos.append(candidate_items)
        working_stock.append(total_stock)
        working_values.append(total_price)


with open('test_cases.txt') as f:
    contents = f.read()
    count = contents.count("test_case")
#Reads while file and executes it into the terminal
exec(open('test_cases.txt').read())
for i in range(1, count+1):
    exec(globals()['test_case' + str(i)])
    print("\nTest case", i)
    print("\nNumber of Stocks: ")
    [print(N)]
    print("\nStocks and values: ")
    [print(a) for a in Stocks_and_values]
    print("\nAllowance: ")
    [print(Amount)]
    stock=[]
    values=[]
    possible_combos=[]
    for x in Stocks_and_values:
        stock.append(x[0])
    for x in Stocks_and_values:
        values.append(x[1])

    for r in range(1, len(stock) + 1):
        possible_combos.extend(itertools.combinations(stock, r))

    # print(possible_combos)

    stock, values = stock_maximization(Amount, possible_combos, values, stock)

    print("\nThe maximum amount of stocks that can be purchased with the current allowance from the list of stocks is: {}".format(stock))
    
    print("\n----------------------------------")