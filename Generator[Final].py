import random
from itertools import permutations

# Default list of characters
alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
cap   = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","S","T","U","V","W","X","X","Y","Z"]
numb  = [1,2,3,4,5,6,7,8,9,0]
spec  = [" ","!",'"',"#","$","%","&","'","(",")","*","+",",","-",".","/",":",";","<","=",">","?","@","[","\\","]","^","_","`","{","|","}","~"]

# Default Character length
count_alpha = count_numb = count_cap = count_spec = 4


def main_menu():
    menu = ""

    while menu not in [1, 2, 3, 4]:                                                                      
        menu = input('''******Password Generator*****\n
        1. Default (16 letters)
        2. Advance
        3. Custom Words
        4. Load Settings
        >> ''')
        if menu.isnumeric() == False:
            continue
        menu = int(menu)
        
    if menu == 1:
        print_password(count_alpha, count_cap, count_numb, count_spec)
    elif menu == 2:
        advance_menu()
    elif menu == 3:
        custom_menu()
    elif menu == 4:
        load_menu()


def advance_menu():
    global alpha, cap, numb, spec, count_alpha, count_cap, count_numb, count_spec
    menu = ""

    print("\n******Password Generator(Advanced)*****\n\nDefault Values = 8 \n")

    count_alpha = count_numb = count_cap = count_spec = ""

    while count_alpha.isnumeric() == False:                                                         # For non integer inputs
        count_alpha = input("No. of lowercase alphabets to be included: ")                          # Inputtting number of alphabets
    
    while count_cap.isnumeric() == False:
        count_cap = input("No. of capital alphabet to be included: ")

    while count_numb.isnumeric() == False:
        count_numb = input("No. of number to be included: ")

    while count_spec.isnumeric() == False:
        count_spec = input("No. of special charatcers to be included: ")

    print("Letters:\n", *alpha, *cap, *numb, *spec )
    del_menu = input("\n\nDo you want to delete some specific letter(Y/N): ")                        # Deleting Specified letters

    while del_menu.casefold() == "y":

        del_char = input("Enter the character to be removed: ")

        if del_char in alpha:
            alpha.remove(del_char)
        
        elif del_char in cap:
            cap.remove(del_char)
        
        elif del_char in numb:
            numb.remove(int(del_char))
        
        elif del_char in spec:
            spec.remove(del_char)
        


        print("New Letters: \n", *alpha, *cap, *numb, *spec, "\n")

        del_menu = input("Do you want to delete more character (Y/N): ")

    while menu.casefold() not in ["y","n"]:
        menu = input("Do you want to save these settings for faster password generation in future [Y/N]: ")
    
    if menu.casefold() == "y":
        file_name = input("Enter file name: ")
        save_setting(file_name)

    print_password(count_alpha, count_cap, count_numb, count_spec)


def custom_menu():
    menu = ""

    print('''\n******Password Generator(Custom Words)*****
    (try to add atleast 5 words and also include some numbers for strong password)\n''')

    password = []

    while menu.casefold() != "n":
        menu = ""
        custom_word = input("Enter the custom word: ")
        password.append(custom_word)

        while menu.casefold() not in ["y","n"]:
            menu = input("You want to add more words(Y/N): ")
    
    complex_password = []
    for i in range(1, len(password)+1):
        complex_password = complex_password + list(permutations(password , i))
        
    menu = ""                                                                                 # Asking to print passwords to file
    while menu.casefold() not in ["y","n"]:
        menu = input("Do you want to print these on notepad [Y/N]? ")

    if menu.casefold() == "y":
        file_name = input("Enter name of file: ")

    print("\nPasswords: \n")

    for i in complex_password:
        new_pass = []
        for j in range(0,len(i)):
            new_pass.append(i[j])
        new_pass_str = make_str(new_pass)
        print(new_pass_str)
        if menu.casefold() == "y":
            print_file(new_pass_str, file_name)
        

    input("Press enter to exit...")
    exit()


def load_menu():

    file_name = input("Enter File name: ")

    load_setting(file_name)
    print_password(count_alpha, count_cap, count_numb, count_spec)


def print_password(count_alpha, count_cap, count_numb, count_spec):
    menu = ""

    count_pass = ""
    while count_pass.isnumeric() != True:
        count_pass = input("how many password you want to generate: ")

    print(f"\nPassword length is {int(count_alpha) + int(count_cap) + int(count_numb) + int(count_spec)}")

                                                                                # Asking to print passwords to file
    while menu.casefold() not in ["y","n"]:
        menu = input("Do you want to print these on notepad [Y/N]? ")

    if menu.casefold() == "y":
        file_name = input("Enter name of file: ")
    
    print("\nPassword List: ")

    for i in range(int(count_pass)):
        pass_alpha = [random.choice(alpha) for i in range(int(count_alpha))]
        pass_cap = [random.choice(cap) for i in range(int(count_cap))]
        pass_numb = [random.choice(numb) for i in range(int(count_numb))]
        pass_spec = [random.choice(spec) for i in range(int(count_spec))]

        password = pass_alpha + pass_numb + pass_cap + pass_spec                                              

        random.shuffle(password)    
                                                                                  
        password_str = make_str(password)
        
        print(password_str)

        if menu.casefold() == "y":                            # Printing to file
            print_file(password_str, file_name)

    input("Press enter to exit...")
    exit()
 
def print_file(password_str, file_name):
    file = open(f"{file_name}.txt", "a")
    file.write(f"{password_str}\n")
    file.close()


def make_str(password):
    password_str =""

    for i in password:
        password_str += str(i)
    
    return password_str
    

def load_setting(file_name):

    global alpha, cap, numb, spec, count_alpha, count_cap, count_numb, count_spec

    settings = open(f"{file_name}.txt")

    for i, line in enumerate(settings):
        if i == 0:
            alpha = list(line)
        elif i == 1:
            cap = list(line)
        elif i == 2:
            numb = list(line)
        elif i == 3:
            spec = list(line)
        elif i == 4:
            count_alpha = list(line)
        elif i == 5:
            count_cap = list(line)
        elif i == 6:
            count_numb = list(line)
        elif i == 7:
            count_spec = list(line)

    alpha.remove("\n")
    cap.remove("\n")
    numb.remove("\n")
    spec.remove("\n")
    count_alpha.remove("\n")
    count_cap.remove("\n")
    count_numb.remove("\n")
    count_spec.remove("\n")

    count_alpha = int(make_str(count_alpha))
    count_cap = int(make_str(count_cap))
    count_numb = int(make_str(count_numb))
    count_spec = int(make_str(count_spec))

    settings.close()


def save_setting(file_name):
    
    settings = open(f"{file_name}.txt", "a")
    
    settings.write(f"{make_str(alpha)}\n{make_str(cap)}\n{make_str(numb)}\n{make_str(spec)}\n{count_alpha}\n{count_cap}\n{count_numb}\n{count_spec}\n")

    settings.close()


main_menu()