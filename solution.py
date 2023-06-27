def firstUniqChar(s):
    freq = {}
    
    # Update frequencies
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    # Find the first non-repeating character
    for i in range(len(s)):
        if freq[s[i]] == 1:
            return i
    
    return -1
