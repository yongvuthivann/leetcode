class Solution:
    def romanToInt(self, s: str) -> int:
      roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
      index, result = 0, 0
      while index < len(s):
        if index + 1 < len(s) and s[index:index+2] in roman:
          result += roman[s[index:index+2]]
          index += 2
        else:
          result += roman[s[index]]
          index += 1
      return result