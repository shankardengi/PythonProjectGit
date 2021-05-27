if __name__ == "__main__":
    words = input("Enter words to sort :")
    words = [word.lower() for word in words.split(" ")]
    words.sort()
    print("Sorted words is :")
    print(words)