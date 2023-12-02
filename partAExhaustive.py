#Used to get all possible combinations.
import itertools

def stock_maximization (M, combos, values, stock):
    #A place to store working combinations as well as their price and amount of stocks from the working combinations
    working_stock =[]
    working_combos =[]
    working_values =[]
    best = None

    y=0
    #Goes through every combination in the combo paramater to feed into the verify_combinations function
    for candidate in (combos):
        verify_combinations(M, candidate, values, stock, working_stock, working_combos, working_values)

    #Goes through the Working Combination array to determine the best deal.
    for x in working_combos:
        #If best is "None", fills up with first index (0).
        #Otherwise, if the value is cheaper than the best or amount of stock is better than the current best, push index to best.
        if best == None or (working_values[y] < working_values[best]) or (working_stock[y] > working_stock[best]):
            best = y
        y=1+y
    #Returns values
    return working_stock[best]

#Function to confirm which combinations give a value less than 
def verify_combinations(M, candidate_items, values, stock, working_stock, working_combos, working_values):
    total_price = 0
    total_stock = 0

    #Goes through the candidate in order to find the location in the stock array
    #Then uses the index of item to find the location of the price in the values array to add to the total price.
    #Then number of stocks is added to the total stock.
    for item in candidate_items:
        location = stock.index(item)
        total_price += values[location]
        total_stock += item

    #If total price is less than the allowance "M", the candidate combination, price for the stocks, and number of stocks
    #   is pushed to their respective "working" array
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

    #Uses Itertools in order to get all possible combinations of stocks
    for r in range(1, len(stock) + 1):
        possible_combos.extend(itertools.combinations(stock, r))

    # print(possible_combos)

    #Calls function, and then gets the return max amount of stocks that can be purchased
    stock = stock_maximization(Amount, possible_combos, values, stock)

    print("\nThe maximum amount of stocks that can be purchased with the current allowance from the list of stocks is: {}".format(stock))
    
    print("\n----------------------------------")