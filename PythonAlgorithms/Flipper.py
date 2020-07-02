a = 1
b = 2
c = 3
d = 4

grid = [[1, 2],
        [3, 4]]

while True:
    enteredValue = input("Please enter H for Horizontal flip or V for Vertical Flip or type exit to quit")

    if enteredValue == 'exit':
        break

    enteredValue = list(enteredValue)

    for i in enteredValue:

        if i == 'V':
            grid.reverse()
            continue

        elif i == 'H':
            for number in grid:
                number.reverse()

        elif i == "D":
            grid.reverse()
            for number in grid:
                number.reverse()


        continue

    else:
        for number in grid:
            for i in grid:
                print(i, sep='\n')
            break
        break
    break
