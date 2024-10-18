def lengthOfLongestSubstring(s):
    # Initialize a set to store characters in the current window
    char_set = set()
    
    # Initialize two pointers and the maximum length
    left = 0
    max_len = 0
    
    # Iterate over the characters in the string with the right pointer
    for right in range(len(s)):
        # If the character at the right pointer is already in the set,
        # move the left pointer until we remove the duplicate
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Add the current character to the set
        char_set.add(s[right])
        
        # Update the maximum length of the substring
        max_len = max(max_len, right - left + 1)
    
    return max_len

# Taking input from the user
s = input("Enter a string: ")

# Calling the function and printing the result
result = lengthOfLongestSubstring(s)
print(f"The length of the longest substring without repeating characters is: {result}")

