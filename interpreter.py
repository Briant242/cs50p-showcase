def main():
    user_input = input("What mathematical operation you want? (Format (x, y, z) Example : 2 + 3) : ").strip()
    x, y, z= user_input.split(" ")
    x = float(x)
    z = float(z)
    operation(x, y, z)

def operation(x, y, z):
    match x, y, z:
        case (_, "+", _):
            output = x + z
            print(f"{output}")
        case (_, "-", _):
            output = x - z
            print(f"{output}")
        case (_, "*", _):
            output = x * z
            print(f"{output}")
        case (_, "/", _):
            output = x / z
            print(f"{output}")

main()
