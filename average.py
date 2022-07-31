def media(myArray):

    sumTotal = 0

    for n in myArray:
        sumTotal += n

    return sumTotal / len(myArray)

print(media([0, 5, 10, 15, 20]))
