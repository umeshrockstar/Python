# A list contains names of boys and girls as its elements.Boys name are stored as tuples.Wap to find out number of boys and girls in a list
tpl =['sita','geeta','rita',('ram','hari','vishnu')]
boys_count = 0
girls_count = 0

for item in tpl:
    if isinstance(item, tuple):  # If the item is a tuple, it contains girls' names
        girls_count += len(item)
    else:
        boys_count += 1

print(f"Number of boys: {boys_count}")
print(f"Number of girls: {girls_count}")
