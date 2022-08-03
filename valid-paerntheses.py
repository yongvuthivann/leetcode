class Solution(object):
    def isValid(self, s):
        valid_lst = []
        if len(s) % 2 != 0:
            return False
        else:
            valid_parenetheses = {'(' : ')', '[' : ']', '{' : '}'}
            result = []
            for item in s:
                if item in valid_parenetheses.keys():
                    result.append(item)
                else:
                    if result == []:
                        return False
                    pop_item = result.pop()
                    if item != valid_parenetheses[pop_item]:
                        return False
            return result == []

