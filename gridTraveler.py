def gridTravel (m, n):
    if (m == 1 and n == 1):
        return 1
    if (m == 0 or n == 0):
        return 0
    return gridTravel(m - 1, n) + gridTravel(m, n - 1)

if __name__ == "__main__":
    print(gridTravel(2, 3))