input_file = input('Input the file name...')
file_handler = open(input_file)

counts = dict()
for line in file_handler:
	words = line.split()
	for word in words:
		counts[word] = counts.get(word, 0) + 1

list_to_sort = list()
for key, value in counts.items():
	new_tuple = (value, key)
	list_to_sort.append(new_tuple)

list_to_sort = sorted(list, reverse=True)

for value, key in list_to_sort[:10]:
	print(key, value)