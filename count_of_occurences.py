from collections import Counter

str = 'aaaabbbccccdddeeeggggghhhhgkkasasasnd'

str_counter={}
for i in range(len(str)):
    if str[i] in str_counter:
        str_counter[str[i]] += 1
    else:
       str_counter[str[i]] = 1


print("My result:", str_counter)
print("Correct Counter result:", Counter(str))

