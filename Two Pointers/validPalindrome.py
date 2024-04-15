class Solution:
    def isPalindrome(self, s: str) -> bool:
        revStr = ""
        for c in s:
            #eliminate punctuation
            if c.isalnum():
                #make all uniform case
                revStr += c.lower()
        #compare string to reversed string
        return revStr == revStr[::-1]
        

def testIsPalindrome():
    s = "A man, a plan, a canal: Panama"
    print(Solution.isPalindrome(Solution, s))
    #Output: true
    #Explanation: "amanaplanacanalpanama" is a palindrome.

    s = "race a car"
    print(Solution.isPalindrome(Solution, s))
    #Output: false
    #Explanation: "raceacar" is not a palindrome.

    s = " "
    print(Solution.isPalindrome(Solution, s))
    #Output: true
    #Explanation: s is an empty string "" after removing non-alphanumeric characters.
    #Since an empty string reads the same forward and backward, it is a palindrome.

testIsPalindrome()