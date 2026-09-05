class Solution(object):
    def reformat(self, s):
        letters = ""
        numbers = ""

        for c in s:
            if c.isalpha():
                letters += c
            else:
                numbers += c

        if abs(len(letters) - len(numbers)) > 1:
            return ""

        if len(numbers) > len(letters):
            letters, numbers = numbers, letters

        result = ""

        for i in range(len(numbers)):
            result += letters[i] + numbers[i]

        if len(letters) > len(numbers):
            result += letters[-1]

        return result