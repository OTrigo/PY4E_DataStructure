name = input("Enter file:")
handle = open(name)

ranking = dict()
ordered_ranking = list()

for line in handle:
  if line.startswith("From"):
    words = line.split()
    if len(words) > 5:
      full_hour = words[5]
      hour = full_hour.split(":")[0]
      ranking[hour] = ranking.get(hour, 0) + 1

for key, value in ranking.items():
  new_tuple = (key, value)
  ordered_ranking.append(new_tuple)


ordered_ranking = sorted(ordered_ranking)

for value, key in ordered_ranking:
  print(value, key)