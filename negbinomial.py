import math

def prob(n, p, r):
    '''
    Return prob of negbinomial destribution
    ---
    Parameters:
    - n: int
        symbol n
    - p: float
        prob bernoulli
    - r: int
        số lần thành công (ngửa) mà đạt được thì dừng
    Return:
        p
    '''
    if n < r:
        return 0

    p = (math.factorial(n-1)/(math.factorial(n-r)*(math.factorial(r-1)))) * (p**r) * ((1-p)**(n-r))
    return p


def infoMeasure(N, p, r):
    '''
    Return amount of information that symbol n carries
    ---
    Parameters:
    - n: int
        symbol n
    - p: float
        prob bernoulli
    - r: int
        số lần thành công (ngửa) mà đạt được thì dừng
    Return:
        -log2(prob(N,p,r))
    '''
    if N < r:
        return 0

    return -math.log2(prob(N, p, r))


def sumProb(N, p, r):
    '''
    Return sum of prob of symbol from 1 to N
    ---
    Parameters:
    - N: int
        sum of symbol
    - p: float
        prob bernoulli
    - r: int
        số lần thành công (ngửa) mà đạt được thì dừng
    Return:
        variable sum

    Không gian mẫu có N symbol => tổng xác suất của các symbol đó phải bằng 1
    Thực nghiệm:
    - khi N = 100 sumProb = 0.9999999999999999 ~ 1.0
    - khi N = 1000 sumProb = 0.9999999999999999 ~ 1.0
    '''
    sum = 0
    for i in range(r, N + 1):
        sum += prob(i, p, r)

    return sum

def approxEntropy(N, p, r):
    '''
    Return average information of all symbol from 1 to N
    ---
    Parameters:
    - N: int
        sum of symbol
    - p: float
        prob bernoulli
    - r: int
        số lần thành công (ngửa) mà đạt được thì dừng
    Return:
        variable avgInfo (xấp xỉ entropy)
    Thực nghiệm:
    - khi N = 100, avgInfo = 4.150775320863947 (entropy)
    - khi N = 1000, avgInfo = 4.150775320863947 (entropy)
    '''
    avgInfo = 0.0
    for i in range(r, N + 1):
        avgInfo += prob(i, p, r) * infoMeasure(i, p, r)
    return avgInfo


if __name__ == "__main__":
    print(prob(5, 0.5, 5))

    print(infoMeasure(5, 0.5, 5))

    print(sumProb(100, 0.5, 10))

    print(approxEntropy(1000, 0.5, 10))
