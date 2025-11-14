# # fruits = ["Apple", "Pear", "Banana"]
# # for fruit in fruits:
# #     print(fruit)
# #     print(fruit + " Pie")
# # print(fruits)

# scores = [87, 59, 92, 73, 64, 100, 81, 45, 78, 69, 88, 53]

# # total = 0
# # for score in scores:
# #     total  += score

# # print(total)
# # print(sum(scores))  

# high_num = 0
# for score in scores:
#     if score > high_num:
#         high_num = score
# print(high_num)
# print(max(scores))
# total = 0
# for number in range(1, 101):
#     total += number

# print(total)

num = 0
for num in range(1, 101):
    if num % 3 == 0 and num % 5!= 0:
        print("Fizz")
    elif num % 5 == 0 and num % 3!= 0:
        print("Buzz")
    elif num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    else:
        print(num)
    

