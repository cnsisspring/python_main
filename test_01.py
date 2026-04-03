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
    second_largest = sorted(divisors)[-2]

    while True:
        mode = input("Add 혹은 Answer를 입력하세요 (종료: quit): ")

        if mode == "quit":
            break

        if mode == "Answer":
            print(divisor_count)
            print(divisor_sum)
            print(second_largest)

            while True:
                user = input()

                if user == "quit":
                    return

                guess = int(user)

                if guess == num:
                    print("true")
                    return
                else:
                    print("false")
                    if guess < num:
                        print("up")
                    else:
                        print("down")

        elif mode == "Add":
            print(num)

            while True:
                user = input()

                if user == "quit":
                    return

                user_sum = int(user)

                if user_sum == divisor_sum:
                    print("true")
                    return
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