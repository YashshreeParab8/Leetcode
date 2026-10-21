# random practice problems

# occurance of every number in given digit
# def count(n):
#     freq = [0] * 10
#     while n != 0:
#         last_digit = n%10
#         freq[last_digit]+=1
#         n //= 10
#     return freq
# n = 1234567789
# res = count(n)
# for i in range(len(res)):
#     if res[i]!=0:
#         # print(f"{i} -> {res[i]}") 
#         print((res[i]))

# anagram
# def anagram(n1,n2):
#     freq = [0] * 10
#     while n1 != 0:
#         last_digit = n1%10
#         freq[last_digit]+=1
#         n1 //= 10

#     while n2 != 0:
#         last_digit = n2%10
#         freq[last_digit]-=1
#         n2 //= 10

#     for i in freq:
#         if (i == 0):
#             return True
#     return False

# n1 = 1221
# n2 = 1213
# res = anagram(n1,n2)
# print( f"{n1} and {n2} are anagram: {res}")


# given an array print the number whose freq is >=3
# def count(n):
#     freq = [0] * 10
#     while n != 0:
#         last_digit = n%10
#         freq[last_digit]+=1
#         n //= 10
#     return freq
# n = 123456778999
# res = count(n)
# for i in range(len(res)):
#     if res[i]>=3:
#         print(f"{i} -> {res[i]}")
#         # print(res)

# def count(n, k):
#     freq = [0] * 10

    # if n == 0:
    #     freq[0] = 1

    # while n != 0:
    #     last_digit = n % 10
    #     freq[last_digit] += 1
    #     n //= 10
    #     return freq

    # res = count(n,k)
    # for i in range(len(res)):
    #     if freq[i] >= k:
    #         res.append(i)

    # return res