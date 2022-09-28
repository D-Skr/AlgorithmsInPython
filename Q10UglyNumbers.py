#Recursive function for successive divisions


def successive_div(x, y):
    while x % y == 0:
        x = x // y
    return x


print(successive_div(6, 2))


#function for checking if a number is ugly or not
def ugly_check(num):
    num = successive_div(num, 2)
    num = successive_div(num, 3)
    num = successive_div(num, 5)
    if num == 1:
        return True
    else:
        return False


print(ugly_check(6))


#function for finding the Nth ugly number
def nth_ugly(n):
    i = 1
    #ugly number count
    counter = 1

    #Looping through all integers until ugly count becomes n
    while n > counter:
        i += 1
        if ugly_check(i):
            counter += 1
    return i


num = nth_ugly(15)
print("15th Ugly number is: ", num)