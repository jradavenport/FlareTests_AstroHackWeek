''' 

    A preliminary version of the flare function

'''


# Define the single flare model
def aflare(t, p=[0.0, 1.0, 1.0]):
    # p must contain 3 numbers: (t0, fwhm, peak)

    # coefficients defined in paper (Davenport 2014)
    fr = np.array([1.0, 1.94053, -0.175084, -2.24588, -1.12498])
    fd = np.array([0.689008, -1.60053, 0.302963, -0.278318])
    model = np.piecewise(t,[((t-p[0])/p[1] >= -1) & (t<=p[0]),(t>p[0])] , 
                         [lambda z: 
                          fr[1]*(((z-p[0])/p[1])) + fr[0] +
                          fr[2]*(((z-p[0])/p[1]) **2) + 
                          fr[3]*(((z-p[0])/p[1]) **3) + 
                          fr[4]*(((z-p[0])/p[1]) **4) , 
                          lambda z:
                          fd[0] * np.exp((z-p[0])/p[1] * fd[1]) + 
                          fd[2] * np.exp((z-p[0])/p[1] * fd[3])
                          ] ) * p[2]
    return model




# Define the multi-flare model
def nflare(t, p):
    model = np.zeros_like(t, dtype='float')
    
    Nmodel = np.floor(np.size(p)/3.0)
    for i in range(int(Nmodel)):
        model += aflare(t, p[i*3:i*3+3])
    return model
