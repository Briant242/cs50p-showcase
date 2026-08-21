def main():
    word = input("Hi there user what you wanna say? ")
    print(convert(word))

def convert(target):
    return target.capitalize().replace(":)", "🙂").replace(":(", "🙁")

main()

"""
I LOVE KHEICZEL LORICA SOMEDAY I'LL MET HER!
"""
