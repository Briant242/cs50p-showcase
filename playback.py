def main():
    word = input("What's your words? ")
    print(playback(word))

def playback(target):
    return target.strip().replace(" ", "...")

main()
