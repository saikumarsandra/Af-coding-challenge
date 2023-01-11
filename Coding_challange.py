def is_prime(n):
    if n < 2:
        return None
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return [i] + [n // i]
    return "Prime!"

def prime_numbers_in_range(min_num, max_num):
    primes = []
    for num in range(min_num, max_num + 1):
        if is_prime(num) == "Prime!":
            primes.append(num)
    return primes

def main():
    while True:
        print("1. Check if a number is prime")
        print("2. Get prime numbers in a range")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            num = int(input("Enter a number: "))
            result = is_prime(num)
            if result == "Prime!":
                print(result)
            else:
                print(f"The factors of {num} are {result}")
        elif choice == 2:
            min_num = int(input("Enter the minimum number of the range: "))
            max_num = int(input("Enter the maximum number of the range: "))
            primes = prime_numbers_in_range(min_num, max_num)
            print(f"The prime numbers in the range {min_num} to {max_num} are {primes}")
        elif choice == 3:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
