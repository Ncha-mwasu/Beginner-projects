def safe_print_list(my_list=[], x=0):
    i = 0
    while i < x:
        try:
            num = my_list[i]
            i += 1
            print("{}".format(num), end="")

        except IndexError:
            break
    print()
    return i

# def safe_print_list(my_list=[], x=0):
#     count = 0
#     for num in range(x):
#         try:
#             print("{}".format(my_list[num]), end="")
#             count += 1
#         except:
#             break
#     print()
#     return count

