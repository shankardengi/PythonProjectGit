if __name__=="__main__":
    string = input("Enter String Check Pallindrome Or Not:")
    if string == string[::-1]:
        print("String is pallindrome")
    else:
        print("String is not pallindrome")
