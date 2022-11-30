def main():
    time = input("What time is it? ")
    time = convert(time)
    if 6.99 < time < 8.01:
        print("breakfast time")
    elif 11.99 < time < 13.01:
        print("lunch time")
    elif 17.99 < time < 19.01:
        print("dinner time")
def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    if minutes.endswith("a.m."):
        minutes = minutes.removesuffix('a.m.')
    elif minutes.endswith("p.m."):
        minutes = minutes.removesuffix('p.m.')
        hours = hours + 12
    minutes = float(minutes) / 60
    time = hours + minutes
    return time
if __name__ == "__main__":
    main()