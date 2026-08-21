def main():
    print("You're on a room!")
    word = input("What you wanna to say? ")
    print(indoor(word))

def indoor(target):
    return target.strip().lower()

main()
