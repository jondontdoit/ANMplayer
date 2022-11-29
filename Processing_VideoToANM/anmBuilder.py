v = []

f = open("output.txt", "r")
for x in f:
  #print(x)
  y = x.split(",")
  for z in y:
    if z:
      v.append((int(z)))
      #v = v + str(int(z))
f.close()

output = bytearray(v)

# for x in output:
#   print(x)

f = open("output.anm", "wb")
f.write(output)
f.close()
