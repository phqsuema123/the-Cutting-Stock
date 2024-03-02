def one_dimensional_cutting_stock(stock_length, required_lengths, required_quantities):
    n = len(required_lengths)
    dp = [0] * (stock_length + 1)
    solution = [[] for _ in range(stock_length + 1)]

    for i in range(1, stock_length + 1):
        for j in range(n):
            if required_lengths[j] <= i and dp[i - required_lengths[j]] + required_quantities[j] > dp[i]:
                dp[i] = dp[i - required_lengths[j]] + required_quantities[j]
                solution[i] = solution[i - required_lengths[j]] + [required_lengths[j]]

    return dp[stock_length], solution[stock_length]


# Example usage:
stock_length = 100  # Length of the stock material
required_lengths = [30, 50, 70]  # Lengths of required pieces
required_quantities = [3, 2, 1]  # Quantities of required pieces

max_quantity, cutting_solution = one_dimensional_cutting_stock(stock_length, required_lengths, required_quantities)
print("Maximum quantity that can be produced:", max_quantity)
print("Cutting solution:", cutting_solution)
