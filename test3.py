import random

count_type1_p = 0
count_type2_p = 0
count_type3_p = 0
count_type1_m = 0
count_type2_m = 0
count_type3_m = 0
count_axle = 0

str1 = '00000'
str2 = '11100'
str3 = '11111'
str4 = '00000'
points = 500000


# for _ in range(points):
#     signal1 = random.randint(0, 1)
#     signal2 = random.randint(0, 1)
#     str1 += str(signal1)
#     str2 += str(signal2)

def find_axle(mass1: str = '', mass2: str = '', size: int = 0, reset: bool = True) -> int:
    global count_type1_p, count_type2_p, count_type3_p, count_type1_m, count_type2_m, count_type3_m, count_axle
    length_single = 2
    length_both = 1

    if reset:
        count_type1_p = 0
        count_type2_p = 0
        count_type3_p = 0
        count_type1_m = 0
        count_type2_m = 0
        count_type3_m = 0
        count_axle = 0
        return 0

    for i in range(size):
        if mass1[i] == '0' and mass2[i] == '1' and count_type1_m <= length_both:
            count_type1_m = 0
            count_type2_m = 0
            count_type3_m = 0
            count_type1_p += 1
        elif mass1[i] == '1' and mass2[i] == '0' and count_type1_p <= length_both:
            count_type1_p = 0
            count_type2_p = 0
            count_type3_p = 0
            count_type1_m += 1
        elif mass1[i] == '0' and mass2[i] == '0' and count_type1_p > length_single and count_type3_p == 0:
            count_type1_m = 0
            count_type2_m = 0
            count_type3_m = 0
            count_type2_p += 1
        elif mass1[i] == '0' and mass2[i] == '0' and count_type1_m > length_single and count_type3_m == 0:
            count_type1_p = 0
            count_type2_p = 0
            count_type3_p = 0
            count_type2_m += 1
        elif mass1[i] == '1' and mass2[i] == '0' and count_type2_p > length_both and count_type1_p > length_single:
            count_type1_m = 0
            count_type2_m = 0
            count_type3_m = 0
            count_type3_p += 1
            if count_type3_p > length_single:
                count_axle += 1
                count_type1_p = 0
                count_type2_p = 0
                count_type3_p = 0
        elif mass1[i] == '0' and mass2[i] == '1' and count_type2_m > length_both and count_type1_m > length_single:
            count_type1_p = 0
            count_type2_p = 0
            count_type3_p = 0
            count_type3_m += 1
            if count_type3_m > length_single:
                count_axle -= 1
                count_type1_m = 0
                count_type2_m = 0
                count_type3_m = 0
        else:
            count_type1_p = 0
            count_type2_p = 0
            count_type3_p = 0
            count_type1_m = 0
            count_type2_m = 0
            count_type3_m = 0
    return count_axle

#print(find_axle(str1, str2, len(str1), False))
#print(find_axle(str3, str4, len(str3), False))
pass
