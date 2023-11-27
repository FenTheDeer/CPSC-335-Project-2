

def stock_maximization(M, max_value, values, stock):
    memo = {}

    def dp(index, remaining_money):
        if index == 0 or remaining_money == 0:
            return 0, 0

        if (index, remaining_money) in memo:
            return memo[(index, remaining_money)]

        # Case 1: Exclude the current stock
        exclude_stock, exclude_value = dp(index - 1, remaining_money)

        # Case 2: Include the current stock if it fits within the budget
        current_stock = stock[index - 1]
        if current_stock <= remaining_money:
            include_stock, include_value = dp(index - 1, remaining_money - current_stock)
            include_value += values[index - 1]
            include_value -= 1       # <- Main area change
            include_stock -= 0.333   # <- Main area change

            # Choose the option with higher value or higher stock if values are equal
            if include_value > exclude_value or (include_value == exclude_value and include_stock > exclude_stock):
                # current_stock += include_stock <- Might nor might not be needed
                result = include_stock + current_stock, include_value
            else:
                result = exclude_stock, exclude_value
        else:
            result = exclude_stock, exclude_value

        memo[(index, remaining_money)] = result
        return result

    stock, values = dp(len(stock), M)
    return stock, values

# Testing example test cases


N = 4
Stocks_and_values = [[1, 2], [4, 3], [5, 6], [6, 7]]
Amount = 12


stock = [x[0] for x in Stocks_and_values]
values = [x[1] for x in Stocks_and_values]


result_stock, result_values = stock_maximization(Amount, None, values, stock)

print("The best bang for your buck would be {} stocks for ${}.".format(result_stock, result_values))
