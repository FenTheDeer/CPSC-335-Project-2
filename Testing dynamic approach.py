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
                print(dp[i][j])  # To see the math in value
    # Maximum number of stocks is stored in dp[N][amount]
    return dp[N][amount]

# Sample input
N = 4
Stocks_and_values = [[3, 2], [4, 3], [5, 3], [6, 7]]
amount = 10

# Call the function with the sample input
stock = max_stocks(N, Stocks_and_values, amount)

print("The best bang for your buck would be {} stocks for ${}.".format(stock, amount))
