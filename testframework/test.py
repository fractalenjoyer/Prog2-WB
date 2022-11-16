low = []
high = []

while True:
    number = int(input())
    if number == 0:
        break
    response = input()
    if response == "too high":
        high.append(number)
    elif response == "too low":
        low.append(number)
    elif response == "right on":
        if number > min(high) or number < max(low):
            print("Stan is dishonest")
        else:
            print("Stan may be honest")
        low = []
        high = []