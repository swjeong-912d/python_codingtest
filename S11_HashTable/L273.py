class Solution:
    def numberToWords(self, num: int) -> str:
        dic = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',
               10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen',
               17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty',
               60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety', 10 ** 2: 'Hundred', 10 ** 3: 'Thousand',
               10 ** 6: 'Million', 10 ** 9: 'Billion'}

        def under_thousand(n):
            q, r = divmod(n, 100)
            if r == 0:
                pass
            elif r < 20:
                output.appendleft(dic[r])
            else:
                if r % 10 > 0:
                    output.appendleft(dic[r % 10])
                output.appendleft(dic[r // 10 * 10])
            if q > 0:
                output.appendleft(dic[100])
                output.appendleft(dic[q])

        if num == 0:
            return "Zero"
        output = deque()

        digit = 1
        while num:
            num, nr = divmod(num, 1000)
            if nr > 0:
                if digit > 1:
                    output.appendleft(dic[digit])
                under_thousand(nr)
            digit *= 1000
        return ' '.join(output)
def print_test():
    leet_sol = Solution()
    leet_sol.numberToWords(1234567891)
    leet_sol.numberToWords(0)
    leet_sol.numberToWords(100000)