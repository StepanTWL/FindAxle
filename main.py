import random
from IPython.display import clear_output

count_type1 = 0
count_type2 = 0
count_type3 = 0
count_axle = 0
count = 0

while True:
	count += 1
	signal1 = random.randint(0, 1)
	signal2 = random.randint(0, 1)

	if signal1 == 0 and signal2 == 1:
		count_type1 += 1
	elif signal1 == 0 and signal2 == 0 and count_type1 > 0:
		count_type2 += 1
	elif signal1 == 1 and signal2 == 0 and count_type2 > 0:
		count_type3 += 1
	elif count_type1 > 5 and count_type2 > 4 and count_type3 > 5:
		count_type1 = 0
		count_type2 = 0
		count_type3 = 0
		count_axle += 1
		clear_output()
		print(count, count_axle)




