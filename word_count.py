
def words(phrase):
	list_words = phrase.split()
	temp_out = {}
	for elem in list_words:
		if elem in temp_out:
			continue
		else:
			temp_out[elem] = list_words.count(elem)

	out = {}

	for item in temp_out.items():
		if item[0].isdigit():
			out[int(item[0])] = item[1]
		else:
			out[item[0]] = item[1]

	return out