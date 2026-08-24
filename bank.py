def main():
    greeting = input("Greeting : ")
    greeting = greeting.strip().lower()
    payment(greeting)

def payment(target):
    match target:
        case text if "hello" in target:
            print("$0")
        case text if target.startswith("h"):
            print("$20")
        case _:
            print("$100")

main()
