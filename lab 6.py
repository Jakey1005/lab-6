#Jake Cavanagh encoding project

#Runs program
def main():
    while True:
        display_menu()
        option = input("Please enter an option: ")
      #Takes in password and encodes it
        if option == "1":
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
            print("")
            encoded_password = encode(password)
      #Prints both password and encoded password
        if option == "2":
            decoded_password = decoder(encoded_password)
            print("The encoded password is " + encoded_password + ", and the original password is " + decoded_password + ".")
            print("")
      #Ends loop
        if option == "3":
            break

#Displays menu
def display_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print("")

#Encodes password
def encode(num):
    result = ""
    for i in range(len(str(num))):
        # when num is > 8, it prints 11, rather than 1, must use %10
        result += str(int(num[i]) + 3)
    return str(result)

# decode function
def decoder(num):
    result = ''
    for n in num:
        new_digit = str((int(n) - 3) % 10)
        result += new_digit
    return result

if __name__ == "__main__":
    main()
