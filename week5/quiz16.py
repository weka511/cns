from intfire import intfire

'''Answer to Q 16 (largest current that will fail to cause neuron to spike)'''
I0 = 0
I1 = 1

while I1-I0>0.0005:
    I                = 0.5*(I0+I1)
    n_spikes,V_trace = intfire(I=I)
    if n_spikes==0:
        I0 = I
    else:
        I1 = I
    print (I0,I1,I,n_spikes)
print (1000*I0)
