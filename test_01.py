import random

def main():
    while True:
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        num = a * 10 + b
        if num != 0:
            break

    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)

    divisor_count = len(divisors)
    divisor_sum = sum(divisors)
    divisors_sorted = sorted(divisors)
    second_largest = divisors_sorted[-2]

    while True:
        user_input = input("Add 혹은 Answer를 입력하세요 (종료: quit): ")

        if user_input == "quit":
            break

        elif user_input == "Answer":
            print(divisor_count)
            print(divisor_sum)
            print(second_largest)

            guess = int(input())

            if guess == num:
                print("true")
                break
            else:
                print("false")
                if guess < num:
                    print("up")
                else:
                    print("down")

        elif user_input == "Add":
            print(num)
            user_sum = int(input())

            if user_sum == divisor_sum:
                print("true")
                break
            else:
                print("false")
                if user_sum < divisor_sum:
                    print("up")
                else:
                    print("down")

        else:
            print("잘못된 입력입니다.")

if __name__ == "__main__":
    main()