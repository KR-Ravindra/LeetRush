class Solution:
    def isPalindrome(self, s: str) -> bool:
# bruteforce:
        # s = s.lower()
        # finals = ""
        # for char in s:
        #     if (char == " " or (ord(char) > 57 and ord(char) <97)
        #         or ord(char) > 122 or ord(char) < 48):
        #         char = ""
        #         finals = finals + char
        #     finals = finals + char
        # print(finals) #97-122,48-57
        # return finals == finals[::-1]
# solution by two pointers:
# -> have a left pointer and right pointer , left moves moves forward from 0 of string and vice versa for right, check if string[left] == string[right] at each step while ignoring all non alpha numeric characters
        left, right = 0 , len(s) - 1
        while left < right:
            if not self.isalphanumeric(s[left]):
                left += 1
                continue
            if not self.isalphanumeric(s[right]):
                right -= 1
                continue
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
                continue
            else:
                return False
        return True

    def isalphanumeric(self, char):
            return ((ord(char) >= ord('A') and ord(char) <= ord('Z')) or
                    (ord(char) >= ord('a') and ord(char) <= ord('z')) or
                    (ord(char) >= ord('0') and ord(char) <= ord('9')))
