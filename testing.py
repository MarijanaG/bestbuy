def get_inputs():
    """ Get user inputs """


result = []
for i in range(3):
    val = input("Enter a number")
    while True:
        try:
            result.append(int(val))
            break
        except Exception as e:
            print(e)


def sum_of_even(numbers):
    """ Sum up all the even numbers in the list """


total = 0
for num in numbers:
    if num % 2 == 0:
        total += 1
return total


def main():
    """ Call the other relevant functions """
    numbers = get_inputs()
    result = sum_of_even(numbers)
    print(f"To sum of even: {result}")


if __name__ == "__main__":
    main()