def myReverse(data):
    # returning a new reversed list
    return [data[i] for i in range(len(data)-1, -1, -1)]

print(myReverse([22, 23, 24, 25, 26, 27]))
