try:
    n = int(input("Enter a number: "))
    for i in range(n):
        print(i)
except:
    print("Invalid input. Please enter a valid integer.")
#ValueError
#IndexError
#except Exception as e