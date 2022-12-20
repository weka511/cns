from matplotlib.pyplot import figure, show
from numpy             import mean, var
from pickle            import load

with open('tuning.pickle', 'rb') as f:
    data = load(f)
    print (data.keys())

    print (data['stim'].shape)
    print (data['stim'])
    print (data['neuron1'].shape)
    print (mean(data['neuron1'],axis=0).shape)
    fig = figure(figsize=(8,8))
    ax1 = fig.add_subplot(2,1,1)
    ax2 = fig.add_subplot(2,1,2)
    for i in range(4):
        neuron = f'neuron{i+1}'
        spike = 1/data[neuron]
        ax1.plot(mean(data[neuron],axis=0),label=neuron)
        ax2.plot(mean(spike,axis=0)/var(spike,axis=0),label=neuron)
    ax1.legend()

with open('pop_coding.pickle', 'rb') as  f1:
    data = load(f1)
show()
