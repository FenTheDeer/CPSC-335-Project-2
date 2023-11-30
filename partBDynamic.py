def max_stocks(N, Stocks_and_values, amount):
    # Create a 2D array to store results of sub_problems
    dp = [[0] * (amount + 1) for _ in range(N + 1)]

    #print(N)
    #print(Stocks_and_values)
    #print(amount)
    # Fill the dp array using top-down dynamic programming
    for i in range(1, N + 1):
        for j in range(amount + 1):
            # If the current stock can be included
            if Stocks_and_values[i - 1][1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][ j - Stocks_and_values[i - 1][1]] + Stocks_and_values[i - 1][0])
            else:
                dp[i][j] = dp[i - 1][j]
    # Maximum number of stocks is stored in dp[N][amount]
    return dp[N][amount]

# Sample input
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

    result = max_stocks(N, Stocks_and_values, Amount)


    print("\nThe maximum amount of stocks that can be purchased with the current allowance from the list of stocks is: {}".format(result))

    print("\n----------------------------------")