def sum(N, M):
    # HCF
    result = min(N, M)
    while (result):
        if ((M % result == 0) and (N % result == 0)):
            break
        else:
            result = result - 1
    finalValue = int((N / result) + (M / result))
    return finalValue


def sum(self, N, M):
    # HCF
    def gcd(N, M):
        if M == 0:
            return N
        else:
            return gcd(M, N % M)

    hcf = int(gcd(N, M))
    result = int((N / hcf) + (M / hcf))
    return (result)


print(sum(5,6))
