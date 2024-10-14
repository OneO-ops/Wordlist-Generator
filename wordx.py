print("Welcome to Wordlist Generator")
print("Python Wordlist Generator created without librarys")
while True:
    try:
        print("")
        Parameter_counter = int(input("How many parameters to enter? (1, 2 ): "))
        if 1 <= Parameter_counter <= 2:
            # 3,4
            break
        else:
            print("Enter a valid number.")
    except ValueError:
        print("Please enter a valid integer.")
Parameter1_length = 0
Parameter2_length = 0
Parameter3_length = 0
Parameter4_length = 0
Parameter1 = "o"
Parameter2 = "n"
Parameter3 = "e"
Parameter4 = "o"
print("")
while True:
    print("Enter Parameter/Parameters")
    if Parameter_counter == 1:
        Parameter1 = input("First Parameter:")
        for i1 in Parameter1:
            Parameter1_length = Parameter1_length + 1
        if Parameter1_length <=0 :
            print("Enter a valid parameter.")
        else :
            break
    elif Parameter_counter == 2:
        Parameter1 = input("First Parameter:")
        print("")
        Parameter2 = input("Second Parameter:")
        for i1 in Parameter1:
            Parameter1_length = Parameter1_length + 1

        for i2 in Parameter2:
            Parameter2_length = Parameter2_length + 1
        if Parameter1_length <=0 and Parameter2_length <= 0 :
            print("Enter a valid parameter.")
        else:
            break
    elif Parameter_counter == 3:
        Parameter1 = input("First Parameter:")
        print("")
        Parameter2 = input("Second Parameter:")
        print("")
        Parameter3 = input("Third Parameter:")
        for i1 in Parameter1:
            Parameter1_length = Parameter1_length + 1

        for i2 in Parameter2:
            Parameter2_length = Parameter2_length + 1

        for i3 in Parameter3:
            Parameter3_length = Parameter3_length + 1
        if Parameter1_length<=0 and Parameter2_length<=0 and Parameter3_length<=0:
            print("Enter a valid parameter.")
        else:
            break
    elif Parameter_counter == 4:
        Parameter1 = input("First Parameter:")
        print("")
        Parameter2 = input("Second Parameter:")
        print("")
        Parameter3 = input("Third Parameter:")
        print("")
        Parameter4 = input("Fourth Parameter:")
        for i1 in Parameter1:
            Parameter1_length = Parameter1_length + 1
        for i2 in Parameter2:
            Parameter2_length = Parameter2_length + 1
        for i3 in Parameter3:
            Parameter3_length = Parameter3_length + 1
        for i4 in Parameter4:
            Parameter4_length = Parameter4_length + 1
        if Parameter1_length <=0 and Parameter2_length<=0 and Parameter3_length<=0 and Parameter4_length<=0:
                print("Enter a valid parameter.")
        else:
            break
    else:
        print("Enter a valid parameter.")
print("")
while True:
    Passwd_long = int(input("How many digits should the password be?(6,7,8,9) :"))
    if Parameter_counter == 1:
        add1 = Passwd_long - Parameter1_length
        if 0<=add1<=9 :
            if 6<=Passwd_long<=9:
                break
            else:
                print("")
                print("Enter a valid number.")
                print("")     
        else:
            print("")
            print("Enter a valid number.")
            print("")
    elif Parameter_counter == 2:
        add1 = Passwd_long - Parameter1_length
        add2 = Passwd_long - Parameter2_length
        add3 = Passwd_long - Parameter1_length - Parameter2_length
        if 0<=add1 and 0<=add2 or 0<=add3 :
            if 6<=Passwd_long<=9:
                break
            else:
                print("")
                print("Enter a valid number.")
                print("")
        else:
            print("")
            print("Enter a valid number.")
            print("")
    elif Parameter_counter == 3:
        add1 = Passwd_long - Parameter1_length
        add2 = Passwd_long - Parameter2_length
        add3 = Passwd_long - Parameter1_length - Parameter2_length
        add4 = Passwd_long - Parameter3_length
        add5 = Passwd_long - Parameter1_length - Parameter3_length
        add6 = Passwd_long - Parameter2_length - Parameter3_length
        add7 = Passwd_long - Parameter2_length - Parameter3_length - Parameter1_length
        if 0<=add1 and 0<=add2 and 0<=add4 or 0<=add3 and 0<=add5 and 0<=add6 or 0<=add7 :
            if 6<=Passwd_long<=9:
                break
            else:
                print("")
                print("Enter a valid number.")
                print("")
        else:
            print("")
            print("Enter a valid number.")
            print("")
    elif Parameter_counter == 4:
        add1 = Passwd_long - Parameter1_length
        add2 = Passwd_long - Parameter2_length
        add3 = Passwd_long - Parameter1_length - Parameter2_length
        add4 = Passwd_long - Parameter3_length
        add5 = Passwd_long - Parameter1_length - Parameter3_length
        add6 = Passwd_long - Parameter2_length - Parameter3_length
        add7 = Passwd_long - Parameter2_length - Parameter3_length - Parameter1_length
        add8 = Passwd_long - Parameter4_length
        add9 = Passwd_long - Parameter1_length - Parameter4_length
        add10 = Passwd_long - Parameter3_length - Parameter4_length
        add11 = Passwd_long - Parameter2_length - Parameter4_length
        add12 = Passwd_long - Parameter2_length - Parameter3_length - Parameter4_length
        add13 = Passwd_long - Parameter3_length - Parameter4_length - Parameter1_length
        add14 = Passwd_long - Parameter4_length - Parameter1_length - Parameter2_length
        add15 = Passwd_long - Parameter1_length - Parameter2_length - Parameter3_length - Parameter4_length
        if 0<=add1 and 0<=add2 and 0<=add4 and 0<=add8 or 0<=add3 and 0<=add5 and 0<=add6 and 0<=add9 and 0<=add10 and 0<=add11 or 0<=add7 and 0<=add12 and 0<=add13 and 0<=add14 or 0<=add15 :
            if 6<=Passwd_long<=9:
                break
            else:
                print("")
                print("Enter a valid number.")
                print("")
        else:
            print("")
            print("Enter a valid number.")
            print("")
    else:
        print("")
        print("Enter a valid number.")
        print("")

l1 = [1,2,3,4,5,6,7,8,9,0]
l2 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","w","x","y","z"]
l3 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","T","U","V","W","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","w","x","y","z"]
l4 = [1,2,3,4,5,6,7,8,9,0,"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","w","x","y","z"]
l5 = [1,2,3,4,5,6,7,8,9,0,"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","T","U","V","W","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","w","x","y","z"]
l6 = ["a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","w","x","y","z"]
l7 = ["A","B","C","Ç","D","E","F","G","Ğ","H","I","İ","J","K","L","M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","W","Y","Z","a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","w","x","y","z"]
l8 = [1,2,3,4,5,6,7,8,9,0,"a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","w","x","y","z"]
l9 = [1,2,3,4,5,6,7,8,9,0,"A","B","C","Ç","D","E","F","G","Ğ","H","I","İ","J","K","L","M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","W","Y","Z","a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","w","x","y","z"]
# l10

print("")
print("1 = 1,2,3,4,5..")
print("2 = a,b,c,..")
print("3 = A,B,..,a,b,c,..")
print("4 = 1,2,3,..,a,b,..")
print("5 = 1,2,3,..,A,B,..,a,b,c,..")
print("6 = a,b,c,ç,..(Turk)")
print("7 = A,B,C,Ç,..,a,b,..(Turk)")
print("8 = 1,2,3,..,a,b,c,ç,..(Turk)")
print("9 = 1,2,3,..,A,B,C,Ç,..,a,b,..(Turk)"),
print("10 = list with selected characters")

print("")
while True:
    selected_list = int(input("Select a list: "))
    if selected_list == 1 :
        selected_list = l1
        print('\n' + "list1 selected")
        break
    elif selected_list == 2 :
        selected_list = l2
        print('\n' + "list2 selected")
        break
    elif selected_list == 3 :
        selected_list = l3
        print('\n' + "list3 selected")
        break
    elif selected_list == 4 :
        selected_list = l4
        print('\n' + "list4 selected")
        break
    elif selected_list == 5 :
        selected_list = l5
        print('\n' + "list5 selected")
        break
    elif selected_list == 6 :
        selected_list = l6
        print('\n' +"list6 selected")
        break
    elif selected_list == 7 :
        selected_list = l7
        print('\n' + "list7 selected")
        break
    elif selected_list == 8 :
        selected_list = l8
        print('\n' + "list8 selected")
        break
    elif selected_list == 9 :
        selected_list = l9
        print('\n' + "list9 selected")
        break
    elif selected_list == 10:
        oneo = input("Type characters(aBçd._?8@4) :")
        l10 = list(oneo)
        selected_list = l10
        print('\n' + "Selected list: " + str(l10) + '\n')
        break
    else:
        print('\n' + "Enter a valid parameter (1,2,3,...,9)")

while True:
    lowercap = input("Lower parameters and capitalized parameters? (Y/N) :")
    lowercap = lowercap.lower()
    if lowercap == "y" or lowercap == "yes":
        Parameter1 = Parameter1.lower()
        Parameter2 = Parameter2.lower()
        Parameter3 = Parameter3.lower()
        Parameter4 = Parameter4.lower()
        lowercap = 1
        break
    elif lowercap == "n" or lowercap == "no":
        lowercap = 0
        break
    else:
        print("Enter a valid parameter.")
#multiparameter(mpar)
mpar = 0

filename = input("Enter the desired output filename: ")

selected_list_long = 0

for list_counter in selected_list:
    selected_list_long = selected_list_long + 1


byte1 = selected_list_long + 1

if Parameter_counter == 1:
    for count in range(0,add1-1):
        byte1 = byte1*selected_list_long

elif Parameter_counter == 2:
    if mpar == 0 :
        for count in range(0,add3-1):
            byte1 = byte1*selected_list_long
    elif mpar == 1:
        print("not now")

byte2 = byte1 * (Passwd_long + 1)

if Parameter_counter == 1:
    if lowercap == 0:
        if add1 == 0:
            byte = byte2 * 1
        elif add1 == 1:
            byte = byte2 * 2
        elif add1 == 2:
            byte = byte2 * 3
        elif add1 == 3:
            byte = byte2 * 4
        elif add1 == 4 :
            byte = byte2 * 5
        elif add1 == 5 :
            byte = byte2 * 6
        elif add1 == 6 :
            byte = byte2 * 7
        elif add1 == 7 :
            byte = byte2 * 8
        elif add1 == 8 :
            byte = byte2 * 9
    elif lowercap == 1:
        if add1 == 0:
            byte = byte2 * 2
        elif add1 == 1:
            byte = byte2 * 4
        elif add1 == 2:
            byte = byte2 * 6
        elif add1 == 3:
            byte = byte2 * 8
        elif add1 == 4 :
            byte = byte2 * 10
        elif add1 == 5 :
            byte = byte2 * 12
        elif add1 == 6 :
            byte = byte2 * 14
        elif add1 == 7 :
            byte = byte2 * 16
        elif add1 == 8 :
            byte = byte2 * 18
elif Parameter_counter == 2 :
    if lowercap == 0:
        if add3 == 0:
            byte = byte2 * 2
        elif add3 == 1:
            byte = byte2 * 6
        elif add3 == 2 :
            byte = byte2 * 12 
        elif add3 == 3 :
            byte = byte2 * 20
        elif add3 == 4 :
            byte = byte2 * 30
        elif add3 == 5 :
            byte = byte2 * 42
        elif add3 == 6 :
            byte = byte2 * 56
        elif add3 == 7 :
            byte = byte2 * 72
    elif lowercap == 1:
        if add3 == 0:
            byte = byte2 * 4
        elif add3 == 1:
            byte = byte2 * 12
        elif add3 == 2 :
            byte = byte2 * 24
        elif add3 == 3 :
            byte = byte2 * 40
        elif add3 == 4 :
            byte = byte2 * 60
        elif add3 == 5 :
            byte = byte2 * 84
        elif add3 == 6 :
            byte = byte2 * 112
        elif add3 == 7 :
            byte = byte2 * 144
mb = byte / 1000000
gb = mb / 1000
while True:
    print("Approximately " + str(mb) + "MB")
    print("Approximately " + str(gb) + "GB")
    areyouok = input("Do you want to continue?(Y/N): ")
    areyouok = areyouok.lower()
    if areyouok == "y" or areyouok == "yes":
        ok = 1
        break
    elif areyouok == "n"or areyouok == "no":
        ok = 0
        break
    else:
        print("Enter a valid parameter.")
