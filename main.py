fileName ="data.txt"
openFile = open(fileName)

counter = 1
for x in openFile:
  x= x.strip()
  print(counter, x)
  counter +=1