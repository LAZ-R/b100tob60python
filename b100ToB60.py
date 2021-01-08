syke = "i"
print("\nB-100 to B-60\n")
while syke != "x":
    def isInputOk(message, errorMessage):
        while True:
            try:
                a = float(input(message))
                b = str(a).split(".")
                return b
            except:
                pass
            message = errorMessage
    durée = (isInputOk('Durée à convertir ? Base 100, au format 8.5 , 17.77\n',
                       "Merci de n'entrer que les caractères autorisés, au format 8.5 , 17.77\n"))
    heures = int(durée[0])
    minutes100 = str(durée[1])
    if len(minutes100) == 1:
        minutes100 = int(minutes100)
        minutes100 = minutes100*10
    else:
        minutes100 = int(minutes100)
    minutes60 = int((minutes100/100)*60)
    print("\n", heures, "h", minutes60, "min")
    syke = input("\nNouvelle conversion : Entrée.\nQuitter : x\n")
