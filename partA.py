import itertools

def stock_maximization (M, combos, values, stock):
    best = None
    for candidate in (combos):
        if verify_combinations(M, combos, candidate, values, stock):
              if best is None or total_value(candidate) > total_value(best):
                    best = candidate
    return best

def verify_combinations(M, items, candidate_items, values, stock):
    total_price = 0
    for item in candidate_items:
        print(candidate_items)
        total_price = 0
        for x in candidate_items:
            # print(x)
            location = stock.index(item)
            total_price += values[location]
            print(total_price)

    # if total_price <= M:
    #     return True
    # else:
    #     return False

def total_value(candidate_items):
    total_value = 0
    for item in candidate_items:
        total_value += [item, 1]
    return total_value    

N = 4 
Stocks_and_values = [ [1, 2], [4, 3], [5, 6], [6, 7] ]
Amount = 12

stock=[]
values=[]
possible_combos=[]
for x in Stocks_and_values:
    stock.append(x[0])
for x in Stocks_and_values:
    values.append(x[1])

for r in range(1, len(stock) + 1):
      possible_combos.extend(itertools.combinations(stock, r))

print(possible_combos)

stock_maximization(Amount, possible_combos, values, stock)

#[0] is the number of stocks, [1] is the value for the stocks
#sample output should be 11, 1+4+6 at index 0,1,3, sum of the values at these indices = 2+3+7<=12