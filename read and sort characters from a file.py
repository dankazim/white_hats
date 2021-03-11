rpt ={}
fileName ="data.txt"
openFile = open(fileName)
counter = 1
for line in openFile:
 line= line.strip().lower()
 for x in line: 
  rpt[x] = rpt.get(x, 0) + 1
rpt.pop(' ')  #to delete the space   

key_list =list(rpt.keys())
key_list.sort()
for key in key_list:
  print(key,rpt[key])