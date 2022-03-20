def result(is_prime):
    if is_prime:
        print("This number is prime")
    else:
        print("This number is not prime")


number = int(input())
prime = False
if number == 1:
    result(prime)
else:
    searching = True
    divisor = 2

    # if there is a factor
    # it should be found before
    # you reach the square root of
    # the number you are evaluating
    search_limit = int(number ** 0.5 + 1)

    while searching:
        is_a_factor = number % divisor == 0

        if is_a_factor:
            searching = False

        if divisor > search_limit:
            searching = False
            prime = True

        divisor += 1
    result(prime)
