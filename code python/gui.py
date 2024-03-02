import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class CuttingStockGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Cutting Stock Solver")

        self.problem_type_var = tk.StringVar()
        self.solver = CuttingStockSolver()

        self.create_widgets()

    def create_widgets(self):
        problem_label = ttk.Label(self.master, text="Choose the type of Cutting Stock Problem:")
        problem_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

        problem_radio1 = ttk.Radiobutton(self.master, text="One-dimensional (1D CSP)",
                                          variable=self.problem_type_var, value="1D")
        problem_radio1.grid(row=1, column=0, padx=10, pady=5)

        problem_radio2 = ttk.Radiobutton(self.master, text="Two-dimensional (2D CSP)",
                                          variable=self.problem_type_var, value="2D")
        problem_radio2.grid(row=1, column=1, padx=10, pady=5)

        problem_radio3 = ttk.Radiobutton(self.master, text="Three-dimensional (3D CSP)",
                                          variable=self.problem_type_var, value="3D")
        problem_radio3.grid(row=1, column=2, padx=10, pady=5)

        solve_button = ttk.Button(self.master, text="Solve", command=self.solve_problem)
        solve_button.grid(row=2, column=1, pady=10)

    def solve_problem(self):
        problem_type = self.problem_type_var.get()
        if problem_type == "":
            messagebox.showerror("Error", "Please select a problem type.")
            return

        if problem_type == "1D":
            self.solver.solve_1d_csp()
        elif problem_type == "2D":
            self.solver.solve_2d_csp()
        elif problem_type == "3D":
            self.solver.solve_3d_csp()

class CuttingStockSolver:
    def __init__(self):
        pass

    def solve_1d_csp(self):
        print("Solving One-dimensional Cutting Stock Problem (1D CSP)")
        stock_length = int(input("Enter the length of the stock material: "))
        required_lengths = list(map(int, input("Enter the lengths of required pieces (comma-separated): ").split(',')))
        required_quantities = list(map(int, input("Enter the quantities of required pieces (comma-separated): ").split(',')))

        max_quantity, cutting_solution = self.one_dimensional_cutting_stock(stock_length, required_lengths, required_quantities)
        print("Maximum quantity that can be produced:", max_quantity)
        print("Cutting solution:", cutting_solution)

    def solve_2d_csp(self):
        print("Solving Two-dimensional Cutting Stock Problem (2D CSP)")
        stock_width = int(input("Enter the width of the stock material: "))
        stock_height = int(input("Enter the height of the stock material: "))
        required_rectangles = []
        num_rectangles = int(input("Enter the number of required rectangles: "))
        for i in range(num_rectangles):
            dimensions = tuple(map(int, input(f"Enter dimensions of rectangle {i+1} (width, height): ").split(',')))
            required_rectangles.append(dimensions)

        max_quantity, cutting_solution = self.two_dimensional_cutting_stock(stock_width, stock_height, required_rectangles)
        print("Maximum quantity of rectangles that can be produced:", max_quantity)
        print("Cutting solution (dimensions of rectangles):", cutting_solution)

    def solve_3d_csp(self):
        print("Solving Three-dimensional Cutting Stock Problem (3D CSP)")
        stock_width = int(input("Enter the width of the stock material: "))
        stock_height = int(input("Enter the height of the stock material: "))
        stock_length = int(input("Enter the length of the stock material: "))
        required_boxes = []
        num_boxes = int(input("Enter the number of required boxes: "))
        for i in range(num_boxes):
            dimensions = tuple(map(int, input(f"Enter dimensions of box {i+1} (width, height, length): ").split(',')))
            required_boxes.append(dimensions)

        max_quantity, cutting_solution = self.three_dimensional_cutting_stock(stock_width, stock_height, stock_length, required_boxes)
        print("Maximum quantity of boxes that can be produced:", max_quantity)
        print("Cutting solution (dimensions of boxes):", cutting_solution)

    def one_dimensional_cutting_stock(self, stock_length, required_lengths, required_quantities):
        n = len(required_lengths)
        dp = [0] * (stock_length + 1)
        solution = [[] for _ in range(stock_length + 1)]

        for i in range(1, stock_length + 1):
            for j in range(n):
                if required_lengths[j] <= i and dp[i - required_lengths[j]] + required_quantities[j] > dp[i]:
                    dp[i] = dp[i - required_lengths[j]] + required_quantities[j]
                    solution[i] = solution[i - required_lengths[j]] + [required_lengths[j]]

        return dp[stock_length], solution[stock_length]

    def two_dimensional_cutting_stock(self, stock_width, stock_height, required_rectangles):
        n = len(required_rectangles)
        dp = {(0, 0): (0, [])}

        for w in range(1, stock_width + 1):
            for h in range(1, stock_height + 1):
                dp[(w, h)] = max(dp.get((w, h), (0, [])),
                                 max((dp.get((w - rw, h - rh), (0, []))[0] + 1, dp.get((w - rw, h - rh), (0, []))[1] + [(rw, rh)])
                                     for rw, rh in required_rectangles))

        return dp[(stock_width, stock_height)]

    def three_dimensional_cutting_stock(self, stock_width, stock_height, stock_length, required_boxes):
        n = len(required_boxes)
        dp = {(0, 0, 0): (0, [])}

        for w in range(1, stock_width + 1):
            for h in range(1, stock_height + 1):
                for l in range(1, stock_length + 1):
                    dp[(w, h, l)] = max(dp.get((w, h, l), (0, [])),
                                        max((dp.get((w - rw, h - rh, l - rl), (0, []))[0] + 1,
                                             dp.get((w - rw, h - rh, l - rl), (0, []))[1] + [(rw, rh, rl)])
                                            for rw, rh, rl in required_boxes))

        return dp[(stock_width, stock_height, stock_length)]

def main():
    root = tk.Tk()
    app = CuttingStockGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
