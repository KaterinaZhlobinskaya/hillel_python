srtoka = "97 більше ніж 47 але менше 99"
word_list = srtoka.split()
num_list = []
 
for word in word_list:
    if word.isnumeric():
        num_list.append(int(word))
 
print(sum(num_list))