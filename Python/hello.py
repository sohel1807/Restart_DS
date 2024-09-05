def welcome(name):
    print(f"welcome{name}")

if __name__=="__main__":
    welcome("sohel")
#When the script is run, the code under the if __name__ == "__main__": 
#                block will only be executed if the script is the main program.
# If the script is imported as a module elsewhere, the code under that block won't run, 
# allowing the module's functions and classes to be imported without executing unnecessary code.
