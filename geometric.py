import math

# ham tra ve xac suat cho phan bo geometric
def prob(n, p):
    '''
    Return prob of geometric destribution
    ---
    Parameters:
    - n: int
        symbol n
    - p: float
        prob bernoulli
    Return:
        p
    '''
    p = 1/(2**n)
    return p

# ham tra ve gia tri luong tin cua symbol X = n
def infoMeasure(n, p):
    '''
    Return amount of information that symbol n carries
    ---
    Parameters:
    - n: int
        symbol n
    - p: float
        prob bernoulli
    Return:
        -log2(prob(n,p))
    '''
    return = -math.log2(prob(n, p))

# ham tra ve tong xac suat cua cac symbol tu 1 den N
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
    - khi N = 10  sumProb = 0.9990234375 (gần bằng 1)
    - khi N = 100 sumProb = 1.0
    - khi N = 1000 sumProb = 1.0
    '''
    sum = 0
    for i in range(1, N + 1):
        sum += prob(i, p)
    return sum

# hàm tính trung bình lượng tin của các symbol từ 1 đến N
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
    - khi N = 100, avgInfo = entropy = 1.9999999999999998 ~ 2
    - khi N = 1000, entropy = 1.9999999999999998 ~ 2
    '''
    sum = 0
    for i in range(1, N + 1):
        sum += infoMeasure(i, p)

    return sum


if __name__ == "__main__":
    print(prob(5, 0.5, 5))

    print(infoMeasure(5, 0.5, 5))

    print(sumProb(100, 0.5))

    print(approxEntropy(100, 0.5))
