def solve(grid, rules):
    height = len(grid)
    width = len(grid[0])
    new_grid = []
    for i in range(height - 1):
        row = []
        for j in range(width - 1):
            pattern = [grid[i][j], grid[i][j + 1], grid[i + 1][j], grid[i + 1][j + 1]]
            transformed = False

            for rule in rules:
                if rule['pattern'] == pattern:
                    row.append(rule['result'])
                    transformed = True
                    break
            
            if not transformed:
                row.append(0)  
        
        new_grid.append(row)

    return new_grid

grid = [[1, 1, 1], [1, 1, 4], [1, 4, 6]]
rules = [{"pattern": [1, 1, 1, 1], "result": 5}, {"pattern": [1, 1, 1, 4], "result": 6}]

solution = solve(grid, rules)
print(solution) 
