pharase = "Don't panic!"
plist = list(pharase)
print(pharase)
print(plist)

a = plist[1:8]
print(a)



a.remove("'")
print(a)
a.extend([a.pop(), a.pop()])
print(a)
a.insert(2, a.pop(3))
print(a)
new_phrase = ''.join(a)
print(a)
print(new_phrase)
