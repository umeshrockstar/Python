lst=['madam','python',"malayalam",12341]

lst1=filter(lambda x: str(x)==str(x)[::-1],lst)

print(list(lst1))