nome = input("come ti chiami")
print("cioa", nome)
anni = input("quanti anni hai")
if anni >= 18:
	print("sei maggiorenne")
else:
	print("sei ancora piccolo")
viaggio = input("dove vuoi andare")
if viaggio == "londra" and anni <= 18:
	print("sorry cambia meta")
