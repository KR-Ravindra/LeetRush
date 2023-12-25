class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        finals = ""
        for char in s:
            if (char == " " or (ord(char) > 57 and ord(char) <97)
                or ord(char) > 122 or ord(char) < 48):
                char = ""
                finals = finals + char
            finals = finals + char
        print(finals) #97-122,48-57
        return finals == finals[::-1]
