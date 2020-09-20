import math

def prob(n, p, N):
    '''
    Return prob of binomial destribution
    ---
    Parameters:
    - n: int
        symbol n
    - p: float
        prob bernoulli
    Return:
        p
    '''
    p = (math.factorial(N)/(math.factorial(n)*(math.factorial(N-n)))) * (p**n) * ((1-p)**(N-n))
    return p


def infoMeasure(n, p, N):
    '''
    Return amount of information that symbol n carries
    ---
    Parameters:
    - n: int
        symbol n
    - p: float
        prob bernoulli
    Return:
        -log2(prob(n,p,N))
    '''
    return -math.log2(prob(n, p, N))


def sumProb(N, p):
    '''
    Return sum of prob of symbol from 1 to N
    ---
    Parameters:
    - N: int
        sum of symbol
    - p: float
        prob bernoulli
    Return:
        variable sum

    Không gian mẫu có N symbol => tổng xác suất của các symbol đó phải bằng 1
    Thực nghiệm:
    - khi N = 100 sumProb = 1.0000000000000002 ~ 1
    - khi N = 1000 sumProb = 1.0
    '''
    sum = 0
    for i in range(1, N + 1):
        sum += prob(i, p, N)
        i = i+1
    return sum

def approxEntropy(N, p):
    '''
    Return average information of all symbol from 1 to N
    ---
    Parameters:
    - N: int
        sum of symbol
    - p: float
        prob bernoulli
    Return:
        variable avgInfo
    Thực nghiệm:
    - khi N = 100, avgInfo = 4.369011409223017 (entropy)
    - khi N = 1000, avgInfo = 6.029987607045884 (entropy)
    '''
    avgInfo = 0
    for i in range(0, N + 1):
        avgInfo += prob(i, p, N) * infoMeasure(i, p, N)
    return avgInfo


if __name__ == "__main__":
    print(prob(5, 0.5, 5))

    print(infoMeasure(5, 0.5, 5))

    print(sumProb(100, 0.5))

    print(approxEntropy(1000, 0.5))
