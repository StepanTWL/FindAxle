import random
from IPython.display import clear_output

count_type1 = 0
count_type2 = 0
count_type3 = 0
count_axle = 0
count = 0
str1 = ''
str2 = ''
length_single = 2
length_both = 1
points = 500000

for _ in range(points):
    signal1 = random.randint(0, 1)
    signal2 = random.randint(0, 1)
    str1 += str(signal1)
    str2 += str(signal2)

for i in range(points):
    if str1[i] == '0' and str2[i] == '1' and count_type2 == 0 and count_type3 == 0:
        count_type1 += 1
    elif str1[i] == '0' and str2[i] == '0' and count_type1 > length_single and count_type3 == 0:
        count_type2 += 1
    elif str1[i] == '1' and str2[i] == '0' and count_type2 > length_both and count_type1 > length_single:
        count_type3 += 1
    elif count_type3 > length_single:
        count_axle += 1
        clear_output()
        print(count_axle)
        print(str1[i-count_type1-count_type2-count_type3:i+1])
        print(str2[i-count_type1-count_type2-count_type3:i+1])
        print()
        count_type1 = 0
        count_type2 = 0
        count_type3 = 0
    else:
        count_type1 = 0
        count_type2 = 0
        count_type3 = 0

pass
