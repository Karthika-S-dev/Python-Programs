def has_unique_chars(s):
    # Standard ASCII has only 128 unique characters.
    if len(s) > 128:
        return False
     #Declaring an empty dictionary to track the frequency of characters   
    seen_chars = {}
    
    for char in s:
        #Character already present
        if seen_chars.get(char, 0) == 1:
            return False
        else:
            #Marking teh character as seen
            seen_chars[char] = seen_chars.get(char, 0) + 1
    return True  # All characters are unique

def main():
    InputString = input("Enter the string: ")
    result = has_unique_chars(InputString)
    print(f"Contains unique characters ? {result}")

main()