if Parameter_counter == 1 and  ok==1 :
    if add1 == 0:
        print("why ?")
    elif add1 == 1:
        if lowercap == 0:
            for j1 in selected_list:
                with open(filename + ".txt", 'a') as f:
                    passwords1 = f"{Parameter1}{j1}"
                    passwords2 = f"{j1}{Parameter1}"  
                    print(passwords1 + '\n'+ passwords2 + '\n')
                    f.write(passwords1 + '\n'+ passwords2 + '\n')
        elif lowercap == 1:
            for j1 in selected_list:
                with open(filename + ".txt", 'a') as f:
                    passwords1 = f"{Parameter1}{j1}"
                    passwords2 = f"{j1}{Parameter1}"
                    passwords3 = f"{Parameter1.capitalize()}{j1}"
                    passwords4 = f"{j1}{Parameter1.capitalize()}"       
                    print(passwords1 + '\n'+ passwords2 + '\n' + passwords3 + '\n'+ passwords4 + '\n')
                    f.write(passwords1 + '\n'+ passwords2 + '\n' + passwords3 + '\n'+ passwords4 + '\n')
    elif add1 == 2:
        if lowercap == 0:
            for j1 in selected_list:
                for j2 in selected_list:
                    with open(filename + ".txt", 'a') as f:
                        passwords1 = f"{Parameter1}{j1}{j2}"
                        passwords2 = f"{j1}{j2}{Parameter1}"
                        passwords3 = f"{j1}{Parameter1}{j2}"
                        print(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n')
                        f.write(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n')
        elif lowercap == 1:
            for j1 in selected_list:
                for j2 in selected_list:
                    with open(filename + ".txt", 'a') as f:
                        passwords1 = f"{Parameter1}{j1}{j2}"
                        passwords2 = f"{j1}{j2}{Parameter1}"
                        passwords3 = f"{j1}{Parameter1}{j2}"
                        passwords4 = f"{Parameter1.capitalize()}{j1}{j2}"
                        passwords5 = f"{j1}{j2}{Parameter1.capitalize()}"
                        passwords6 = f"{j1}{Parameter1.capitalize()}{j2}"
                        print(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' + passwords4 + '\n'+ passwords5 + '\n'+ passwords6 + '\n')
                        f.write(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' + passwords4 + '\n'+ passwords5 + '\n'+ passwords6 + '\n')
    elif add1 == 3:
        if lowercap == 0:
            for j1 in selected_list:
                for j2 in selected_list:
                    for j3 in selected_list:
                        with open(filename + ".txt", 'a') as f:
                            passwords1 = f"{Parameter1}{j1}{j2}{j3}"
                            passwords2 = f"{j1}{j2}{j3}{Parameter1}"
                            passwords3 = f"{j1}{j2}{Parameter1}{j3}"
                            passwords4 = f"{j1}{Parameter1}{j2}{j3}"
                            print(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' +passwords4 + '\n')
                            f.write(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n'+passwords4 + '\n')
        elif lowercap == 1:
            for j1 in selected_list:
                for j2 in selected_list:
                    for j3 in selected_list:
                        with open(filename + ".txt", 'a') as f:
                            passwords1 = f"{Parameter1}{j1}{j2}{j3}"
                            passwords2 = f"{j1}{j2}{j3}{Parameter1}"
                            passwords3 = f"{j1}{j2}{Parameter1}{j3}"
                            passwords4 = f"{j1}{Parameter1}{j2}{j3}"
                            passwords5 = f"{Parameter1.capitalize()}{j1}{j2}{j3}"
                            passwords6 = f"{j1}{j2}{j3}{Parameter1.capitalize()}"
                            passwords7 = f"{j1}{j2}{Parameter1.capitalize()}{j3}"
                            passwords8 = f"{j1}{Parameter1.capitalize()}{j2}{j3}"
                            print(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' +passwords4 + '\n' + passwords5 + '\n'+ passwords6 + '\n'+ passwords7 + '\n' +passwords8 + '\n')
                            f.write(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' +passwords4 + '\n' + passwords5 + '\n'+ passwords6 + '\n'+ passwords7 + '\n' +passwords8 + '\n')
    elif add1 == 4:
        if lowercap == 0:
            for j1 in selected_list:
                for j2 in selected_list:
                    for j3 in selected_list:
                        for j4 in selected_list:
                            with open(filename + ".txt", 'a') as f:
                                passwords1 = f"{Parameter1}{j1}{j2}{j3}{j4}"
                                passwords2 = f"{j1}{j2}{j3}{j4}{Parameter1}"
                                passwords3 = f"{j1}{j2}{j3}{Parameter1}{j4}"
                                passwords4 = f"{j1}{Parameter1}{j2}{j3}{j4}"
                                passwords5 = f"{j1}{j2}{Parameter1}{j3}{j4}"
                                print(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' +passwords4 + '\n' + passwords5 + '\n')
                                f.write(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n'+passwords4 + '\n' + passwords5 + '\n')
        elif lowercap == 1:
            for j1 in selected_list:
                for j2 in selected_list:
                    for j3 in selected_list:
                        for j4 in selected_list:
                            with open(filename + ".txt", 'a') as f:
                                passwords1 = f"{Parameter1}{j1}{j2}{j3}{j4}"
                                passwords2 = f"{j1}{j2}{j3}{j4}{Parameter1}"
                                passwords3 = f"{j1}{j2}{j3}{Parameter1}{j4}"
                                passwords4 = f"{j1}{Parameter1}{j2}{j3}{j4}"
                                passwords5 = f"{j1}{j2}{Parameter1}{j3}{j4}"
                                passwords6 = f"{Parameter1.capitalize()}{j1}{j2}{j3}{j4}"
                                passwords7 = f"{j1}{j2}{j3}{j4}{Parameter1.capitalize()}"
                                passwords8 = f"{j1}{j2}{j3}{Parameter1.capitalize()}{j4}"
                                passwords9 = f"{j1}{Parameter1.capitalize()}{j2}{j3}{j4}"
                                passwords10 = f"{j1}{j2}{Parameter1.capitalize()}{j3}{j4}"
                                print(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' +passwords4 + '\n' + passwords5 + '\n' + passwords6 + '\n'+ passwords7 + '\n'+ passwords8 + '\n' +passwords9 + '\n' + passwords10 + '\n')
                                f.write(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' +passwords4 + '\n' + passwords5 + '\n' + passwords6 + '\n'+ passwords7 + '\n'+ passwords8 + '\n' +passwords9 + '\n' + passwords10 + '\n')            
    elif add1 == 5:
        if lowercap == 0:
            for j1 in selected_list:
                for j2 in selected_list:
                    for j3 in selected_list:
                        for j4 in selected_list:
                            for j5 in selected_list:
                                with open(filename + ".txt", 'a') as f:
                                    passwords1 = f"{Parameter1}{j1}{j2}{j3}{j4}{j5}"
                                    passwords2 = f"{j1}{j2}{j3}{j4}{j5}{Parameter1}"
                                    passwords3 = f"{j1}{j2}{j3}{j4}{Parameter1}{j5}"
                                    passwords4 = f"{j1}{Parameter1}{j2}{j3}{j4}{j5}"
                                    passwords5 = f"{j1}{j2}{j3}{Parameter1}{j4}{j5}"
                                    passwords6 = f"{j1}{j2}{Parameter1}{j3}{j4}{j5}"
                                    print(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' +passwords4 + '\n' + passwords5 + '\n' + passwords6 + '\n')
                                    f.write(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n'+passwords4 + '\n' + passwords5 + '\n' + passwords6 + '\n')
        elif lowercap == 1:
            for j1 in selected_list:
                for j2 in selected_list:
                    for j3 in selected_list:
                        for j4 in selected_list:
                            for j5 in selected_list:
                                with open(filename + ".txt", 'a') as f:
                                    passwords1 = f"{Parameter1}{j1}{j2}{j3}{j4}{j5}"
                                    passwords2 = f"{j1}{j2}{j3}{j4}{j5}{Parameter1}"
                                    passwords3 = f"{j1}{j2}{j3}{j4}{Parameter1}{j5}"
                                    passwords4 = f"{j1}{Parameter1}{j2}{j3}{j4}{j5}"
                                    passwords5 = f"{j1}{j2}{j3}{Parameter1}{j4}{j5}"
                                    passwords6 = f"{j1}{j2}{Parameter1}{j3}{j4}{j5}"
                                    passwords7 = f"{Parameter1.capitalize()}{j1}{j2}{j3}{j4}{j5}"
                                    passwords8 = f"{j1}{j2}{j3}{j4}{j5}{Parameter1.capitalize()}"
                                    passwords9 = f"{j1}{j2}{j3}{j4}{Parameter1.capitalize()}{j5}"
                                    passwords10 = f"{j1}{Parameter1.capitalize()}{j2}{j3}{j4}{j5}"
                                    passwords11 = f"{j1}{j2}{j3}{Parameter1.capitalize()}{j4}{j5}"
                                    passwords12 = f"{j1}{j2}{Parameter1.capitalize()}{j3}{j4}{j5}"                            
                                    print(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' +passwords4 + '\n' + passwords5 + '\n' + passwords6 + '\n' + passwords7 + '\n'+ passwords8 + '\n'+ passwords9 + '\n' +passwords10 + '\n' + passwords11 + '\n' + passwords12 + '\n')
                                    f.write(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' +passwords4 + '\n' + passwords5 + '\n' + passwords6 + '\n' + passwords7 + '\n'+ passwords8 + '\n'+ passwords9 + '\n' +passwords10 + '\n' + passwords11 + '\n' + passwords12 + '\n')           

    elif add1 == 6:
        if lowercap == 0:
            for j1 in selected_list:
                for j2 in selected_list:
                    for j3 in selected_list:
                        for j4 in selected_list:
                            for j5 in selected_list:
                                for j6 in selected_list:
                                    with open(filename + ".txt", 'a') as f:
                                        passwords1 = f"{Parameter1}{j1}{j2}{j3}{j4}{j5}{j6}"
                                        passwords2 = f"{j1}{j2}{j3}{j4}{j5}{j6}{Parameter1}"
                                        passwords3 = f"{j1}{j2}{j3}{j4}{j5}{Parameter1}{j6}"
                                        passwords4 = f"{j1}{Parameter1}{j2}{j3}{j4}{j5}{j6}"
                                        passwords5 = f"{j1}{j2}{j3}{j4}{Parameter1}{j5}{j6}"
                                        passwords6 = f"{j1}{j2}{Parameter1}{j3}{j4}{j5}{j6}"
                                        passwords7 = f"{j1}{j2}{j3}{Parameter1}{j4}{j5}{j6}"
                                        print(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' +passwords4 + '\n' + passwords5 + '\n' + passwords6 + '\n' + passwords7 + '\n' )
                                        f.write(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n'+passwords4 + '\n' + passwords5 + '\n' + passwords6 + '\n' + passwords7 + '\n' )
        elif lowercap == 1:
            for j1 in selected_list:
                for j2 in selected_list:
                    for j3 in selected_list:
                        for j4 in selected_list:
                            for j5 in selected_list:
                                for j6 in selected_list:
                                    with open(filename + ".txt", 'a') as f:
                                        passwords1 = f"{Parameter1}{j1}{j2}{j3}{j4}{j5}{j6}"
                                        passwords2 = f"{j1}{j2}{j3}{j4}{j5}{j6}{Parameter1}"
                                        passwords3 = f"{j1}{j2}{j3}{j4}{j5}{Parameter1}{j6}"
                                        passwords4 = f"{j1}{Parameter1}{j2}{j3}{j4}{j5}{j6}"
                                        passwords5 = f"{j1}{j2}{j3}{j4}{Parameter1}{j5}{j6}"
                                        passwords6 = f"{j1}{j2}{Parameter1}{j3}{j4}{j5}{j6}"
                                        passwords7 = f"{j1}{j2}{j3}{Parameter1}{j4}{j5}{j6}"
                                        passwords8 = f"{Parameter1.capitalize()}{j1}{j2}{j3}{j4}{j5}{j6}"
                                        passwords9 = f"{j1}{j2}{j3}{j4}{j5}{j6}{Parameter1.capitalize()}"
                                        passwords10 = f"{j1}{j2}{j3}{j4}{j5}{Parameter1.capitalize()}{j6}"
                                        passwords11 = f"{j1}{Parameter1.capitalize()}{j2}{j3}{j4}{j5}{j6}"
                                        passwords12 = f"{j1}{j2}{j3}{j4}{Parameter1.capitalize()}{j5}{j6}"
                                        passwords13 = f"{j1}{j2}{Parameter1.capitalize()}{j3}{j4}{j5}{j6}"
                                        passwords14 = f"{j1}{j2}{j3}{Parameter1.capitalize()}{j4}{j5}{j6}"                                        
                                        print(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' +passwords4 + '\n' + passwords5 + '\n' + passwords6 + '\n' + passwords7 + '\n' + passwords8 + '\n'+ passwords9 + '\n'+ passwords10 + '\n' +passwords11 + '\n' + passwords12 + '\n' + passwords13 + '\n' + passwords14 + '\n' )
                                        f.write(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' +passwords4 + '\n' + passwords5 + '\n' + passwords6 + '\n' + passwords7 + '\n' + passwords8 + '\n'+ passwords9 + '\n'+ passwords10 + '\n' +passwords11 + '\n' + passwords12 + '\n' + passwords13 + '\n' + passwords14 + '\n' )

    elif add1 == 7:
        if lowercap == 0:
            for j1 in selected_list:         
                for j2 in selected_list:
                    for j3 in selected_list:
                        for j4 in selected_list:
                            for j5 in selected_list:
                                for j6 in selected_list:
                                    for j7 in selected_list:
                                        with open(filename + ".txt", 'a') as f:
                                            passwords1 = f"{Parameter1}{j1}{j2}{j3}{j4}{j5}{j6}{j7}"
                                            passwords2 = f"{j1}{j2}{j3}{j4}{j5}{j6}{j7}{Parameter1}"
                                            passwords3 = f"{j1}{j2}{j3}{j4}{j5}{j6}{Parameter1}{j7}"
                                            passwords4 = f"{j1}{Parameter1}{j2}{j3}{j4}{j5}{j6}{j7}"
                                            passwords5 = f"{j1}{j2}{j3}{j4}{j5}{Parameter1}{j6}{j7}"
                                            passwords6 = f"{j1}{j2}{Parameter1}{j3}{j4}{j5}{j6}{j7}"
                                            passwords7 = f"{j1}{j2}{j3}{Parameter1}{j4}{j5}{j6}{j7}"
                                            passwords8 = f"{j1}{j2}{j3}{j4}{Parameter1}{j5}{j6}{j7}"
                                            print(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' +passwords4 + '\n' + passwords5 + '\n' + passwords6 + '\n' + passwords7 + '\n' + passwords8 + '\n' )
                                            f.write(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n'+passwords4 + '\n' + passwords5 + '\n' + passwords6 + '\n' + passwords7 + '\n' + passwords8 + '\n' )
        elif lowercap == 1:
            for j1 in selected_list:         
                for j2 in selected_list:
                    for j3 in selected_list:
                        for j4 in selected_list:
                            for j5 in selected_list:
                                for j6 in selected_list:
                                    for j7 in selected_list:
                                        with open(filename + ".txt", 'a') as f:
                                            passwords1 = f"{Parameter1}{j1}{j2}{j3}{j4}{j5}{j6}{j7}"
                                            passwords2 = f"{j1}{j2}{j3}{j4}{j5}{j6}{j7}{Parameter1}"
                                            passwords3 = f"{j1}{j2}{j3}{j4}{j5}{j6}{Parameter1}{j7}"
                                            passwords4 = f"{j1}{Parameter1}{j2}{j3}{j4}{j5}{j6}{j7}"
                                            passwords5 = f"{j1}{j2}{j3}{j4}{j5}{Parameter1}{j6}{j7}"
                                            passwords6 = f"{j1}{j2}{Parameter1}{j3}{j4}{j5}{j6}{j7}"
                                            passwords7 = f"{j1}{j2}{j3}{Parameter1}{j4}{j5}{j6}{j7}"
                                            passwords8 = f"{j1}{j2}{j3}{j4}{Parameter1}{j5}{j6}{j7}"
                                            passwords9 = f"{Parameter1.capitalize()}{j1}{j2}{j3}{j4}{j5}{j6}{j7}"
                                            passwords10 = f"{j1}{j2}{j3}{j4}{j5}{j6}{j7}{Parameter1.capitalize()}"
                                            passwords11 = f"{j1}{j2}{j3}{j4}{j5}{j6}{Parameter1.capitalize()}{j7}"
                                            passwords12 = f"{j1}{Parameter1.capitalize()}{j2}{j3}{j4}{j5}{j6}{j7}"
                                            passwords13 = f"{j1}{j2}{j3}{j4}{j5}{Parameter1.capitalize()}{j6}{j7}"
                                            passwords14 = f"{j1}{j2}{Parameter1.capitalize()}{j3}{j4}{j5}{j6}{j7}"
                                            passwords15 = f"{j1}{j2}{j3}{Parameter1.capitalize()}{j4}{j5}{j6}{j7}"
                                            passwords16 = f"{j1}{j2}{j3}{j4}{Parameter1.capitalize()}{j5}{j6}{j7}"                                            
                                            print(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' +passwords4 + '\n' + passwords5 + '\n' + passwords6 + '\n' + passwords7 + '\n' + passwords8 + '\n' + passwords9 + '\n'+ passwords10 + '\n'+ passwords11 + '\n' +passwords12 + '\n' + passwords13 + '\n' + passwords14 + '\n' + passwords15 + '\n' + passwords16 + '\n' )
                                            f.write(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' +passwords4 + '\n' + passwords5 + '\n' + passwords6 + '\n' + passwords7 + '\n' + passwords8 + '\n' + passwords9 + '\n'+ passwords10 + '\n'+ passwords11 + '\n' +passwords12 + '\n' + passwords13 + '\n' + passwords14 + '\n' + passwords15 + '\n' + passwords16 + '\n' )

    elif add1 == 8:
        if lowercap == 0:
            for j1 in selected_list:
                for j2 in selected_list:
                    for j3 in selected_list:
                        for j4 in selected_list:
                            for j5 in selected_list:
                                for j6 in selected_list:
                                    for j7 in selected_list:
                                        for j8 in selected_list:
                                            with open(filename + ".txt", 'a') as f:
                                                passwords1 = f"{Parameter1}{j1}{j2}{j3}{j4}{j5}{j6}{j7}{j8}"
                                                passwords2 = f"{j1}{j2}{j3}{j4}{j5}{j6}{j7}{j8}{Parameter1}"
                                                passwords3 = f"{j1}{j2}{j3}{j4}{j5}{j6}{j7}{Parameter1}{j8}"
                                                passwords4 = f"{j1}{Parameter1}{j2}{j3}{j4}{j5}{j6}{j7}{j8}"
                                                passwords5 = f"{j1}{j2}{j3}{j4}{j5}{j6}{Parameter1}{j7}{j8}"
                                                passwords6 = f"{j1}{j2}{Parameter1}{j3}{j4}{j5}{j6}{j7}{j8}"
                                                passwords7 = f"{j1}{j2}{j3}{Parameter1}{j4}{j5}{j6}{j7}{j8}"
                                                passwords8 = f"{j1}{j2}{j3}{j4}{j5}{Parameter1}{j6}{j7}{j8}"
                                                passwords9 = f"{j1}{j2}{j3}{j4}{Parameter1}{j5}{j6}{j7}{j8}"
                                                print(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' +passwords4 + '\n' + passwords5 + '\n' + passwords6 + '\n' + passwords7 + '\n' + passwords8 + '\n' + passwords9 + '\n' )
                                                f.write(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n'+passwords4 + '\n' + passwords5 + '\n' + passwords6 + '\n' + passwords7 + '\n' + passwords8 + '\n' + passwords9 + '\n' )
        elif lowercap == 1:
            for j1 in selected_list:
                for j2 in selected_list:
                    for j3 in selected_list:
                        for j4 in selected_list:
                            for j5 in selected_list:
                                for j6 in selected_list:
                                    for j7 in selected_list:
                                        for j8 in selected_list:
                                            with open(filename + ".txt", 'a') as f:
                                                passwords1 = f"{Parameter1}{j1}{j2}{j3}{j4}{j5}{j6}{j7}{j8}"
                                                passwords2 = f"{j1}{j2}{j3}{j4}{j5}{j6}{j7}{j8}{Parameter1}"
                                                passwords3 = f"{j1}{j2}{j3}{j4}{j5}{j6}{j7}{Parameter1}{j8}"
                                                passwords4 = f"{j1}{Parameter1}{j2}{j3}{j4}{j5}{j6}{j7}{j8}"
                                                passwords5 = f"{j1}{j2}{j3}{j4}{j5}{j6}{Parameter1}{j7}{j8}"
                                                passwords6 = f"{j1}{j2}{Parameter1}{j3}{j4}{j5}{j6}{j7}{j8}"
                                                passwords7 = f"{j1}{j2}{j3}{Parameter1}{j4}{j5}{j6}{j7}{j8}"
                                                passwords8 = f"{j1}{j2}{j3}{j4}{j5}{Parameter1}{j6}{j7}{j8}"
                                                passwords9 = f"{j1}{j2}{j3}{j4}{Parameter1}{j5}{j6}{j7}{j8}"
                                                passwords10 = f"{Parameter1.capitalize()}{j1}{j2}{j3}{j4}{j5}{j6}{j7}{j8}"
                                                passwords11 = f"{j1}{j2}{j3}{j4}{j5}{j6}{j7}{j8}{Parameter1.capitalize()}"
                                                passwords12 = f"{j1}{j2}{j3}{j4}{j5}{j6}{j7}{Parameter1.capitalize()}{j8}"
                                                passwords13 = f"{j1}{Parameter1.capitalize()}{j2}{j3}{j4}{j5}{j6}{j7}{j8}"
                                                passwords14 = f"{j1}{j2}{j3}{j4}{j5}{j6}{Parameter1.capitalize()}{j7}{j8}"
                                                passwords15 = f"{j1}{j2}{Parameter1.capitalize()}{j3}{j4}{j5}{j6}{j7}{j8}"
                                                passwords16 = f"{j1}{j2}{j3}{Parameter1.capitalize()}{j4}{j5}{j6}{j7}{j8}"
                                                passwords17 = f"{j1}{j2}{j3}{j4}{j5}{Parameter1.capitalize()}{j6}{j7}{j8}"
                                                passwords18 = f"{j1}{j2}{j3}{j4}{Parameter1.capitalize()}{j5}{j6}{j7}{j8}"                                                
                                                print(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' +passwords4 + '\n' + passwords5 + '\n' + passwords6 + '\n' + passwords7 + '\n' + passwords8 + '\n' + passwords9 + '\n' + passwords10 + '\n'+ passwords11 + '\n'+ passwords12 + '\n' +passwords13 + '\n' + passwords14 + '\n' + passwords15 + '\n' + passwords16 + '\n' + passwords17 + '\n' + passwords18 + '\n' )
                                                f.write(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' +passwords4 + '\n' + passwords5 + '\n' + passwords6 + '\n' + passwords7 + '\n' + passwords8 + '\n' + passwords9 + '\n' + passwords10 + '\n'+ passwords11 + '\n'+ passwords12 + '\n' +passwords13 + '\n' + passwords14 + '\n' + passwords15 + '\n' + passwords16 + '\n' + passwords17 + '\n' + passwords18 + '\n' )
##############################################################    
elif Parameter_counter == 2 and ok == 1:
    if add3 == 0 :
        print("why??")
        #I cant code anymore..
    elif add3 == 1 :
        if mpar == 0 :
            if lowercap == 0:
                for j1 in selected_list:
                    with open(filename + ".txt", 'a') as f:
                        passwords1 = f"{Parameter1}{Parameter2}{j1}"
                        passwords2 = f"{j1}{Parameter1}{Parameter2}"  
                        passwords3 = f"{Parameter1}{j1}{Parameter1}"  
                        passwords4 = f"{Parameter2}{Parameter1}{j1}"
                        passwords5 = f"{j1}{Parameter2}{Parameter1}"  
                        passwords6 = f"{Parameter2}{j1}{Parameter1}"                          
                        print(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' +passwords4 + '\n' + passwords5 + '\n' + passwords6 + '\n')
                        f.write(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' +passwords4 + '\n' + passwords5 + '\n' + passwords6 + '\n')
            elif lowercap == 1:
                for j1 in selected_list:
                    with open(filename + ".txt", 'a') as f:
                        passwords1 = f"{Parameter1}{Parameter2}{j1}"
                        passwords2 = f"{j1}{Parameter1}{Parameter2}"  
                        passwords3 = f"{Parameter1}{j1}{Parameter1}"  
                        passwords4 = f"{Parameter2}{Parameter1}{j1}"
                        passwords5 = f"{j1}{Parameter2}{Parameter1}"  
                        passwords6 = f"{Parameter2}{j1}{Parameter1}"          
                        passwords7 = f"{Parameter1.capitalize()}{Parameter2}{j1}"
                        passwords8 = f"{j1}{Parameter1.capitalize()}{Parameter2}"  
                        passwords9 = f"{Parameter1.capitalize()}{j1}{Parameter1}"  
                        passwords10 = f"{Parameter2.capitalize()}{Parameter1}{j1}"
                        passwords11 = f"{j1}{Parameter2.capitalize()}{Parameter1}"  
                        passwords12 = f"{Parameter2.capitalize()}{j1}{Parameter1}"                                            
                        print(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' +passwords4 + '\n' + passwords5 + '\n' + passwords6 + '\n' + passwords7 + '\n' + passwords8 + '\n' + passwords9 + '\n' + passwords10 + '\n'+ passwords11 + '\n'+ passwords12 + '\n')
                        f.write(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' +passwords4 + '\n' + passwords5 + '\n' + passwords6 + '\n' + passwords7 + '\n' + passwords8 + '\n' + passwords9 + '\n' + passwords10 + '\n'+ passwords11 + '\n'+ passwords12 + '\n')
        elif mpar == 1 :
            print("not now")
    elif add3 == 2 :
        if mpar == 0 :
            if lowercap == 0:
                for j1 in selected_list:
                    for j2 in selected_list:
                        with open(filename + ".txt", 'a') as f:
                            passwords1 = f"{Parameter1}{Parameter2}{j1}{j2}"
                            passwords2 = f"{Parameter1}{j1}{Parameter2}{j2}"
                            passwords3 = f"{Parameter1}{j1}{j2}{Parameter2}"
                            passwords4 = f"{Parameter2}{Parameter1}{j1}{j2}"                      
                            passwords5 = f"{Parameter2}{j1}{Parameter1}{j2}"
                            passwords6 = f"{Parameter2}{j1}{j2}{Parameter1}"
                            passwords7 = f"{j1}{Parameter1}{Parameter2}{j2}"
                            passwords8 = f"{j1}{Parameter1}{j2}{Parameter2}"
                            passwords9 = f"{j1}{Parameter2}{Parameter1}{j2}"
                            passwords10 = f"{j1}{Parameter2}{j2}{Parameter1}"
                            passwords11 = f"{j1}{j2}{Parameter1}{Parameter2}"
                            passwords12 = f"{j1}{j2}{Parameter2}{Parameter1}"
                            print(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' +passwords4 + '\n' + passwords5 + '\n' + passwords6 + '\n' + passwords7 + '\n' + passwords8 + '\n' + passwords9 + '\n' + passwords10 + '\n'+ passwords11 + '\n'+ passwords12 + '\n')
                            f.write(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' +passwords4 + '\n' + passwords5 + '\n' + passwords6 + '\n' + passwords7 + '\n' + passwords8 + '\n' + passwords9 + '\n' + passwords10 + '\n'+ passwords11 + '\n'+ passwords12 + '\n')
            elif lowercap == 1:
                for j1 in selected_list:
                    for j2 in selected_list:
                        with open(filename + ".txt", 'a') as f:
                            passwords1 = f"{Parameter1}{Parameter2}{j1}{j2}"
                            passwords2 = f"{Parameter1}{j1}{Parameter2}{j2}"
                            passwords3 = f"{Parameter1}{j1}{j2}{Parameter2}"
                            passwords4 = f"{Parameter2}{Parameter1}{j1}{j2}"                      
                            passwords5 = f"{Parameter2}{j1}{Parameter1}{j2}"
                            passwords6 = f"{Parameter2}{j1}{j2}{Parameter1}"
                            passwords7 = f"{j1}{Parameter1}{Parameter2}{j2}"
                            passwords8 = f"{j1}{Parameter1}{j2}{Parameter2}"
                            passwords9 = f"{j1}{Parameter2}{Parameter1}{j2}"
                            passwords10 = f"{j1}{Parameter2}{j2}{Parameter1}"
                            passwords11 = f"{j1}{j2}{Parameter1}{Parameter2}"
                            passwords12 = f"{j1}{j2}{Parameter2}{Parameter1}"
                            passwords1 = f"{Parameter1.capitalize()}{Parameter2}{j1}{j2}"
                            passwords2 = f"{Parameter1.capitalize()}{j1}{Parameter2}{j2}"
                            passwords3 = f"{Parameter1.capitalize()}{j1}{j2}{Parameter2}"
                            passwords4 = f"{Parameter2.capitalize()}{Parameter1}{j1}{j2}"                      
                            passwords5 = f"{Parameter2.capitalize()}{j1}{Parameter1}{j2}"
                            passwords6 = f"{Parameter2.capitalize()}{j1}{j2}{Parameter1}"
                            passwords7 = f"{j1}{Parameter1.capitalize()}{Parameter2}{j2}"
                            passwords8 = f"{j1}{Parameter1.capitalize()}{j2}{Parameter2}"
                            passwords9 = f"{j1}{Parameter2.capitalize()}{Parameter1}{j2}"
                            passwords10 = f"{j1}{Parameter2.capitalize()}{j2}{Parameter1}"
                            passwords11 = f"{j1}{j2}{Parameter1.capitalize()}{Parameter2}"
                            passwords12 = f"{j1}{j2}{Parameter2.capitalize()}{Parameter1}"                            
                            print(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' +passwords4 + '\n' + passwords5 + '\n' + passwords6 + '\n' + passwords7 + '\n' + passwords8 + '\n' + passwords9 + '\n' + passwords10 + '\n'+ passwords11 + '\n'+ passwords12 + '\n')
                            f.write(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' +passwords4 + '\n' + passwords5 + '\n' + passwords6 + '\n' + passwords7 + '\n' + passwords8 + '\n' + passwords9 + '\n' + passwords10 + '\n'+ passwords11 + '\n'+ passwords12 + '\n')
        elif mpar == 1 :
            print("not now")      
    elif add3 == 3 :
        if mpar == 0:
            if lowercap == 0:
                for j1 in selected_list:
                    for j2 in selected_list:
                        for j3 in selected_list:
                            with open(filename + ".txt", 'a') as f:
                                passwords1 = f"{Parameter1}{Parameter2}{j1}{j2}{j3}"
                                passwords2 = f"{Parameter1}{j1}{Parameter2}{j2}{j3}"   
                                passwords3 = f"{Parameter1}{j1}{j2}{Parameter2}{j3}"   
                                passwords4 = f"{Parameter1}{j1}{j2}{j3}{Parameter2}"  
                                passwords5 = f"{Parameter2}{Parameter1}{j1}{j2}{j3}"
                                passwords6 = f"{Parameter2}{j1}{Parameter1}{j2}{j3}"
                                passwords7 = f"{Parameter2}{j1}{j2}{Parameter1}{j3}"
                                passwords8 = f"{Parameter2}{j1}{j2}{j3}{Parameter1}"
                                passwords9 = f"{j1}{Parameter1}{Parameter2}{j2}{j3}"
                                passwords10 = f"{j1}{Parameter1}{j2}{Parameter2}{j3}"
                                passwords11 = f"{j1}{Parameter1}{j2}{j3}{Parameter2}"
                                passwords12 = f"{j1}{Parameter2}{Parameter1}{j2}{j3}"
                                passwords13 = f"{j1}{Parameter2}{j2}{Parameter1}{j3}"
                                passwords14 = f"{j1}{Parameter2}{j2}{j3}{Parameter1}"
                                passwords15 = f"{j1}{j2}{Parameter1}{Parameter2}{j3}"
                                passwords16 = f"{j1}{j2}{Parameter1}{j3}{Parameter2}"
                                passwords17 = f"{j1}{j2}{Parameter2}{Parameter1}{j3}"
                                passwords18 = f"{j1}{j2}{Parameter2}{j3}{Parameter1}"
                                passwords19 = f"{j1}{j2}{j3}{Parameter1}{Parameter2}"
                                passwords20 = f"{j1}{j2}{j3}{Parameter2}{Parameter1}"
                                print(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' +passwords4 + '\n' + passwords5 + '\n' + passwords6 + '\n' + passwords7 + '\n' + passwords8 + '\n' + passwords9 + '\n' + passwords10 + '\n'+ passwords11 + '\n'+ passwords12 + '\n' + passwords13 + '\n' + passwords14 + '\n' + passwords15 + '\n'+ passwords16 + '\n'+ passwords17 + '\n'+ passwords18 + '\n'+ passwords19 + '\n' + passwords20 + '\n')
                                f.write(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' +passwords4 + '\n' + passwords5 + '\n' + passwords6 + '\n' + passwords7 + '\n' + passwords8 + '\n' + passwords9 + '\n' + passwords10 + '\n'+ passwords11 + '\n'+ passwords12 + '\n' + passwords13 + '\n' + passwords14 + '\n' + passwords15 + '\n'+ passwords16 + '\n'+ passwords17 + '\n'+ passwords18 + '\n'+ passwords19 + '\n' + passwords20 + '\n')
            if lowercap == 1 :
                for j1 in selected_list:
                    for j2 in selected_list:
                        for j3 in selected_list:
                            with open(filename + ".txt", 'a') as f:
                                passwords1 = f"{Parameter1}{Parameter2}{j1}{j2}{j3}"
                                passwords2 = f"{Parameter1}{j1}{Parameter2}{j2}{j3}"   
                                passwords3 = f"{Parameter1}{j1}{j2}{Parameter2}{j3}"   
                                passwords4 = f"{Parameter1}{j1}{j2}{j3}{Parameter2}"  
                                passwords5 = f"{Parameter2}{Parameter1}{j1}{j2}{j3}"
                                passwords6 = f"{Parameter2}{j1}{Parameter1}{j2}{j3}"
                                passwords7 = f"{Parameter2}{j1}{j2}{Parameter1}{j3}"
                                passwords8 = f"{Parameter2}{j1}{j2}{j3}{Parameter1}"
                                passwords9 = f"{j1}{Parameter1}{Parameter2}{j2}{j3}"
                                passwords10 = f"{j1}{Parameter1}{j2}{Parameter2}{j3}"
                                passwords11 = f"{j1}{Parameter1}{j2}{j3}{Parameter2}"
                                passwords12 = f"{j1}{Parameter2}{Parameter1}{j2}{j3}"
                                passwords13 = f"{j1}{Parameter2}{j2}{Parameter1}{j3}"
                                passwords14 = f"{j1}{Parameter2}{j2}{j3}{Parameter1}"
                                passwords15 = f"{j1}{j2}{Parameter1}{Parameter2}{j3}"
                                passwords16 = f"{j1}{j2}{Parameter1}{j3}{Parameter2}"
                                passwords17 = f"{j1}{j2}{Parameter2}{Parameter1}{j3}"
                                passwords18 = f"{j1}{j2}{Parameter2}{j3}{Parameter1}"
                                passwords19 = f"{j1}{j2}{j3}{Parameter1}{Parameter2}"
                                passwords20 = f"{j1}{j2}{j3}{Parameter2}{Parameter1}"
                                passwords21 = f"{Parameter1.capitalize()}{Parameter2}{j1}{j2}{j3}"
                                passwords22 = f"{Parameter1.capitalize()}{j1}{Parameter2}{j2}{j3}"   
                                passwords23 = f"{Parameter1.capitalize()}{j1}{j2}{Parameter2}{j3}"   
                                passwords24 = f"{Parameter1.capitalize()}{j1}{j2}{j3}{Parameter2}"  
                                passwords25 = f"{Parameter2.capitalize()}{Parameter1}{j1}{j2}{j3}"
                                passwords26 = f"{Parameter2.capitalize()}{j1}{Parameter1}{j2}{j3}"
                                passwords27 = f"{Parameter2.capitalize()}{j1}{j2}{Parameter1}{j3}"
                                passwords28 = f"{Parameter2.capitalize()}{j1}{j2}{j3}{Parameter1}"
                                passwords29 = f"{j1}{Parameter1.capitalize()}{Parameter2}{j2}{j3}"
                                passwords30 = f"{j1}{Parameter1.capitalize()}{j2}{Parameter2}{j3}"
                                passwords31 = f"{j1}{Parameter1.capitalize()}{j2}{j3}{Parameter2}"
                                passwords32 = f"{j1}{Parameter2.capitalize()}{Parameter1}{j2}{j3}"
                                passwords33 = f"{j1}{Parameter2.capitalize()}{j2}{Parameter1}{j3}"
                                passwords34 = f"{j1}{Parameter2.capitalize()}{j2}{j3}{Parameter1}"
                                passwords35 = f"{j1}{j2}{Parameter1.capitalize()}{Parameter2}{j3}"
                                passwords36 = f"{j1}{j2}{Parameter1.capitalize()}{j3}{Parameter2}"
                                passwords37 = f"{j1}{j2}{Parameter2.capitalize()}{Parameter1}{j3}"
                                passwords38 = f"{j1}{j2}{Parameter2.capitalize()}{j3}{Parameter1}"
                                passwords39 = f"{j1}{j2}{j3}{Parameter1.capitalize()}{Parameter2}"
                                passwords40 = f"{j1}{j2}{j3}{Parameter2.capitalize()}{Parameter1}"
                                print(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' +passwords4 + '\n' + passwords5 + '\n' + passwords6 + '\n' + passwords7 + '\n' + passwords8 + '\n' + passwords9 + '\n' + passwords10 + '\n'+ passwords11 + '\n'+ passwords12 + '\n' + passwords13 + '\n' + passwords14 + '\n' + passwords15 + '\n'+ passwords16 + '\n'+ passwords17 + '\n' + passwords18 + '\n'+ passwords19 + '\n'+ passwords20 + '\n' +passwords21 + '\n' + passwords22 + '\n' + passwords23 + '\n' + passwords24 + '\n' + passwords25 + '\n' + passwords26 + '\n' + passwords27 + '\n'+ passwords28 + '\n'+ passwords29 + '\n' + passwords30 + '\n' + passwords31 + '\n' + passwords32 + '\n'+ passwords33 + '\n'+ passwords34 + '\n'+ passwords35 + '\n'+ passwords36 + '\n' + passwords37 + '\n'+ passwords38 + '\n'+ passwords39 + '\n'+ passwords40 + '\n')
                                f.write(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' +passwords4 + '\n' + passwords5 + '\n' + passwords6 + '\n' + passwords7 + '\n' + passwords8 + '\n' + passwords9 + '\n' + passwords10 + '\n'+ passwords11 + '\n'+ passwords12 + '\n' + passwords13 + '\n' + passwords14 + '\n' + passwords15 + '\n'+ passwords16 + '\n'+ passwords17 + '\n' + passwords18 + '\n'+ passwords19 + '\n'+ passwords20 + '\n' +passwords21 + '\n' + passwords22 + '\n' + passwords23 + '\n' + passwords24 + '\n' + passwords25 + '\n' + passwords26 + '\n' + passwords27 + '\n'+ passwords28 + '\n'+ passwords29 + '\n' + passwords30 + '\n' + passwords31 + '\n' + passwords32 + '\n'+ passwords33 + '\n'+ passwords34 + '\n'+ passwords35 + '\n'+ passwords36 + '\n' + passwords37 + '\n'+ passwords38 + '\n'+ passwords39 + '\n'+ passwords40 + '\n')
        elif mpar == 1 :
            print("not now")
    elif add3 == 4 :
        if mpar == 0:
            if lowercap == 0:
                for j1 in selected_list:
                    for j2 in selected_list:
                        for j3 in selected_list:
                            for j4 in selected_list:
                                with open(filename + ".txt", 'a') as f:
                                    passwords1 = f"{Parameter1}{Parameter2}{j1}{j2}{j3}{j4}"
                                    passwords2 = f"{Parameter1}{j1}{Parameter2}{j2}{j3}{j4}"
                                    passwords3 = f"{Parameter1}{j1}{j2}{Parameter2}{j3}{j4}"
                                    passwords4 = f"{Parameter1}{j1}{j2}{j3}{Parameter2}{j4}"
                                    passwords5 = f"{Parameter1}{j1}{j2}{j3}{j4}{Parameter2}"
                                    passwords6 = f"{Parameter2}{Parameter1}{j1}{j2}{j3}{j4}"
                                    passwords7 = f"{Parameter2}{j1}{Parameter1}{j2}{j3}{j4}"
                                    passwords8 = f"{Parameter2}{j1}{j2}{Parameter1}{j3}{j4}"
                                    passwords9 = f"{Parameter2}{j1}{j2}{j3}{Parameter1}{j4}"
                                    passwords10 = f"{Parameter2}{j1}{j2}{j3}{j4}{Parameter1}"
                                    passwords11 = f"{j1}{Parameter1}{Parameter2}{j2}{j3}{j4}"
                                    passwords12 = f"{j1}{Parameter1}{j2}{Parameter2}{j3}{j4}"
                                    passwords13 = f"{j1}{Parameter1}{j2}{j3}{Parameter2}{j4}"
                                    passwords14 = f"{j1}{Parameter1}{j2}{j3}{j4}{Parameter2}"
                                    passwords15 = f"{j1}{Parameter2}{Parameter1}{j2}{j3}{j4}"
                                    passwords16 = f"{j1}{Parameter2}{j2}{Parameter1}{j3}{j4}"
                                    passwords17 = f"{j1}{Parameter2}{j2}{j3}{Parameter1}{j4}"
                                    passwords18 = f"{j1}{Parameter2}{j2}{j3}{j4}{Parameter1}"
                                    passwords19 = f"{j1}{j2}{Parameter1}{Parameter2}{j3}{j4}"
                                    passwords20 = f"{j1}{j2}{Parameter1}{j3}{Parameter2}{j4}"
                                    passwords21 = f"{j1}{j2}{Parameter1}{j3}{j4}{Parameter2}"
                                    passwords22 = f"{j1}{j2}{Parameter2}{Parameter1}{j3}{j4}"
                                    passwords23 = f"{j1}{j2}{Parameter2}{j3}{Parameter1}{j4}"
                                    passwords24 = f"{j1}{j2}{Parameter2}{j3}{j4}{Parameter1}"
                                    passwords25 = f"{j1}{j2}{j3}{Parameter1}{Parameter2}{j4}"
                                    passwords26 = f"{j1}{j2}{j3}{Parameter1}{j4}{Parameter2}"
                                    passwords27 = f"{j1}{j2}{j3}{Parameter2}{Parameter1}{j4}"
                                    passwords28 = f"{j1}{j2}{j3}{Parameter2}{j4}{Parameter1}"
                                    passwords29 = f"{j1}{j2}{j3}{j4}{Parameter1}{Parameter2}"
                                    passwords30 = f"{j1}{j2}{j3}{j4}{Parameter2}{Parameter1}"
                                    print(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' +passwords4 + '\n' + passwords5 + '\n' + passwords6 + '\n' + passwords7 + '\n' + passwords8 + '\n' + passwords9 + '\n' + passwords10 + '\n'+ passwords11 + '\n'+ passwords12 + '\n' + passwords13 + '\n' + passwords14 + '\n' + passwords15 + '\n'+ passwords16 + '\n'+ passwords17 + '\n'+ passwords18 + '\n'+ passwords19 + '\n' + passwords20 + '\n' + passwords21 + '\n'+ passwords22 + '\n'+ passwords23 + '\n' + passwords24 + '\n' + passwords25 + '\n' + passwords26 + '\n'+ passwords27 + '\n'+ passwords28 +'\n'+ passwords29 + '\n'+ passwords30 + '\n')
                                    f.write(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' +passwords4 + '\n' + passwords5 + '\n' + passwords6 + '\n' + passwords7 + '\n' + passwords8 + '\n' + passwords9 + '\n' + passwords10 + '\n'+ passwords11 + '\n'+ passwords12 + '\n' + passwords13 + '\n' + passwords14 + '\n' + passwords15 + '\n'+ passwords16 + '\n'+ passwords17 + '\n'+ passwords18 + '\n'+ passwords19 + '\n' + passwords20 + '\n' + passwords21 + '\n'+ passwords22 + '\n'+ passwords23 + '\n' + passwords24 + '\n' + passwords25 + '\n' + passwords26 + '\n'+ passwords27 + '\n'+ passwords28 +'\n'+ passwords29 + '\n'+ passwords30 + '\n')
            if lowercap == 1 :
                for j1 in selected_list:
                    for j2 in selected_list:
                        for j3 in selected_list:
                            for j4 in selected_list:
                                with open(filename + ".txt", 'a') as f:
                                    passwords1 = f"{Parameter1}{Parameter2}{j1}{j2}{j3}{j4}"
                                    passwords2 = f"{Parameter1}{j1}{Parameter2}{j2}{j3}{j4}"
                                    passwords3 = f"{Parameter1}{j1}{j2}{Parameter2}{j3}{j4}"
                                    passwords4 = f"{Parameter1}{j1}{j2}{j3}{Parameter2}{j4}"
                                    passwords5 = f"{Parameter1}{j1}{j2}{j3}{j4}{Parameter2}"
                                    passwords6 = f"{Parameter2}{Parameter1}{j1}{j2}{j3}{j4}"
                                    passwords7 = f"{Parameter2}{j1}{Parameter1}{j2}{j3}{j4}"
                                    passwords8 = f"{Parameter2}{j1}{j2}{Parameter1}{j3}{j4}"
                                    passwords9 = f"{Parameter2}{j1}{j2}{j3}{Parameter1}{j4}"
                                    passwords10 = f"{Parameter2}{j1}{j2}{j3}{j4}{Parameter1}"
                                    passwords11 = f"{j1}{Parameter1}{Parameter2}{j2}{j3}{j4}"
                                    passwords12 = f"{j1}{Parameter1}{j2}{Parameter2}{j3}{j4}"
                                    passwords13 = f"{j1}{Parameter1}{j2}{j3}{Parameter2}{j4}"
                                    passwords14 = f"{j1}{Parameter1}{j2}{j3}{j4}{Parameter2}"
                                    passwords15 = f"{j1}{Parameter2}{Parameter1}{j2}{j3}{j4}"
                                    passwords16 = f"{j1}{Parameter2}{j2}{Parameter1}{j3}{j4}"
                                    passwords17 = f"{j1}{Parameter2}{j2}{j3}{Parameter1}{j4}"
                                    passwords18 = f"{j1}{Parameter2}{j2}{j3}{j4}{Parameter1}"
                                    passwords19 = f"{j1}{j2}{Parameter1}{Parameter2}{j3}{j4}"
                                    passwords20 = f"{j1}{j2}{Parameter1}{j3}{Parameter2}{j4}"
                                    passwords21 = f"{j1}{j2}{Parameter1}{j3}{j4}{Parameter2}"
                                    passwords22 = f"{j1}{j2}{Parameter2}{Parameter1}{j3}{j4}"
                                    passwords23 = f"{j1}{j2}{Parameter2}{j3}{Parameter1}{j4}"
                                    passwords24 = f"{j1}{j2}{Parameter2}{j3}{j4}{Parameter1}"
                                    passwords25 = f"{j1}{j2}{j3}{Parameter1}{Parameter2}{j4}"
                                    passwords26 = f"{j1}{j2}{j3}{Parameter1}{j4}{Parameter2}"
                                    passwords27 = f"{j1}{j2}{j3}{Parameter2}{Parameter1}{j4}"
                                    passwords28 = f"{j1}{j2}{j3}{Parameter2}{j4}{Parameter1}"
                                    passwords29 = f"{j1}{j2}{j3}{j4}{Parameter1}{Parameter2}"
                                    passwords30 = f"{j1}{j2}{j3}{j4}{Parameter2}{Parameter1}"
                                    passwords31 = f"{Parameter1.capitalize()}{Parameter2}{j1}{j2}{j3}{j4}"
                                    passwords32 = f"{Parameter1.capitalize()}{j1}{Parameter2}{j2}{j3}{j4}"
                                    passwords33 = f"{Parameter1.capitalize()}{j1}{j2}{Parameter2}{j3}{j4}"
                                    passwords34 = f"{Parameter1.capitalize()}{j1}{j2}{j3}{Parameter2}{j4}"
                                    passwords35 = f"{Parameter1.capitalize()}{j1}{j2}{j3}{j4}{Parameter2}"
                                    passwords36 = f"{Parameter2.capitalize()}{Parameter1}{j1}{j2}{j3}{j4}"
                                    passwords37 = f"{Parameter2.capitalize()}{j1}{Parameter1}{j2}{j3}{j4}"
                                    passwords38 = f"{Parameter2.capitalize()}{j1}{j2}{Parameter1}{j3}{j4}"
                                    passwords39 = f"{Parameter2.capitalize()}{j1}{j2}{j3}{Parameter1}{j4}"
                                    passwords40 = f"{Parameter2.capitalize()}{j1}{j2}{j3}{j4}{Parameter1}"
                                    passwords41 = f"{j1}{Parameter1.capitalize()}{Parameter2}{j2}{j3}{j4}"
                                    passwords42 = f"{j1}{Parameter1.capitalize()}{j2}{Parameter2}{j3}{j4}"
                                    passwords43 = f"{j1}{Parameter1.capitalize()}{j2}{j3}{Parameter2}{j4}"
                                    passwords44 = f"{j1}{Parameter1.capitalize()}{j2}{j3}{j4}{Parameter2}"
                                    passwords45 = f"{j1}{Parameter2.capitalize()}{Parameter1}{j2}{j3}{j4}"
                                    passwords46 = f"{j1}{Parameter2.capitalize()}{j2}{Parameter1}{j3}{j4}"
                                    passwords47 = f"{j1}{Parameter2.capitalize()}{j2}{j3}{Parameter1}{j4}"
                                    passwords48 = f"{j1}{Parameter2.capitalize()}{j2}{j3}{j4}{Parameter1}"
                                    passwords49 = f"{j1}{j2}{Parameter1.capitalize()}{Parameter2}{j3}{j4}"
                                    passwords50 = f"{j1}{j2}{Parameter1.capitalize()}{j3}{Parameter2}{j4}"
                                    passwords51 = f"{j1}{j2}{Parameter1.capitalize()}{j3}{j4}{Parameter2}"
                                    passwords52 = f"{j1}{j2}{Parameter2.capitalize()}{Parameter1}{j3}{j4}"
                                    passwords53 = f"{j1}{j2}{Parameter2.capitalize()}{j3}{Parameter1}{j4}"
                                    passwords54 = f"{j1}{j2}{Parameter2.capitalize()}{j3}{j4}{Parameter1}"
                                    passwords55 = f"{j1}{j2}{j3}{Parameter1.capitalize()}{Parameter2}{j4}"
                                    passwords56 = f"{j1}{j2}{j3}{Parameter1.capitalize()}{j4}{Parameter2}"
                                    passwords57 = f"{j1}{j2}{j3}{Parameter2.capitalize()}{Parameter1}{j4}"
                                    passwords58 = f"{j1}{j2}{j3}{Parameter2.capitalize()}{j4}{Parameter1}"
                                    passwords59 = f"{j1}{j2}{j3}{j4}{Parameter1.capitalize()}{Parameter2}"
                                    passwords60 = f"{j1}{j2}{j3}{j4}{Parameter2.capitalize()}{Parameter1}"                          
                                    print(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' +passwords4 + '\n' + passwords5 + '\n' + passwords6 + '\n' + passwords7 + '\n' + passwords8 + '\n' + passwords9 + '\n' + passwords10 + '\n'+ passwords11 + '\n'+ passwords12 + '\n' + passwords13 + '\n' + passwords14 + '\n' + passwords15 + '\n'+ passwords16 + '\n'+ passwords17 + '\n' + passwords18 + '\n'+ passwords19 + '\n'+ passwords20 + '\n' +passwords21 + '\n' + passwords22 + '\n' + passwords23 + '\n' + passwords24 + '\n' + passwords25 + '\n' + passwords26 + '\n' + passwords27 + '\n'+ passwords28 + '\n'+ passwords29 + '\n' + passwords30 + '\n' + passwords31 + '\n' + passwords32 + '\n'+ passwords33 + '\n'+ passwords34 + '\n'+ passwords35 + '\n'+ passwords36 + '\n'+ passwords37 + '\n'+ passwords38 + '\n' +passwords39 + '\n' + passwords40 + '\n' + passwords41 + '\n' + passwords42 + '\n' + passwords43 + '\n' + passwords44 + '\n' + passwords45 + '\n'+ passwords46 + '\n'+ passwords47 + '\n' + passwords48 + '\n' + passwords49 + '\n' + passwords50 + '\n'+ passwords51 + '\n'+ passwords52 + '\n' + passwords53 + '\n'+ passwords54 + '\n'+ passwords55 + '\n' +passwords56 + '\n' + passwords57 + '\n' + passwords58 + '\n' + passwords59 + '\n' + passwords60 + '\n' )
                                    f.write(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' +passwords4 + '\n' + passwords5 + '\n' + passwords6 + '\n' + passwords7 + '\n' + passwords8 + '\n' + passwords9 + '\n' + passwords10 + '\n'+ passwords11 + '\n'+ passwords12 + '\n' + passwords13 + '\n' + passwords14 + '\n' + passwords15 + '\n'+ passwords16 + '\n'+ passwords17 + '\n' + passwords18 + '\n'+ passwords19 + '\n'+ passwords20 + '\n' +passwords21 + '\n' + passwords22 + '\n' + passwords23 + '\n' + passwords24 + '\n' + passwords25 + '\n' + passwords26 + '\n' + passwords27 + '\n'+ passwords28 + '\n'+ passwords29 + '\n' + passwords30 + '\n' + passwords31 + '\n' + passwords32 + '\n'+ passwords33 + '\n'+ passwords34 + '\n'+ passwords35 + '\n'+ passwords36 + '\n'+ passwords37 + '\n'+ passwords38 + '\n' +passwords39 + '\n' + passwords40 + '\n' + passwords41 + '\n' + passwords42 + '\n' + passwords43 + '\n' + passwords44 + '\n' + passwords45 + '\n'+ passwords46 + '\n'+ passwords47 + '\n' + passwords48 + '\n' + passwords49 + '\n' + passwords50 + '\n'+ passwords51 + '\n'+ passwords52 + '\n' + passwords53 + '\n'+ passwords54 + '\n'+ passwords55 + '\n' +passwords56 + '\n' + passwords57 + '\n' + passwords58 + '\n' + passwords59 + '\n' + passwords60 + '\n' )
        if mpar == 1:
            print("not now")
    elif add3 == 5 :
        if mpar == 0:
            if lowercap == 0:
                for j1 in selected_list:
                    for j2 in selected_list:
                        for j3 in selected_list:
                            for j4 in selected_list:
                                for j5 in selected_list:
                                    with open(filename + ".txt", 'a') as f:
                                        passwords1 = f"{Parameter1}{Parameter2}{j1}{j2}{j3}{j4}{j5}"
                                        passwords2 = f"{Parameter1}{j1}{Parameter2}{j2}{j3}{j4}{j5}"
                                        passwords3 = f"{Parameter1}{j1}{j2}{Parameter2}{j3}{j4}{j5}"
                                        passwords4 = f"{Parameter1}{j1}{j2}{j3}{Parameter2}{j4}{j5}"
                                        passwords5 = f"{Parameter1}{j1}{j2}{j3}{j4}{Parameter2}{j5}"
                                        passwords6 = f"{Parameter1}{j1}{j2}{j3}{j4}{j5}{Parameter2}"
                                        passwords7 = f"{Parameter2}{Parameter1}{j1}{j2}{j3}{j4}{j5}"
                                        passwords8 = f"{Parameter2}{j1}{Parameter1}{j2}{j3}{j4}{j5}"
                                        passwords9 = f"{Parameter2}{j1}{j2}{Parameter1}{j3}{j4}{j5}"
                                        passwords10 = f"{Parameter2}{j1}{j2}{j3}{Parameter1}{j4}{j5}"
                                        passwords11 = f"{Parameter2}{j1}{j2}{j3}{j4}{Parameter1}{j5}"
                                        passwords12 = f"{Parameter2}{j1}{j2}{j3}{j4}{j5}{Parameter1}"
                                        passwords13 = f"{j1}{Parameter1}{Parameter2}{j2}{j3}{j4}{j5}"
                                        passwords14 = f"{j1}{Parameter1}{j2}{Parameter2}{j3}{j4}{j5}"
                                        passwords15 = f"{j1}{Parameter1}{j2}{j3}{Parameter2}{j4}{j5}"
                                        passwords16 = f"{j1}{Parameter1}{j2}{j3}{j4}{Parameter2}{j5}"
                                        passwords17 = f"{j1}{Parameter1}{j2}{j3}{j4}{j5}{Parameter2}"
                                        passwords18 = f"{j1}{Parameter2}{Parameter1}{j2}{j3}{j4}{j5}"
                                        passwords19 = f"{j1}{Parameter2}{j2}{Parameter1}{j3}{j4}{j5}"
                                        passwords20 = f"{j1}{Parameter2}{j2}{j3}{Parameter1}{j4}{j5}"
                                        passwords21 = f"{j1}{Parameter2}{j2}{j3}{j4}{Parameter1}{j5}"
                                        passwords22 = f"{j1}{Parameter2}{j2}{j3}{j4}{j5}{Parameter1}"
                                        passwords23 = f"{j1}{j2}{Parameter1}{Parameter2}{j3}{j4}{j5}"
                                        passwords24 = f"{j1}{j2}{Parameter1}{j3}{Parameter2}{j4}{j5}"
                                        passwords25 = f"{j1}{j2}{Parameter1}{j3}{j4}{Parameter2}{j5}"
                                        passwords26 = f"{j1}{j2}{Parameter1}{j3}{j4}{j5}{Parameter2}"
                                        passwords27 = f"{j1}{j2}{Parameter2}{Parameter1}{j3}{j4}{j5}"
                                        passwords28 = f"{j1}{j2}{Parameter2}{j3}{Parameter1}{j4}{j5}"
                                        passwords29 = f"{j1}{j2}{Parameter2}{j3}{j4}{Parameter1}{j5}"
                                        passwords30 = f"{j1}{j2}{Parameter2}{j3}{j4}{j5}{Parameter1}"
                                        passwords31 = f"{j1}{j2}{j3}{Parameter1}{Parameter2}{j4}{j5}"
                                        passwords32 = f"{j1}{j2}{j3}{Parameter1}{j4}{Parameter2}{j5}"
                                        passwords33 = f"{j1}{j2}{j3}{Parameter1}{j4}{j5}{Parameter2}"
                                        passwords34 = f"{j1}{j2}{j3}{Parameter2}{Parameter1}{j4}{j5}"
                                        passwords35 = f"{j1}{j2}{j3}{Parameter2}{j4}{Parameter1}{j5}"
                                        passwords36 = f"{j1}{j2}{j3}{Parameter2}{j4}{j5}{Parameter1}"
                                        passwords37 = f"{j1}{j2}{j3}{j4}{Parameter1}{Parameter2}{j5}"
                                        passwords38 = f"{j1}{j2}{j3}{j4}{Parameter1}{j5}{Parameter2}"
                                        passwords39 = f"{j1}{j2}{j3}{j4}{Parameter2}{Parameter1}{j5}"
                                        passwords40 = f"{j1}{j2}{j3}{j4}{Parameter2}{j5}{Parameter1}"
                                        passwords41 = f"{j1}{j2}{j3}{j4}{j5}{Parameter1}{Parameter2}"
                                        passwords42 = f"{j1}{j2}{j3}{j4}{j5}{Parameter2}{Parameter1}"
                                        print(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' +passwords4 + '\n' + passwords5 + '\n' + passwords6 + '\n' + passwords7 + '\n' + passwords8 + '\n' + passwords9 + '\n' + passwords10 + '\n'+ passwords11 + '\n'+ passwords12 + '\n' + passwords13 + '\n' + passwords14 + '\n' + passwords15 + '\n'+ passwords16 + '\n'+ passwords17 + '\n'+ passwords18 + '\n'+ passwords19 + '\n' + passwords20 + '\n' + passwords21 + '\n'+ passwords22 + '\n'+ passwords23 + '\n' + passwords24 + '\n' + passwords25 + '\n' + passwords26 + '\n'+ passwords27 + '\n'+ passwords28 +'\n'+ passwords29 + '\n'+ passwords30 +'\n'+ passwords31 + '\n'+ passwords32 + '\n' +passwords33 + '\n' + passwords34 + '\n' + passwords35 + '\n' + passwords36 + '\n' + passwords37 + '\n' + passwords38 + '\n' + passwords39 + '\n'+ passwords40 + '\n'+ passwords41 + '\n' + passwords42 + '\n' )
                                        f.write(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' +passwords4 + '\n' + passwords5 + '\n' + passwords6 + '\n' + passwords7 + '\n' + passwords8 + '\n' + passwords9 + '\n' + passwords10 + '\n'+ passwords11 + '\n'+ passwords12 + '\n' + passwords13 + '\n' + passwords14 + '\n' + passwords15 + '\n'+ passwords16 + '\n'+ passwords17 + '\n'+ passwords18 + '\n'+ passwords19 + '\n' + passwords20 + '\n' + passwords21 + '\n'+ passwords22 + '\n'+ passwords23 + '\n' + passwords24 + '\n' + passwords25 + '\n' + passwords26 + '\n'+ passwords27 + '\n'+ passwords28 +'\n'+ passwords29 + '\n'+ passwords30 + '\n'+ passwords31 + '\n'+ passwords32 + '\n' +passwords33 + '\n' + passwords34 + '\n' + passwords35 + '\n' + passwords36 + '\n' + passwords37 + '\n' + passwords38 + '\n' + passwords39 + '\n'+ passwords40 + '\n'+ passwords41 + '\n' + passwords42 + '\n' )
            if lowercap == 1 :
                for j1 in selected_list:
                    for j2 in selected_list:
                        for j3 in selected_list:
                            for j4 in selected_list:
                                for j5 in selected_list:
                                    with open(filename + ".txt", 'a') as f:
                                        passwords1 = f"{Parameter1}{Parameter2}{j1}{j2}{j3}{j4}{j5}"
                                        passwords2 = f"{Parameter1}{j1}{Parameter2}{j2}{j3}{j4}{j5}"
                                        passwords3 = f"{Parameter1}{j1}{j2}{Parameter2}{j3}{j4}{j5}"
                                        passwords4 = f"{Parameter1}{j1}{j2}{j3}{Parameter2}{j4}{j5}"
                                        passwords5 = f"{Parameter1}{j1}{j2}{j3}{j4}{Parameter2}{j5}"
                                        passwords6 = f"{Parameter1}{j1}{j2}{j3}{j4}{j5}{Parameter2}"
                                        passwords7 = f"{Parameter2}{Parameter1}{j1}{j2}{j3}{j4}{j5}"
                                        passwords8 = f"{Parameter2}{j1}{Parameter1}{j2}{j3}{j4}{j5}"
                                        passwords9 = f"{Parameter2}{j1}{j2}{Parameter1}{j3}{j4}{j5}"
                                        passwords10 = f"{Parameter2}{j1}{j2}{j3}{Parameter1}{j4}{j5}"
                                        passwords11 = f"{Parameter2}{j1}{j2}{j3}{j4}{Parameter1}{j5}"
                                        passwords12 = f"{Parameter2}{j1}{j2}{j3}{j4}{j5}{Parameter1}"
                                        passwords13 = f"{j1}{Parameter1}{Parameter2}{j2}{j3}{j4}{j5}"
                                        passwords14 = f"{j1}{Parameter1}{j2}{Parameter2}{j3}{j4}{j5}"
                                        passwords15 = f"{j1}{Parameter1}{j2}{j3}{Parameter2}{j4}{j5}"
                                        passwords16 = f"{j1}{Parameter1}{j2}{j3}{j4}{Parameter2}{j5}"
                                        passwords17 = f"{j1}{Parameter1}{j2}{j3}{j4}{j5}{Parameter2}"
                                        passwords18 = f"{j1}{Parameter2}{Parameter1}{j2}{j3}{j4}{j5}"
                                        passwords19 = f"{j1}{Parameter2}{j2}{Parameter1}{j3}{j4}{j5}"
                                        passwords20 = f"{j1}{Parameter2}{j2}{j3}{Parameter1}{j4}{j5}"
                                        passwords21 = f"{j1}{Parameter2}{j2}{j3}{j4}{Parameter1}{j5}"
                                        passwords22 = f"{j1}{Parameter2}{j2}{j3}{j4}{j5}{Parameter1}"
                                        passwords23 = f"{j1}{j2}{Parameter1}{Parameter2}{j3}{j4}{j5}"
                                        passwords24 = f"{j1}{j2}{Parameter1}{j3}{Parameter2}{j4}{j5}"
                                        passwords25 = f"{j1}{j2}{Parameter1}{j3}{j4}{Parameter2}{j5}"
                                        passwords26 = f"{j1}{j2}{Parameter1}{j3}{j4}{j5}{Parameter2}"
                                        passwords27 = f"{j1}{j2}{Parameter2}{Parameter1}{j3}{j4}{j5}"
                                        passwords28 = f"{j1}{j2}{Parameter2}{j3}{Parameter1}{j4}{j5}"
                                        passwords29 = f"{j1}{j2}{Parameter2}{j3}{j4}{Parameter1}{j5}"
                                        passwords30 = f"{j1}{j2}{Parameter2}{j3}{j4}{j5}{Parameter1}"
                                        passwords31 = f"{j1}{j2}{j3}{Parameter1}{Parameter2}{j4}{j5}"
                                        passwords32 = f"{j1}{j2}{j3}{Parameter1}{j4}{Parameter2}{j5}"
                                        passwords33 = f"{j1}{j2}{j3}{Parameter1}{j4}{j5}{Parameter2}"
                                        passwords34 = f"{j1}{j2}{j3}{Parameter2}{Parameter1}{j4}{j5}"
                                        passwords35 = f"{j1}{j2}{j3}{Parameter2}{j4}{Parameter1}{j5}"
                                        passwords36 = f"{j1}{j2}{j3}{Parameter2}{j4}{j5}{Parameter1}"
                                        passwords37 = f"{j1}{j2}{j3}{j4}{Parameter1}{Parameter2}{j5}"
                                        passwords38 = f"{j1}{j2}{j3}{j4}{Parameter1}{j5}{Parameter2}"
                                        passwords39 = f"{j1}{j2}{j3}{j4}{Parameter2}{Parameter1}{j5}"
                                        passwords40 = f"{j1}{j2}{j3}{j4}{Parameter2}{j5}{Parameter1}"
                                        passwords41 = f"{j1}{j2}{j3}{j4}{j5}{Parameter1}{Parameter2}"
                                        passwords42 = f"{j1}{j2}{j3}{j4}{j5}{Parameter2}{Parameter1}"
                                        passwords43 = f"{Parameter1.capitalize()}{Parameter2}{j1}{j2}{j3}{j4}{j5}"
                                        passwords44 = f"{Parameter1.capitalize()}{j1}{Parameter2}{j2}{j3}{j4}{j5}"
                                        passwords45 = f"{Parameter1.capitalize()}{j1}{j2}{Parameter2}{j3}{j4}{j5}"
                                        passwords46 = f"{Parameter1.capitalize()}{j1}{j2}{j3}{Parameter2}{j4}{j5}"
                                        passwords47 = f"{Parameter1.capitalize()}{j1}{j2}{j3}{j4}{Parameter2}{j5}"
                                        passwords48 = f"{Parameter1.capitalize()}{j1}{j2}{j3}{j4}{j5}{Parameter2}"
                                        passwords49 = f"{Parameter2.capitalize()}{Parameter1}{j1}{j2}{j3}{j4}{j5}"
                                        passwords50 = f"{Parameter2.capitalize()}{j1}{Parameter1}{j2}{j3}{j4}{j5}"
                                        passwords51 = f"{Parameter2.capitalize()}{j1}{j2}{Parameter1}{j3}{j4}{j5}"
                                        passwords52 = f"{Parameter2.capitalize()}{j1}{j2}{j3}{Parameter1}{j4}{j5}"
                                        passwords53 = f"{Parameter2.capitalize()}{j1}{j2}{j3}{j4}{Parameter1}{j5}"
                                        passwords54 = f"{Parameter2.capitalize()}{j1}{j2}{j3}{j4}{j5}{Parameter1}"
                                        passwords55 = f"{j1}{Parameter1.capitalize()}{Parameter2}{j2}{j3}{j4}{j5}"
                                        passwords56 = f"{j1}{Parameter1.capitalize()}{j2}{Parameter2}{j3}{j4}{j5}"
                                        passwords57 = f"{j1}{Parameter1.capitalize()}{j2}{j3}{Parameter2}{j4}{j5}"
                                        passwords58 = f"{j1}{Parameter1.capitalize()}{j2}{j3}{j4}{Parameter2}{j5}"
                                        passwords59 = f"{j1}{Parameter1.capitalize()}{j2}{j3}{j4}{j5}{Parameter2}"
                                        passwords60 = f"{j1}{Parameter2.capitalize()}{Parameter1}{j2}{j3}{j4}{j5}"
                                        passwords61 = f"{j1}{Parameter2.capitalize()}{j2}{Parameter1}{j3}{j4}{j5}"
                                        passwords62 = f"{j1}{Parameter2.capitalize()}{j2}{j3}{Parameter1}{j4}{j5}"
                                        passwords63 = f"{j1}{Parameter2.capitalize()}{j2}{j3}{j4}{Parameter1}{j5}"
                                        passwords64 = f"{j1}{Parameter2.capitalize()}{j2}{j3}{j4}{j5}{Parameter1}"
                                        passwords65 = f"{j1}{j2}{Parameter1.capitalize()}{Parameter2}{j3}{j4}{j5}"
                                        passwords66 = f"{j1}{j2}{Parameter1.capitalize()}{j3}{Parameter2}{j4}{j5}"
                                        passwords67 = f"{j1}{j2}{Parameter1.capitalize()}{j3}{j4}{Parameter2}{j5}"
                                        passwords68 = f"{j1}{j2}{Parameter1.capitalize()}{j3}{j4}{j5}{Parameter2}"
                                        passwords69 = f"{j1}{j2}{Parameter2.capitalize()}{Parameter1}{j3}{j4}{j5}"
                                        passwords70 = f"{j1}{j2}{Parameter2.capitalize()}{j3}{Parameter1}{j4}{j5}"
                                        passwords71 = f"{j1}{j2}{Parameter2.capitalize()}{j3}{j4}{Parameter1}{j5}"
                                        passwords72 = f"{j1}{j2}{Parameter2.capitalize()}{j3}{j4}{j5}{Parameter1}"
                                        passwords73 = f"{j1}{j2}{j3}{Parameter1.capitalize()}{Parameter2}{j4}{j5}"
                                        passwords74 = f"{j1}{j2}{j3}{Parameter1.capitalize()}{j4}{Parameter2}{j5}"
                                        passwords75 = f"{j1}{j2}{j3}{Parameter1.capitalize()}{j4}{j5}{Parameter2}"
                                        passwords76 = f"{j1}{j2}{j3}{Parameter2.capitalize()}{Parameter1}{j4}{j5}"
                                        passwords77 = f"{j1}{j2}{j3}{Parameter2.capitalize()}{j4}{Parameter1}{j5}"
                                        passwords78 = f"{j1}{j2}{j3}{Parameter2.capitalize()}{j4}{j5}{Parameter1}"
                                        passwords79 = f"{j1}{j2}{j3}{j4}{Parameter1.capitalize()}{Parameter2}{j5}"
                                        passwords80 = f"{j1}{j2}{j3}{j4}{Parameter1.capitalize()}{j5}{Parameter2}"
                                        passwords81 = f"{j1}{j2}{j3}{j4}{Parameter2.capitalize()}{Parameter1}{j5}"
                                        passwords82 = f"{j1}{j2}{j3}{j4}{Parameter2.capitalize()}{j5}{Parameter1}"
                                        passwords83 = f"{j1}{j2}{j3}{j4}{j5}{Parameter1.capitalize()}{Parameter2}"
                                        passwords84 = f"{j1}{j2}{j3}{j4}{j5}{Parameter2.capitalize()}{Parameter1}"                                        
                                        print(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' +passwords4 + '\n' + passwords5 + '\n' + passwords6 + '\n' + passwords7 + '\n' + passwords8 + '\n' + passwords9 + '\n' + passwords10 + '\n'+ passwords11 + '\n'+ passwords12 + '\n' + passwords13 + '\n' + passwords14 + '\n' + passwords15 + '\n'+ passwords16 + '\n'+ passwords17 + '\n' + passwords18 + '\n'+ passwords19 + '\n'+ passwords20 + '\n' +passwords21 + '\n' + passwords22 + '\n' + passwords23 + '\n' + passwords24 + '\n' + passwords25 + '\n' + passwords26 + '\n' + passwords27 + '\n'+ passwords28 + '\n'+ passwords29 + '\n' + passwords30 + '\n' + passwords31 + '\n' + passwords32 + '\n'+ passwords33 + '\n'+ passwords34 + '\n'+ passwords35 + '\n'+ passwords36 + '\n'+ passwords37 + '\n'+ passwords38 + '\n' +passwords39 + '\n' + passwords40 + '\n' + passwords41 + '\n' + passwords42 + '\n' + passwords43 + '\n' + passwords44 + '\n' + passwords45 + '\n'+ passwords46 + '\n'+ passwords47 + '\n' + passwords48 + '\n' + passwords49 + '\n' + passwords50 + '\n'+ passwords51 + '\n'+ passwords52 + '\n' + passwords53 + '\n'+ passwords54 + '\n'+ passwords55 + '\n' +passwords56 + '\n' + passwords57 + '\n' + passwords58 + '\n' + passwords59 + '\n' + passwords60 + '\n'+ passwords61 + '\n' + passwords62 + '\n' + passwords63 + '\n' + passwords64 + '\n'+ passwords65 + '\n'+ passwords66 + '\n' + passwords67 + '\n'+ passwords68 + '\n'+ passwords69 + '\n' +passwords70 + '\n' + passwords71 + '\n' + passwords72 + '\n' + passwords73 + '\n' + passwords74 + '\n' + passwords75 + '\n' + passwords76 + '\n' + passwords77 + '\n' + passwords78 + '\n'+ passwords79 + '\n'+ passwords80 + '\n' + passwords81 + '\n'+ passwords82 + '\n'+ passwords83 + '\n' +passwords84 + '\n' )
                                        f.write(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' +passwords4 + '\n' + passwords5 + '\n' + passwords6 + '\n' + passwords7 + '\n' + passwords8 + '\n' + passwords9 + '\n' + passwords10 + '\n'+ passwords11 + '\n'+ passwords12 + '\n' + passwords13 + '\n' + passwords14 + '\n' + passwords15 + '\n'+ passwords16 + '\n'+ passwords17 + '\n' + passwords18 + '\n'+ passwords19 + '\n'+ passwords20 + '\n' +passwords21 + '\n' + passwords22 + '\n' + passwords23 + '\n' + passwords24 + '\n' + passwords25 + '\n' + passwords26 + '\n' + passwords27 + '\n'+ passwords28 + '\n'+ passwords29 + '\n' + passwords30 + '\n' + passwords31 + '\n' + passwords32 + '\n'+ passwords33 + '\n'+ passwords34 + '\n'+ passwords35 + '\n'+ passwords36 + '\n'+ passwords37 + '\n'+ passwords38 + '\n' +passwords39 + '\n' + passwords40 + '\n' + passwords41 + '\n' + passwords42 + '\n' + passwords43 + '\n' + passwords44 + '\n' + passwords45 + '\n'+ passwords46 + '\n'+ passwords47 + '\n' + passwords48 + '\n' + passwords49 + '\n' + passwords50 + '\n'+ passwords51 + '\n'+ passwords52 + '\n' + passwords53 + '\n'+ passwords54 + '\n'+ passwords55 + '\n' +passwords56 + '\n' + passwords57 + '\n' + passwords58 + '\n' + passwords59 + '\n' + passwords60 + '\n'+ passwords61 + '\n' + passwords62 + '\n' + passwords63 + '\n' + passwords64 + '\n'+ passwords65 + '\n'+ passwords66 + '\n' + passwords67 + '\n'+ passwords68 + '\n'+ passwords69 + '\n' +passwords70 + '\n' + passwords71 + '\n' + passwords72 + '\n' + passwords73 + '\n' + passwords74 + '\n' + passwords75 + '\n' + passwords76 + '\n' + passwords77 + '\n' + passwords78 + '\n'+ passwords79 + '\n'+ passwords80 + '\n' + passwords81 + '\n'+ passwords82 + '\n'+ passwords83 + '\n' +passwords84 + '\n' )
        if mpar == 1:
            print("not now")
    elif add3 == 6 :
        if mpar == 0:
            if lowercap == 0:
                for j1 in selected_list:
                    for j2 in selected_list:
                        for j3 in selected_list:
                            for j4 in selected_list:
                                for j5 in selected_list:
                                    for j6 in selected_list:
                                        with open(filename + ".txt", 'a') as f:
                                            passwords1 = f"{Parameter1}{Parameter2}{j1}{j2}{j3}{j4}{j5}{j6}"
                                            passwords2 = f"{Parameter1}{j1}{Parameter2}{j2}{j3}{j4}{j5}{j6}"
                                            passwords3 = f"{Parameter1}{j1}{j2}{Parameter2}{j3}{j4}{j5}{j6}"
                                            passwords4 = f"{Parameter1}{j1}{j2}{j3}{Parameter2}{j4}{j5}{j6}"
                                            passwords5 = f"{Parameter1}{j1}{j2}{j3}{j4}{Parameter2}{j5}{j6}"
                                            passwords6 = f"{Parameter1}{j1}{j2}{j3}{j4}{j5}{Parameter2}{j6}"
                                            passwords7 = f"{Parameter1}{j1}{j2}{j3}{j4}{j5}{j6}{Parameter2}"
                                            passwords8 = f"{Parameter2}{Parameter1}{j1}{j2}{j3}{j4}{j5}{j6}"
                                            passwords9 = f"{Parameter2}{j1}{Parameter1}{j2}{j3}{j4}{j5}{j6}"
                                            passwords10 = f"{Parameter2}{j1}{j2}{Parameter1}{j3}{j4}{j5}{j6}"
                                            passwords11 = f"{Parameter2}{j1}{j2}{j3}{Parameter1}{j4}{j5}{j6}"
                                            passwords12 = f"{Parameter2}{j1}{j2}{j3}{j4}{Parameter1}{j5}{j6}"
                                            passwords13 = f"{Parameter2}{j1}{j2}{j3}{j4}{j5}{Parameter1}{j6}"
                                            passwords14 = f"{Parameter2}{j1}{j2}{j3}{j4}{j5}{j6}{Parameter1}"
                                            passwords15 = f"{j1}{Parameter1}{Parameter2}{j2}{j3}{j4}{j5}{j6}"
                                            passwords16 = f"{j1}{Parameter1}{j2}{Parameter2}{j3}{j4}{j5}{j6}"
                                            passwords17 = f"{j1}{Parameter1}{j2}{j3}{Parameter2}{j4}{j5}{j6}"
                                            passwords18 = f"{j1}{Parameter1}{j2}{j3}{j4}{Parameter2}{j5}{j6}"
                                            passwords19 = f"{j1}{Parameter1}{j2}{j3}{j4}{j5}{Parameter2}{j6}"
                                            passwords20 = f"{j1}{Parameter1}{j2}{j3}{j4}{j5}{j6}{Parameter2}"
                                            passwords21 = f"{j1}{Parameter2}{Parameter1}{j2}{j3}{j4}{j5}{j6}"
                                            passwords22 = f"{j1}{Parameter2}{j2}{Parameter1}{j3}{j4}{j5}{j6}"
                                            passwords23 = f"{j1}{Parameter2}{j2}{j3}{Parameter1}{j4}{j5}{j6}"
                                            passwords24 = f"{j1}{Parameter2}{j2}{j3}{j4}{Parameter1}{j5}{j6}"
                                            passwords25 = f"{j1}{Parameter2}{j2}{j3}{j4}{j5}{Parameter1}{j6}"
                                            passwords26 = f"{j1}{Parameter2}{j2}{j3}{j4}{j5}{j6}{Parameter1}"
                                            passwords27 = f"{j1}{j2}{Parameter1}{Parameter2}{j3}{j4}{j5}{j6}"
                                            passwords28 = f"{j1}{j2}{Parameter1}{j3}{Parameter2}{j4}{j5}{j6}"
                                            passwords29 = f"{j1}{j2}{Parameter1}{j3}{j4}{Parameter2}{j5}{j6}"
                                            passwords30 = f"{j1}{j2}{Parameter1}{j3}{j4}{j5}{Parameter2}{j6}"
                                            passwords31 = f"{j1}{j2}{Parameter1}{j3}{j4}{j5}{j6}{Parameter2}"
                                            passwords32 = f"{j1}{j2}{Parameter2}{Parameter1}{j3}{j4}{j5}{j6}"
                                            passwords33 = f"{j1}{j2}{Parameter2}{j3}{Parameter1}{j4}{j5}{j6}"
                                            passwords34 = f"{j1}{j2}{Parameter2}{j3}{j4}{Parameter1}{j5}{j6}"
                                            passwords35 = f"{j1}{j2}{Parameter2}{j3}{j4}{j5}{Parameter1}{j6}"
                                            passwords36 = f"{j1}{j2}{Parameter2}{j3}{j4}{j5}{j6}{Parameter1}"
                                            passwords37 = f"{j1}{j2}{j3}{Parameter1}{Parameter2}{j4}{j5}{j6}"
                                            passwords38 = f"{j1}{j2}{j3}{Parameter1}{j4}{Parameter2}{j5}{j6}"
                                            passwords39 = f"{j1}{j2}{j3}{Parameter1}{j4}{j5}{Parameter2}{j6}"
                                            passwords40 = f"{j1}{j2}{j3}{Parameter1}{j4}{j5}{j6}{Parameter2}"
                                            passwords41 = f"{j1}{j2}{j3}{Parameter2}{Parameter1}{j4}{j5}{j6}"
                                            passwords42 = f"{j1}{j2}{j3}{Parameter2}{j4}{Parameter1}{j5}{j6}"
                                            passwords43 = f"{j1}{j2}{j3}{Parameter2}{j4}{j5}{Parameter1}{j6}"
                                            passwords44 = f"{j1}{j2}{j3}{Parameter2}{j4}{j5}{j6}{Parameter1}"
                                            passwords45 = f"{j1}{j2}{j3}{j4}{Parameter1}{Parameter2}{j5}{j6}"
                                            passwords46 = f"{j1}{j2}{j3}{j4}{Parameter1}{j5}{Parameter2}{j6}"
                                            passwords47 = f"{j1}{j2}{j3}{j4}{Parameter1}{j5}{j6}{Parameter2}"
                                            passwords48 = f"{j1}{j2}{j3}{j4}{Parameter2}{Parameter1}{j5}{j6}"
                                            passwords49 = f"{j1}{j2}{j3}{j4}{Parameter2}{j5}{Parameter1}{j6}"
                                            passwords50 = f"{j1}{j2}{j3}{j4}{Parameter2}{j5}{j6}{Parameter1}"
                                            passwords51 = f"{j1}{j2}{j3}{j4}{j5}{Parameter1}{Parameter2}{j6}"
                                            passwords52 = f"{j1}{j2}{j3}{j4}{j5}{Parameter1}{j6}{Parameter2}"
                                            passwords53 = f"{j1}{j2}{j3}{j4}{j5}{Parameter2}{Parameter1}{j6}"
                                            passwords54 = f"{j1}{j2}{j3}{j4}{j5}{Parameter2}{j6}{Parameter1}"
                                            passwords55 = f"{j1}{j2}{j3}{j4}{j5}{j6}{Parameter1}{Parameter2}"
                                            passwords56 = f"{j1}{j2}{j3}{j4}{j5}{j6}{Parameter2}{Parameter1}"
                                            print(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' +passwords4 + '\n' + passwords5 + '\n' + passwords6 + '\n' + passwords7 + '\n' + passwords8 + '\n' + passwords9 + '\n' + passwords10 + '\n'+ passwords11 + '\n'+ passwords12 + '\n' + passwords13 + '\n' + passwords14 + '\n' + passwords15 + '\n'+ passwords16 + '\n'+ passwords17 + '\n'+ passwords18 + '\n'+ passwords19 + '\n' + passwords20 + '\n' + passwords21 + '\n'+ passwords22 + '\n'+ passwords23 + '\n' + passwords24 + '\n' + passwords25 + '\n' + passwords26 + '\n'+ passwords27 + '\n'+ passwords28 +'\n'+ passwords29 + '\n'+ passwords30 + '\n'+ passwords31 + '\n'+ passwords32 + '\n' +passwords33 + '\n' + passwords34 + '\n' + passwords35 + '\n' + passwords36 + '\n' + passwords37 + '\n' + passwords38 + '\n' + passwords39 + '\n'+ passwords40 + '\n'+ passwords41 + '\n' + passwords42 + '\n'+ passwords43 + '\n'+ passwords44 +'\n'+ passwords45 + '\n'+ passwords46 + '\n'+ passwords47 + '\n'+ passwords48 + '\n' +passwords49 + '\n' + passwords50 + '\n' + passwords51 + '\n' + passwords52 + '\n' + passwords53 + '\n' + passwords54 + '\n' + passwords55 + '\n'+ passwords56 + '\n' )
                                            f.write(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' +passwords4 + '\n' + passwords5 + '\n' + passwords6 + '\n' + passwords7 + '\n' + passwords8 + '\n' + passwords9 + '\n' + passwords10 + '\n'+ passwords11 + '\n'+ passwords12 + '\n' + passwords13 + '\n' + passwords14 + '\n' + passwords15 + '\n'+ passwords16 + '\n'+ passwords17 + '\n'+ passwords18 + '\n'+ passwords19 + '\n' + passwords20 + '\n' + passwords21 + '\n'+ passwords22 + '\n'+ passwords23 + '\n' + passwords24 + '\n' + passwords25 + '\n' + passwords26 + '\n'+ passwords27 + '\n'+ passwords28 +'\n'+ passwords29 + '\n'+ passwords30 + '\n'+ passwords31 + '\n'+ passwords32 + '\n' +passwords33 + '\n' + passwords34 + '\n' + passwords35 + '\n' + passwords36 + '\n' + passwords37 + '\n' + passwords38 + '\n' + passwords39 + '\n'+ passwords40 + '\n'+ passwords41 + '\n' + passwords42 + '\n'+ passwords43 + '\n'+ passwords44 +'\n'+ passwords45 + '\n'+ passwords46 + '\n'+ passwords47 + '\n'+ passwords48 + '\n' +passwords49 + '\n' + passwords50 + '\n' + passwords51 + '\n' + passwords52 + '\n' + passwords53 + '\n' + passwords54 + '\n' + passwords55 + '\n'+ passwords56 + '\n' )
            if lowercap == 1 :
                for j1 in selected_list:
                    for j2 in selected_list:
                        for j3 in selected_list:
                            for j4 in selected_list:
                                for j5 in selected_list:
                                    for j6 in selected_list:
                                        with open(filename + ".txt", 'a') as f:
                                            passwords1 = f"{Parameter1}{Parameter2}{j1}{j2}{j3}{j4}{j5}{j6}"
                                            passwords2 = f"{Parameter1}{j1}{Parameter2}{j2}{j3}{j4}{j5}{j6}"
                                            passwords3 = f"{Parameter1}{j1}{j2}{Parameter2}{j3}{j4}{j5}{j6}"
                                            passwords4 = f"{Parameter1}{j1}{j2}{j3}{Parameter2}{j4}{j5}{j6}"
                                            passwords5 = f"{Parameter1}{j1}{j2}{j3}{j4}{Parameter2}{j5}{j6}"
                                            passwords6 = f"{Parameter1}{j1}{j2}{j3}{j4}{j5}{Parameter2}{j6}"
                                            passwords7 = f"{Parameter1}{j1}{j2}{j3}{j4}{j5}{j6}{Parameter2}"
                                            passwords8 = f"{Parameter2}{Parameter1}{j1}{j2}{j3}{j4}{j5}{j6}"
                                            passwords9 = f"{Parameter2}{j1}{Parameter1}{j2}{j3}{j4}{j5}{j6}"
                                            passwords10 = f"{Parameter2}{j1}{j2}{Parameter1}{j3}{j4}{j5}{j6}"
                                            passwords11 = f"{Parameter2}{j1}{j2}{j3}{Parameter1}{j4}{j5}{j6}"
                                            passwords12 = f"{Parameter2}{j1}{j2}{j3}{j4}{Parameter1}{j5}{j6}"
                                            passwords13 = f"{Parameter2}{j1}{j2}{j3}{j4}{j5}{Parameter1}{j6}"
                                            passwords14 = f"{Parameter2}{j1}{j2}{j3}{j4}{j5}{j6}{Parameter1}"
                                            passwords15 = f"{j1}{Parameter1}{Parameter2}{j2}{j3}{j4}{j5}{j6}"
                                            passwords16 = f"{j1}{Parameter1}{j2}{Parameter2}{j3}{j4}{j5}{j6}"
                                            passwords17 = f"{j1}{Parameter1}{j2}{j3}{Parameter2}{j4}{j5}{j6}"
                                            passwords18 = f"{j1}{Parameter1}{j2}{j3}{j4}{Parameter2}{j5}{j6}"
                                            passwords19 = f"{j1}{Parameter1}{j2}{j3}{j4}{j5}{Parameter2}{j6}"
                                            passwords20 = f"{j1}{Parameter1}{j2}{j3}{j4}{j5}{j6}{Parameter2}"
                                            passwords21 = f"{j1}{Parameter2}{Parameter1}{j2}{j3}{j4}{j5}{j6}"
                                            passwords22 = f"{j1}{Parameter2}{j2}{Parameter1}{j3}{j4}{j5}{j6}"
                                            passwords23 = f"{j1}{Parameter2}{j2}{j3}{Parameter1}{j4}{j5}{j6}"
                                            passwords24 = f"{j1}{Parameter2}{j2}{j3}{j4}{Parameter1}{j5}{j6}"
                                            passwords25 = f"{j1}{Parameter2}{j2}{j3}{j4}{j5}{Parameter1}{j6}"
                                            passwords26 = f"{j1}{Parameter2}{j2}{j3}{j4}{j5}{j6}{Parameter1}"
                                            passwords27 = f"{j1}{j2}{Parameter1}{Parameter2}{j3}{j4}{j5}{j6}"
                                            passwords28 = f"{j1}{j2}{Parameter1}{j3}{Parameter2}{j4}{j5}{j6}"
                                            passwords29 = f"{j1}{j2}{Parameter1}{j3}{j4}{Parameter2}{j5}{j6}"
                                            passwords30 = f"{j1}{j2}{Parameter1}{j3}{j4}{j5}{Parameter2}{j6}"
                                            passwords31 = f"{j1}{j2}{Parameter1}{j3}{j4}{j5}{j6}{Parameter2}"
                                            passwords32 = f"{j1}{j2}{Parameter2}{Parameter1}{j3}{j4}{j5}{j6}"
                                            passwords33 = f"{j1}{j2}{Parameter2}{j3}{Parameter1}{j4}{j5}{j6}"
                                            passwords34 = f"{j1}{j2}{Parameter2}{j3}{j4}{Parameter1}{j5}{j6}"
                                            passwords35 = f"{j1}{j2}{Parameter2}{j3}{j4}{j5}{Parameter1}{j6}"
                                            passwords36 = f"{j1}{j2}{Parameter2}{j3}{j4}{j5}{j6}{Parameter1}"
                                            passwords37 = f"{j1}{j2}{j3}{Parameter1}{Parameter2}{j4}{j5}{j6}"
                                            passwords38 = f"{j1}{j2}{j3}{Parameter1}{j4}{Parameter2}{j5}{j6}"
                                            passwords39 = f"{j1}{j2}{j3}{Parameter1}{j4}{j5}{Parameter2}{j6}"
                                            passwords40 = f"{j1}{j2}{j3}{Parameter1}{j4}{j5}{j6}{Parameter2}"
                                            passwords41 = f"{j1}{j2}{j3}{Parameter2}{Parameter1}{j4}{j5}{j6}"
                                            passwords42 = f"{j1}{j2}{j3}{Parameter2}{j4}{Parameter1}{j5}{j6}"
                                            passwords43 = f"{j1}{j2}{j3}{Parameter2}{j4}{j5}{Parameter1}{j6}"
                                            passwords44 = f"{j1}{j2}{j3}{Parameter2}{j4}{j5}{j6}{Parameter1}"
                                            passwords45 = f"{j1}{j2}{j3}{j4}{Parameter1}{Parameter2}{j5}{j6}"
                                            passwords46 = f"{j1}{j2}{j3}{j4}{Parameter1}{j5}{Parameter2}{j6}"
                                            passwords47 = f"{j1}{j2}{j3}{j4}{Parameter1}{j5}{j6}{Parameter2}"
                                            passwords48 = f"{j1}{j2}{j3}{j4}{Parameter2}{Parameter1}{j5}{j6}"
                                            passwords49 = f"{j1}{j2}{j3}{j4}{Parameter2}{j5}{Parameter1}{j6}"
                                            passwords50 = f"{j1}{j2}{j3}{j4}{Parameter2}{j5}{j6}{Parameter1}"
                                            passwords51 = f"{j1}{j2}{j3}{j4}{j5}{Parameter1}{Parameter2}{j6}"
                                            passwords52 = f"{j1}{j2}{j3}{j4}{j5}{Parameter1}{j6}{Parameter2}"
                                            passwords53 = f"{j1}{j2}{j3}{j4}{j5}{Parameter2}{Parameter1}{j6}"
                                            passwords54 = f"{j1}{j2}{j3}{j4}{j5}{Parameter2}{j6}{Parameter1}"
                                            passwords55 = f"{j1}{j2}{j3}{j4}{j5}{j6}{Parameter1}{Parameter2}"
                                            passwords56 = f"{j1}{j2}{j3}{j4}{j5}{j6}{Parameter2}{Parameter1}"
                                            passwords57 = f"{Parameter1.capitalize()}{Parameter2}{j1}{j2}{j3}{j4}{j5}{j6}"
                                            passwords58 = f"{Parameter1.capitalize()}{j1}{Parameter2}{j2}{j3}{j4}{j5}{j6}"
                                            passwords59 = f"{Parameter1.capitalize()}{j1}{j2}{Parameter2}{j3}{j4}{j5}{j6}"
                                            passwords60 = f"{Parameter1.capitalize()}{j1}{j2}{j3}{Parameter2}{j4}{j5}{j6}"
                                            passwords61 = f"{Parameter1.capitalize()}{j1}{j2}{j3}{j4}{Parameter2}{j5}{j6}"
                                            passwords62 = f"{Parameter1.capitalize()}{j1}{j2}{j3}{j4}{j5}{Parameter2}{j6}"
                                            passwords63 = f"{Parameter1.capitalize()}{j1}{j2}{j3}{j4}{j5}{j6}{Parameter2}"
                                            passwords64 = f"{Parameter2.capitalize()}{Parameter1}{j1}{j2}{j3}{j4}{j5}{j6}"
                                            passwords65 = f"{Parameter2.capitalize()}{j1}{Parameter1}{j2}{j3}{j4}{j5}{j6}"
                                            passwords66 = f"{Parameter2.capitalize()}{j1}{j2}{Parameter1}{j3}{j4}{j5}{j6}"
                                            passwords67 = f"{Parameter2.capitalize()}{j1}{j2}{j3}{Parameter1}{j4}{j5}{j6}"
                                            passwords68 = f"{Parameter2.capitalize()}{j1}{j2}{j3}{j4}{Parameter1}{j5}{j6}"
                                            passwords69 = f"{Parameter2.capitalize()}{j1}{j2}{j3}{j4}{j5}{Parameter1}{j6}"
                                            passwords70 = f"{Parameter2.capitalize()}{j1}{j2}{j3}{j4}{j5}{j6}{Parameter1}"
                                            passwords71 = f"{j1}{Parameter1.capitalize()}{Parameter2}{j2}{j3}{j4}{j5}{j6}"
                                            passwords72 = f"{j1}{Parameter1.capitalize()}{j2}{Parameter2}{j3}{j4}{j5}{j6}"
                                            passwords73 = f"{j1}{Parameter1.capitalize()}{j2}{j3}{Parameter2}{j4}{j5}{j6}"
                                            passwords74 = f"{j1}{Parameter1.capitalize()}{j2}{j3}{j4}{Parameter2}{j5}{j6}"
                                            passwords75 = f"{j1}{Parameter1.capitalize()}{j2}{j3}{j4}{j5}{Parameter2}{j6}"
                                            passwords76 = f"{j1}{Parameter1.capitalize()}{j2}{j3}{j4}{j5}{j6}{Parameter2}"
                                            passwords77 = f"{j1}{Parameter2.capitalize()}{Parameter1}{j2}{j3}{j4}{j5}{j6}"
                                            passwords78 = f"{j1}{Parameter2.capitalize()}{j2}{Parameter1}{j3}{j4}{j5}{j6}"
                                            passwords79 = f"{j1}{Parameter2.capitalize()}{j2}{j3}{Parameter1}{j4}{j5}{j6}"
                                            passwords80 = f"{j1}{Parameter2.capitalize()}{j2}{j3}{j4}{Parameter1}{j5}{j6}"
                                            passwords81 = f"{j1}{Parameter2.capitalize()}{j2}{j3}{j4}{j5}{Parameter1}{j6}"
                                            passwords82 = f"{j1}{Parameter2.capitalize()}{j2}{j3}{j4}{j5}{j6}{Parameter1}"
                                            passwords83 = f"{j1}{j2}{Parameter1.capitalize()}{Parameter2}{j3}{j4}{j5}{j6}"
                                            passwords84 = f"{j1}{j2}{Parameter1.capitalize()}{j3}{Parameter2}{j4}{j5}{j6}"
                                            passwords85 = f"{j1}{j2}{Parameter1.capitalize()}{j3}{j4}{Parameter2}{j5}{j6}"
                                            passwords86 = f"{j1}{j2}{Parameter1.capitalize()}{j3}{j4}{j5}{Parameter2}{j6}"
                                            passwords87 = f"{j1}{j2}{Parameter1.capitalize()}{j3}{j4}{j5}{j6}{Parameter2}"
                                            passwords88 = f"{j1}{j2}{Parameter2.capitalize()}{Parameter1}{j3}{j4}{j5}{j6}"
                                            passwords89 = f"{j1}{j2}{Parameter2.capitalize()}{j3}{Parameter1}{j4}{j5}{j6}"
                                            passwords90 = f"{j1}{j2}{Parameter2.capitalize()}{j3}{j4}{Parameter1}{j5}{j6}"
                                            passwords91 = f"{j1}{j2}{Parameter2.capitalize()}{j3}{j4}{j5}{Parameter1}{j6}"
                                            passwords92 = f"{j1}{j2}{Parameter2.capitalize()}{j3}{j4}{j5}{j6}{Parameter1}"
                                            passwords93 = f"{j1}{j2}{j3}{Parameter1.capitalize()}{Parameter2}{j4}{j5}{j6}"
                                            passwords94 = f"{j1}{j2}{j3}{Parameter1.capitalize()}{j4}{Parameter2}{j5}{j6}"
                                            passwords95 = f"{j1}{j2}{j3}{Parameter1.capitalize()}{j4}{j5}{Parameter2}{j6}"
                                            passwords96 = f"{j1}{j2}{j3}{Parameter1.capitalize()}{j4}{j5}{j6}{Parameter2}"
                                            passwords97 = f"{j1}{j2}{j3}{Parameter2.capitalize()}{Parameter1}{j4}{j5}{j6}"
                                            passwords98 = f"{j1}{j2}{j3}{Parameter2.capitalize()}{j4}{Parameter1}{j5}{j6}"
                                            passwords99 = f"{j1}{j2}{j3}{Parameter2.capitalize()}{j4}{j5}{Parameter1}{j6}"
                                            passwords100 = f"{j1}{j2}{j3}{Parameter2.capitalize()}{j4}{j5}{j6}{Parameter1}"
                                            passwords101 = f"{j1}{j2}{j3}{j4}{Parameter1.capitalize()}{Parameter2}{j5}{j6}"
                                            passwords102 = f"{j1}{j2}{j3}{j4}{Parameter1.capitalize()}{j5}{Parameter2}{j6}"
                                            passwords103 = f"{j1}{j2}{j3}{j4}{Parameter1.capitalize()}{j5}{j6}{Parameter2}"
                                            passwords104 = f"{j1}{j2}{j3}{j4}{Parameter2.capitalize()}{Parameter1}{j5}{j6}"
                                            passwords105 = f"{j1}{j2}{j3}{j4}{Parameter2.capitalize()}{j5}{Parameter1}{j6}"
                                            passwords106 = f"{j1}{j2}{j3}{j4}{Parameter2.capitalize()}{j5}{j6}{Parameter1}"
                                            passwords107 = f"{j1}{j2}{j3}{j4}{j5}{Parameter1.capitalize()}{Parameter2}{j6}"
                                            passwords108 = f"{j1}{j2}{j3}{j4}{j5}{Parameter1.capitalize()}{j6}{Parameter2}"
                                            passwords109 = f"{j1}{j2}{j3}{j4}{j5}{Parameter2.capitalize()}{Parameter1}{j6}"
                                            passwords110 = f"{j1}{j2}{j3}{j4}{j5}{Parameter2.capitalize()}{j6}{Parameter1}"
                                            passwords111 = f"{j1}{j2}{j3}{j4}{j5}{j6}{Parameter1.capitalize()}{Parameter2}"
                                            passwords112 = f"{j1}{j2}{j3}{j4}{j5}{j6}{Parameter2.capitalize()}{Parameter1}"                                                                             
                                            print(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' +passwords4 + '\n' + passwords5 + '\n' + passwords6 + '\n' + passwords7 + '\n' + passwords8 + '\n' + passwords9 + '\n' + passwords10 + '\n'+ passwords11 + '\n'+ passwords12 + '\n' + passwords13 + '\n' + passwords14 + '\n' + passwords15 + '\n'+ passwords16 + '\n'+ passwords17 + '\n' + passwords18 + '\n'+ passwords19 + '\n'+ passwords20 + '\n' +passwords21 + '\n' + passwords22 + '\n' + passwords23 + '\n' + passwords24 + '\n' + passwords25 + '\n' + passwords26 + '\n' + passwords27 + '\n'+ passwords28 + '\n'+ passwords29 + '\n' + passwords30 + '\n' + passwords31 + '\n' + passwords32 + '\n'+ passwords33 + '\n'+ passwords34 + '\n'+ passwords35 + '\n'+ passwords36 + '\n'+ passwords37 + '\n'+ passwords38 + '\n' +passwords39 + '\n' + passwords40 + '\n' + passwords41 + '\n' + passwords42 + '\n' + passwords43 + '\n' + passwords44 + '\n' + passwords45 + '\n'+ passwords46 + '\n'+ passwords47 + '\n' + passwords48 + '\n' + passwords49 + '\n' + passwords50 + '\n'+ passwords51 + '\n'+ passwords52 + '\n' + passwords53 + '\n'+ passwords54 + '\n'+ passwords55 + '\n' +passwords56 + '\n' + passwords57 + '\n' + passwords58 + '\n' + passwords59 + '\n' + passwords60 + '\n'+ passwords61 + '\n' + passwords62 + '\n' + passwords63 + '\n' + passwords64 + '\n'+ passwords65 + '\n'+ passwords66 + '\n' + passwords67 + '\n'+ passwords68 + '\n'+ passwords69 + '\n' +passwords70 + '\n' + passwords71 + '\n' + passwords72 + '\n' + passwords73 + '\n' + passwords74 + '\n' + passwords75 + '\n' + passwords76 + '\n' + passwords77 + '\n' + passwords78 + '\n'+ passwords79 + '\n'+ passwords80 + '\n' + passwords81 + '\n'+ passwords82 + '\n'+ passwords83 + '\n' +passwords84 + '\n' + passwords85 + '\n' + passwords86 + '\n' + passwords87 + '\n'+ passwords88 + '\n'+ passwords89 + '\n' + passwords90 + '\n' + passwords91 + '\n' + passwords92 + '\n'+ passwords93 + '\n'+ passwords94 + '\n' + passwords95 + '\n'+ passwords96 + '\n'+ passwords97 + '\n' +passwords98 + '\n' + passwords99 + '\n' + passwords100 + '\n' + passwords101 + '\n' + passwords102 + '\n' + passwords103 + '\n' + passwords104 + '\n'+ passwords105 + '\n'+ passwords106 + '\n' + passwords107 + '\n' + passwords108 + '\n' + passwords109 + '\n'+ passwords110 + '\n'+ passwords111 + '\n'+ passwords112 + '\n')
                                            f.write(passwords1 + '\n'+ passwords2 + '\n'+ passwords3 + '\n' +passwords4 + '\n' + passwords5 + '\n' + passwords6 + '\n' + passwords7 + '\n' + passwords8 + '\n' + passwords9 + '\n' + passwords10 + '\n'+ passwords11 + '\n'+ passwords12 + '\n' + passwords13 + '\n' + passwords14 + '\n' + passwords15 + '\n'+ passwords16 + '\n'+ passwords17 + '\n' + passwords18 + '\n'+ passwords19 + '\n'+ passwords20 + '\n' +passwords21 + '\n' + passwords22 + '\n' + passwords23 + '\n' + passwords24 + '\n' + passwords25 + '\n' + passwords26 + '\n' + passwords27 + '\n'+ passwords28 + '\n'+ passwords29 + '\n' + passwords30 + '\n' + passwords31 + '\n' + passwords32 + '\n'+ passwords33 + '\n'+ passwords34 + '\n'+ passwords35 + '\n'+ passwords36 + '\n'+ passwords37 + '\n'+ passwords38 + '\n' +passwords39 + '\n' + passwords40 + '\n' + passwords41 + '\n' + passwords42 + '\n' + passwords43 + '\n' + passwords44 + '\n' + passwords45 + '\n'+ passwords46 + '\n'+ passwords47 + '\n' + passwords48 + '\n' + passwords49 + '\n' + passwords50 + '\n'+ passwords51 + '\n'+ passwords52 + '\n' + passwords53 + '\n'+ passwords54 + '\n'+ passwords55 + '\n' +passwords56 + '\n' + passwords57 + '\n' + passwords58 + '\n' + passwords59 + '\n' + passwords60 + '\n'+ passwords61 + '\n' + passwords62 + '\n' + passwords63 + '\n' + passwords64 + '\n'+ passwords65 + '\n'+ passwords66 + '\n' + passwords67 + '\n'+ passwords68 + '\n'+ passwords69 + '\n' +passwords70 + '\n' + passwords71 + '\n' + passwords72 + '\n' + passwords73 + '\n' + passwords74 + '\n' + passwords75 + '\n' + passwords76 + '\n' + passwords77 + '\n' + passwords78 + '\n'+ passwords79 + '\n'+ passwords80 + '\n' + passwords81 + '\n'+ passwords82 + '\n'+ passwords83 + '\n' +passwords84 + '\n' + passwords85 + '\n' + passwords86 + '\n' + passwords87 + '\n'+ passwords88 + '\n'+ passwords89 + '\n' + passwords90 + '\n' + passwords91 + '\n' + passwords92 + '\n'+ passwords93 + '\n'+ passwords94 + '\n' + passwords95 + '\n'+ passwords96 + '\n'+ passwords97 + '\n' +passwords98 + '\n' + passwords99 + '\n' + passwords100 + '\n' + passwords101 + '\n' + passwords102 + '\n' + passwords103 + '\n' + passwords104 + '\n'+ passwords105 + '\n'+ passwords106 + '\n' + passwords107 + '\n' + passwords108 + '\n' + passwords109 + '\n'+ passwords110 + '\n'+ passwords111 + '\n'+ passwords112 + '\n')
        if mpar == 1:
            print("not now")
    else:
        print("not now")
print("The process ended successfully")
#I cant code anymore, I will do clean one next project.
