name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counter = dict()

for words in handle:
  if words.startswith("From:"):
    pieces = words.split()
    formatted_email = pieces[1].strip()
    counter[formatted_email] = counter.get(formatted_email, 0) + 1

who_many_times = None
who_is = None
    
for key, value in counter.items():
  if who_many_times is None or value > who_many_times:
    who_many_times = value
    who_is = key
    
print(who_is, who_many_times)