from lexer import Lex

m = Lex()
m.build()
#sample data
nm = str(input("Enter filname: "))
f = open(nm,'r')
data = str(f.readlines())
f.close()
#doing this because its just easeir
data = data[2:-2]
data = data.replace(" ", "")
m.run(data)