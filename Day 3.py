# Assignment Day 3: From a dict, how can we print the Key whose value is maximum

s = 'welcome'
d = {}

for i in s:
  d[i] = d.get(i, 0) + 1
  #print(d)

print(d)
max_key = max(d, key=d.get)
print (max_key)
