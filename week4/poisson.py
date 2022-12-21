from matplotlib.pyplot import figure, show
from numpy             import array, mean, var
from pickle            import load

def get_tuning():
    with open('tuning.pickle', 'rb') as f:
        data   = load(f)
        stim   = data['stim']
        Neuron = array([data[f'neuron{i+1}'] for i in range(4)])
    return stim,Neuron

def get_pop_coding():
    with open('pop_coding.pickle', 'rb') as  f:
        data = load(f)
        C    = array([data[f'c{i+1}'] for i in range(4)])
        R    = array([data[f'r{i+1}'] for i in range(4)])
        return C, R

if __name__=='__main__':
    stim,Neuron = get_tuning()
    C,R         = get_pop_coding()

    fig = figure(figsize=(8,8))
    ax1 = fig.add_subplot(2,1,1)
    ax2 = fig.add_subplot(2,1,2)
    for i in range(4):
        spike = 1/Neuron[i,:,:]
        ax1.plot(mean(Neuron[i,:,:],axis=0),label=f'Tuning: {i+1}')
        ax2.plot(mean(spike,axis=0)/var(spike,axis=0),label=f'{i+1}')
    ax1.legend()



    show()
