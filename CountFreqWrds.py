from collections import Counter
s="She bought a bit of butter but the butter was bitter"
t="cat bat mat cat bat cat"
n=input("How many most common frequent words in the sentence do you wish to display?")
list1=s.split()
freq=Counter(list1).most_common(n)
print freq
