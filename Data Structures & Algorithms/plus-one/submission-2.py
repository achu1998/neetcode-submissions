class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for i in range(len(digits)-1, -1, -1):
            if i == len(digits)-1:
                digits[i] += 1

            if carry:
                digits[i] += carry
                carry = 0

            if digits[i] > 9:
                temp = digits[i] % 10
                carry = digits[i] // 10
                digits[i] = temp 

        if carry:
            return [1] + digits
        return digits               