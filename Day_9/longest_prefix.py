def longestCommonPrefix(strs):
    if not strs:
        return ""
    
  
    prefix = strs[0]
    
   
    for s in strs[1:]:
        
        while not s.startswith(prefix):
           
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix

# Test cases
print(longestCommonPrefix(["flower", "flow", "flight"])) # Output: "fl"
print(longestCommonPrefix(["dog", "racecar", "car"]))    # Output: ""
print(longestCommonPrefix(["apple", "ape", "april"]))    # Output: "ap"
print(longestCommonPrefix([""]))                        # Output: ""
print(longestCommonPrefix(["alone"]))                    # Output: "alone"
