# Check if a number is Armstrong or not

def armstrong_num(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp = temp // 10
    if num == sum:
        print(f"{num} is an Armstrong number")
    else:
        print(f"{num} is not an Armstrong number")


num = int(input("Enter the number: "))
armstrong_num(num)
