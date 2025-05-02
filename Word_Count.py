word_count={}
for letter in "Banana":
   if letter in word_count:
       word_count[letter]+1
   else:
       word_count[letter] = 1

   print(word_count)
   # Output: {'b': 1, 'a': 3, 'n': 2}



