for num in range(0, 1000):
    if num > 1:
        for div in range(2, num):
            if not num % div:
                break
        else:
            print(num)
