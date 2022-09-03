data = ["Adam", 
"Michel",  
"antonio"
]
first = str(data[0]).upper()
second = str(data[1]).upper()
thirdth = str(data[2]).upper()

new_data = []

if first.startswith("A"):
    new_data.append(first)

if second.startswith("A"):
    new_data.append(second)

if thirdth.startswith("A"):
    new_data.append(thirdth)

print (new_data)