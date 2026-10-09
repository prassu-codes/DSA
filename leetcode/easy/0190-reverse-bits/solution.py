class Solution:
    def reverseBits(self, n: int) -> int:
        b = ""
        for _ in range(32):
            b += str(n % 2)
            n //= 2
        return int(b, 2)
