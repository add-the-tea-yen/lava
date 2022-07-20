from lexer import Lex

m = Lex()
m.build()
#sample data
nm = str(input("Enter filname: "))
f = open(nm,'r')
data = str(f.readlines())
f.close()
data = data[2:-2]
data = data.replace(" ", "")
print(data)
m.run(data)