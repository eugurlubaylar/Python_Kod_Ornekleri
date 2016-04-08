# Program to transpose a matrix using nested loop

x = [[12, 7],
     [4, 5],
     [3, 8]]

result = [[0,0,0],
          [0,0,0]]

# iterate through rows
for i in range(len(x)):
    # iterate through columns
    for j in range(len(x[0])):
        result[j][i] = x[i][j]

for r in result:
    print(r)
