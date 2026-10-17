class Node:
    def __init__(self, value, ri):
        self.value = value
        self.risk_index = ri

def generateNextRow(row):
    next_row = []
    for num in row:
        new_value_1 = num.value + num.risk_index
        new_value_2 = num.value - num.risk_index
        new_ri_1 = num.risk_index
        new_ri_2 = num.risk_index + 1
        next_row.append(Node(new_value_1, new_ri_1))
        next_row.append(Node(new_value_2, new_ri_2))
    return next_row

def calcPercentages(row):
    win_percent = 0
    zero_percent = 0
    loose_percent = 0
    for num in row:
        percent = abs( 1 / len(row) * 100 )
        if num.value > 0:
            win_percent += percent
        elif num.value < 0:
            loose_percent += percent
        else:
            zero_percent += percent
    return [str(win_percent) + "%", str(zero_percent) + "%", str(loose_percent) + "%"]

def printRow(row):
    statement = []
    for num in row:
        statement.append(num.value)
    print(statement)

row_1 = [Node(0, 1)]
printRow(row_1)
input(["0%", "100%", "0%"])
new_row = row_1
while True:
    new_row = generateNextRow(new_row)
    print("---")
    printRow(new_row)
    input(calcPercentages(new_row))
