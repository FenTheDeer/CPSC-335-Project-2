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
        if best == None or ((working_values[y] > working_values[best]) or (working_values[y] < working_values[best] and working_stock[y] > working_stock[best])):
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


#Testing example testcases
N = 4 
Stocks_and_values = [ [3, 2], [6, 3], [5, 3], [6, 7] ]
Amount = 10

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

print("The best bang for your buck would be {} stocks for ${}.".format(stock, values))
