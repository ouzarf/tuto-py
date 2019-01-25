def dire_message(nom,message):
    print("{}:{}".format(nom,message))
    
dire_message("mohamed"," bonjour comment vas-tu?")
dire_message ("yassine"," ca va merci")

def redire_message(nom="ali",age=50,message="    bnj"):
    print("{} a ({}):{}".format(nom,age,message))
    
redire_message("mohamed",25,"    bonjour comment vas-tu?")
redire_message(age=40, message="   Re- bonjour comment vas-tu?")

def affiche_list(*ma_list):
    for elements in ma_list:
        print(elements)
    
affiche_list("mohamed","bonjour comment vas-tu?",28 , "FES", "Morocco")

def aurevoir():
	print("au revoir :)")