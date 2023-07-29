import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors



def plot(enrgs, names, states=['RC', 'TS1', 'IC', 'TS2', 'BisCuTr'], color=None,connection=True):
    """"it allows to plot energy diagram of the same reactions computed with different energy levels.
    enrgs is an array or a list which could be an array of arrays also. name describe the computetional level, 
    states is optional and represents the name of the states of the reaction"""

    for c,i in enumerate(enrgs):
        


        #you can choose the color modyfing None-->[color_list] with the dimension equals to the number of reactions
        if color==None:
            clr = list(mcolors.TABLEAU_COLORS.keys())[c] 
        else:
            clr=color[c]
        l = len(enrgs[0])
        plt.hlines(i, np.linspace(1,l-0.5, l), np.linspace(1.5, l, l), colors=clr, label =names[c])
        
        x=np.linspace(0.5, l, l)
        dx = np.linspace(1,l+0.5, l) - x
        y=i
        dy = np.roll(y,-1) - y
        if connection:
            for b in range(len(x)-1):
                
                plt.arrow(x[b],y[b], dx[b], dy[b], linewidth=0.3)

    max_y = enrgs.max() * 1.5
    min_y = enrgs.min() * 1.5
    for i in range(len(states)):
        plt.text(x=1.125*i+0.25, y=max_y*0.8, s = states[i], ha='center')
    
    plt.ylim(min_y, max_y)
    plt.ylabel("Energy (Kcal/mol)")
    plt.legend()
    plt.xticks([])
    plt.show()
