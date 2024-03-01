import sys
#t

if len(sys.argv) != 2:
    print("Usage: python3 triangle.py <number_of_rows>")
    sys.exit(1)

try:
    rows = int(sys.argv[1])
except ValueError:
    print("Please enter a valid integer for the number of rows.")
    sys.exit(1)


def get_triangle(rows):
    triangle = []
    for i in range(rows):
        row = [1] * (i + 1)
        for j in range(i+1):
            if j != 0 and j != i:
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle


triangle = get_triangle(rows)
joined = [' '.join(map(str, r)) for r in triangle]
max_length = len(joined[-1])
for row in joined:
    print(row.center(max_length))
