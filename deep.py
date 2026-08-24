def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    answer = answer.strip().lower()
    deepthinking(answer)

def deepthinking(target):
    match target:
        case "42" | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")

main()
