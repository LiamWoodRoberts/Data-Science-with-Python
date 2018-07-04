def z_scorez(x,allpoints):
    import numpy as np
    zscore = (x-np.mean(allpoints))/np.std(bike_data)
    return zscore

def z_score_no_numpy(x,allpoints):
    import numpy as np
    data = np.asarray(allpoints)
    mean = sum(data)/len(data)
    std = np.sqrt(sum((data-mean)**2)/(len(data)-1))
    zscore = (x-mean)/std
    return zscore
