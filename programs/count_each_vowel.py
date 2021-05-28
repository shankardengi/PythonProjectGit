if __name__=="__main__":
    data = input("Enter String:").casefold()
    vowels = "aeiou"
    dicts = {}.fromkeys(vowels,0)
    for ch in data:
        if ch in vowels:
            dicts[ch] +=1
    print(dicts)