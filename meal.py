def main():
    # Where's user would input their time and saved it as a value to "time" variable.
    time = (input("What's the time is it now [#:## OR ##:##]: "))

    # Variabel used to call the convert() function and save the value that returned from the function
    new_time = convert(time)

    # Main logic checking the time and choose it's breakfast, lunch, or dinner time!
    if 7.0 <= new_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= new_time <= 13.0:
        print("lunch time")
    elif 18.0 <= new_time <= 19.0:
        print("dinner time")
    else:
        print("Work!! Not eat time!!")


def convert(time):
    # Used to remove unnecessary extra space in the start and the end of the str value.
    time = time.strip()

    # Splitting the srt with ":" as the separator and give it as value to hours and minutes each.
    hours, minutes = time.split(":")

    # Turning the value type from str to int for the math calculation purpose.
    hours_int = int(hours)
    minutes_int = int(minutes)

    # Returning value to the variable that call convert() in main with minutes turned into hour
    return hours_int + (minutes_int / 60)

if __name__ == "__main__":
    main()
