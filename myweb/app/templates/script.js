// JavaScript code
console.log("JavaScript file connected!");

class CuttingStockSolver {
  chooseProblem() {
      console.log("Choose the type of Cutting Stock Problem:");
      console.log("1. One-dimensional Cutting Stock Problem (1D CSP)");
      console.log("2. Two-dimensional Cutting Stock Problem (2D CSP)");
      console.log("3. Three-dimensional Cutting Stock Problem (3D CSP)");
      let choice = prompt("Enter your choice (1/2/3): ");
      if (choice === '1') {
          this.solve1DCSP();
      } else if (choice === '2') {
          this.solve2DCSP();
      } else if (choice === '3') {
          this.solve3DCSP();
      } else {
          console.log("Invalid choice. Please enter a valid option (1/2/3).");
      }
  }

  solve1DCSP() {
      console.log("Solving One-dimensional Cutting Stock Problem (1D CSP)");
      let stockLength = parseInt(prompt("Enter the length of the stock material: "));
      let requiredLengths = prompt("Enter the lengths of required pieces (comma-separated): ").split(',').map(Number);
      let requiredQuantities = prompt("Enter the quantities of required pieces (comma-separated): ").split(',').map(Number);

      let [maxQuantity, cuttingSolution] = this.oneDimensionalCuttingStock(stockLength, requiredLengths, requiredQuantities);
      console.log("Maximum quantity that can be produced:", maxQuantity);
      console.log("Cutting solution:", cuttingSolution);
  }

  solve2DCSP() {
      console.log("Solving Two-dimensional Cutting Stock Problem (2D CSP)");
      let stockWidth = parseInt(prompt("Enter the width of the stock material: "));
      let stockHeight = parseInt(prompt("Enter the height of the stock material: "));
      let requiredRectangles = [];
      let numRectangles = parseInt(prompt("Enter the number of required rectangles: "));
      for (let i = 0; i < numRectangles; i++) {
          let dimensions = prompt(`Enter dimensions of rectangle ${i+1} (width, height): `).split(',').map(Number);
          requiredRectangles.push(dimensions);
      }

      let [maxQuantity, cuttingSolution] = this.twoDimensionalCuttingStock(stockWidth, stockHeight, requiredRectangles);
      console.log("Maximum quantity of rectangles that can be produced:", maxQuantity);
      console.log("Cutting solution (dimensions of rectangles):", cuttingSolution);
  }

  solve3DCSP() {
      console.log("Solving Three-dimensional Cutting Stock Problem (3D CSP)");
      let stockWidth = parseInt(prompt("Enter the width of the stock material: "));
      let stockHeight = parseInt(prompt("Enter the height of the stock material: "));
      let stockLength = parseInt(prompt("Enter the length of the stock material: "));
      let requiredBoxes = [];
      let numBoxes = parseInt(prompt("Enter the number of required boxes: "));
      for (let i = 0; i < numBoxes; i++) {
          let dimensions = prompt(`Enter dimensions of box ${i+1} (width, height, length): `).split(',').map(Number);
          requiredBoxes.push(dimensions);
      }

      let [maxQuantity, cuttingSolution] = this.threeDimensionalCuttingStock(stockWidth, stockHeight, stockLength, requiredBoxes);
      console.log("Maximum quantity of boxes that can be produced:", maxQuantity);
      console.log("Cutting solution (dimensions of boxes):", cuttingSolution);
  }

  oneDimensionalCuttingStock(stockLength, requiredLengths, requiredQuantities) {
      let n = requiredLengths.length;
      let dp = Array(stockLength + 1).fill(0);
      let solution = Array(stockLength + 1).fill().map(() => []);

      for (let i = 1; i <= stockLength; i++) {
          for (let j = 0; j < n; j++) {
              if (requiredLengths[j] <= i && dp[i - requiredLengths[j]] + requiredQuantities[j] > dp[i]) {
                  dp[i] = dp[i - requiredLengths[j]] + requiredQuantities[j];
                  solution[i] = [...solution[i - requiredLengths[j]], requiredLengths[j]];
              }
          }
      }

      return [dp[stockLength], solution[stockLength]];
  }

  twoDimensionalCuttingStock(stockWidth, stockHeight, requiredRectangles) {
      let n = requiredRectangles.length;
      let dp = {};

      for (let w = 1; w <= stockWidth; w++) {
          for (let h = 1; h <= stockHeight; h++) {
              dp[[w, h]] = [0, []];
              for (let rectangle of requiredRectangles) {
                  let [rw, rh] = rectangle;
                  let [prevMax, prevSolution] = dp[[w - rw, h - rh]] || [0, []];
                  if (prevMax + 1 > dp[[w, h]][0]) {
                      dp[[w, h]] = [prevMax + 1, [...prevSolution, rectangle]];
                  }
              }
          }
      }

      return dp[[stockWidth, stockHeight]];
  }

  threeDimensionalCuttingStock(stockWidth, stockHeight, stockLength, requiredBoxes) {
      let n = requiredBoxes.length;
      let dp = {};

      for (let w = 1; w <= stockWidth; w++) {
          for (let h = 1; h <= stockHeight; h++) {
              for (let l = 1; l <= stockLength; l++) {
                  dp[[w, h, l]] = [0, []];
                  for (let box of requiredBoxes) {
                      let [rw, rh, rl] = box;
                      let [prevMax, prevSolution] = dp[[w - rw, h - rh, l - rl]] || [0, []];
                      if (prevMax + 1 > dp[[w, h, l]][0]) {
                          dp[[w, h, l]] = [prevMax + 1, [...prevSolution, box]];
                      }
                  }
              }
          }
      }

      return dp[[stockWidth, stockHeight, stockLength]];
  }
}

// Example usage:
let solver = new CuttingStockSolver();
solver.chooseProblem();
