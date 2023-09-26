mot = input("Entrez la première phrase/ le premier mot : ")

mot_1 = mot.lower().strip()

mot_1 = mot_1.replace(" ", "")

mot_2 = mot_1[::-1]
if mot_1 == mot_2:
    print("'{}' est un palindrome".format(mot))
else:
    print("'{}' n'est pas un palindrome".format(mot))
