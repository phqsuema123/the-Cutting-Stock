def two_dimensional_cutting_stock(stock_width, stock_height, required_rectangles):
    n = len(required_rectangles)
    dp = {(0, 0): (0, [])}

    for w in range(1, stock_width + 1):
        for h in range(1, stock_height + 1):
            dp[(w, h)] = max(dp.get((w, h), (0, [])),
                             max((dp.get((w - rw, h - rh), (0, []))[0] + 1, dp.get((w - rw, h - rh), (0, []))[1] + [(rw, rh)])
                                 for rw, rh in required_rectangles))

    return dp[(stock_width, stock_height)]


# Example usage:
stock_width = 100  # Width of the stock material
stock_height = 50  # Height of the stock material
required_rectangles = [(30, 20), (20, 15), (40, 25)]  # Dimensions of required rectangles

max_quantity, cutting_solution = two_dimensional_cutting_stock(stock_width, stock_height, required_rectangles)
print("Maximum quantity of rectangles that can be produced:", max_quantity)
print("Cutting solution (dimensions of rectangles):", cutting_solution)

