def mean(np_array):
    tot = 0
    for i in np_array:
        tot += i 
    c = len(np_array)
    ans = float(tot/c)  
    return ans


def stdev(np_array, mu='none'):
    tot = 0
    for i in np_array:
        tot += (i - mu) ** 2
    c = len(np_array)
    ans = float((tot/c) ** 0.5)  
    return ans

def sampleMean(np_array):
    ''' Each column represents a feature'''
    features = len(np_array[0])
    c = len(np_array)
    ans = []
    for i in range(features):
        tot = 0
        for j in range(c):
            tot += np_array[j][i]
        ans.append(float(tot/c))  
    return ans


def covariance(np_array):
    ''' Each column represents a feature'''
    features = len(np_array[0])
    c = len(np_array)
    mean = sampleMean(np_array)
    ans = []
    for i in range(features):
        cov = []
        for j in range(features):
            tot = 0
            for k in range(c):
                tot += (np_array[k][i] - mean[i]) * (np_array[k][j] - mean[j])
            cov.append(float(tot / c)) # For Sample Covariance we can divide the tot with c-1
        ans.append(cov)  
    return ans