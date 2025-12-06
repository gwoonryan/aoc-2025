def main():
    with open("input", "r") as file:
        lines = file.readlines()
    n_0 = 0
    current_numer = 50
    for line in lines:
        stripped = line.strip()
        side = 1 if stripped[0] == 'R' else -1
        amount = int(stripped[1:])
        current_numer += side * amount
        current_numer = current_numer % 100
        if current_numer == 0:
            n_0 += 1
    print(n_0)


if __name__ == "__main__":
    main()
