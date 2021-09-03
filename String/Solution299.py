class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = []
        cows = []
        n = len(secret)
        for i in range(n):
            if secret[i] == guess[i]:
                bulls.append(i)
        secret = sorted([s for i, s in enumerate(secret) if i not in bulls])
        guess = sorted([s for i, s in enumerate(guess) if i not in bulls])
        i, j = 0, 0
        n = len(secret)
        while i < n and j < n:
            if secret[i] == guess[j]:
                cows.append(i)
                i += 1
                j += 1
                continue
            elif secret[i] < guess[j]:
                i += 1
            else:
                j += 1
        return "{}A{}B".format(len(bulls), len(cows))


s = Solution()
print(s.getHint("1807","7810"))

