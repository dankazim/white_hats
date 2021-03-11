sender = {''}

file_name = "mbox-short.txt"
open_file_data = open(file_name)
x=1
for line in open_file_data:
  line = line.strip()
  if (line.startswith('From: ')):
    # print(x,line[6:])
    sender.add(line[6:])
    x  +=1
print(sender)
for item in sender:
  print(item)

print(len(sender), "Sender")