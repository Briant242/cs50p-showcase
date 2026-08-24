def main():
    file = input("Please input your file here : ")
    file = file.strip().lower()
    formatter(file)

def formatter(target):
    match target:
        case text if ".gif" in target:
            print("image/gif")
        case text if ".jpg" in target or ".jpeg" in target:
            print("image/jpeg")
        case text if ".png" in target:
            print("image/png")
        case text if ".pdf" in target:
            print("application/pdf")
        case text if ".txt" in target:
            print("text/plain")
        case text if ".zip" in target:
            print("application/zip")
        case _:
            print("application/octet-stream")

main()
