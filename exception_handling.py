'''a = "hello"
# int(a)

phone = input("Enter your phone Number: ")
try:
    phone = int(phone)
    print(phone)
except ValueError:
    print("Enter valid Phone Number")
except BaseException as err:
    print(err)
else:
    print("Everything went well")
finally:
    print("Thank you")'''

# try, except, else, finally

