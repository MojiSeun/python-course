var1 = [1,2,3,4,5,-1,-2,-3]
#
# while var1 < 20:
#     var1+=2
#     print(f'This is variable {var1}')
#     if(var1%3 == 0):
#         break

for i in var1:
    print(f'{i} is a number')

    # if i == 3:
    #     break
    if i <0:
        print(f'This is not a positive integer')
        break
