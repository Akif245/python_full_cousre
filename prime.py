def prime_check(number):
    is_prime=True
    for i in range(2,number):
        if number %  i == 0 :
            is_prime=False
    if is_prime:
        print("It is a prime number \n")
    else:
        print("Not a prime number \n")
n=int(input("Enter n value\n"))
prime_check(number=n)
