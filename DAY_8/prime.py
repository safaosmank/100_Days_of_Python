def prime_checker(number):
    is_prime = True

    for i in range(2,number - 1):
        if number % i != 0:
            is_prime = True
            print(f"{n} is a prime number.")
        else:
            print(f" {n} is not a prime number.")



n = int(input("Check this number: "))
prime_checker(number=n)



