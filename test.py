import random
from IPython.display import clear_output

count_type1 = 0
count_type2 = 0
count_type3 = 0
count_axle = 0
count = 0
str1 = ''
str2 = ''
length_single = 3
length_both = 2

while True:
    count += 1
    signal1 = random.randint(0, 1)
    signal2 = random.randint(0, 1)
    str1 += str(signal1)
    str2 += str(signal2)

    if signal1 == 0 and signal2 == 1 and count_type2 == 0 and count_type3 == 0:
        count_type1 += 1
    elif signal1 == 0 and signal2 == 0 and count_type1 > length_single and count_type3 == 0:
        count_type2 += 1
    elif signal1 == 1 and signal2 == 0 and count_type2 > length_both and count_type1 > length_single:
        count_type3 += 1
    elif count_type3 > length_single:
        count_type1 = 0
        count_type2 = 0
        count_type3 = 0
        count_axle += 1
        clear_output()
        print(count, count_axle)
        print(str1)
        print(str2)
        print()
        str1 = ''
        str2 = ''
    else:
        count_type1 = 0
        count_type2 = 0
        count_type3 = 0
        str1 = ''
        str2 = ''

    """
	elif count_type1 > 4 and count_type2 > 3 and count_type3 > 4:
		count_type1 = 0
		count_type2 = 0
		count_type3 = 0
		count_axle += 1
		clear_output()
		print(count, count_axle, str1, str2)
		str1 = ''
		str2 = ''
		break
	"""
