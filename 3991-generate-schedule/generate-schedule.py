class Solution:
    def generateSchedule(self, n):
        """
        this one was pretty hard; round-robin style
        """
        result = []

        if n <= 4:
            return []

        l = 1
        if n % 2 == 0:
            for i in range(0, n, 2):
                result.append([i, i + l])
            for i in range(0, n, 2):
                result.append([i + l, i])
            for i in range(1, n, 2):
                result.append([i, (i + l) % n])
            for i in range(1, n, 2):
                result.append([(i + l) % n, i])
        else:
            for i in range(0, 2 * n, 2):
                result.append([i % n, (i + l) % n])
            for i in range(0, 2 * n, 2):
                result.append([(i + l) % n, i % n])

        for l in range(2, (n + 1) // 2):
            j = result[-1][0] + 1
            for i in range(j, j + n):
                result.append([i % n, (i + l) % n])
            j = result[-1][1] - 1
            for i in range(j, j + n):
                result.append([(i + l) % n, i % n])

        if n % 2 == 0:
            l = n // 2
            j = result[-1][0] - 1
            for i in range(j, j + n):
                result.append([i % n, (i + l) % n])

        return result