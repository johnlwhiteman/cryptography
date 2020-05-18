class Cryptography:

    @staticmethod
    def getEquivalenceClasses(N, elements=20):
        classes = []
        for i in range(0, N):
            pos = list(range(i, elements, N))
            print(pos)
