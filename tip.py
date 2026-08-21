def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    data = d.removeprefix("$")
    data = float(data)
    return round(data, 2)


def percent_to_float(p):
    data2 = p.removesuffix("%")
    data2 = float(data2)
    return data2 / 100


main()
