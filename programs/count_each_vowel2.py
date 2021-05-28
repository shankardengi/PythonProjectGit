if __name__=="__main__":
    data = input("Enter the data to check number of vowels:")
    vowels = "aeiou"
    result = {x : sum([1 for ch in data if ch == x])for x in vowels }
    print(result)