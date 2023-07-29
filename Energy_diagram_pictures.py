#import the packages
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import numpy as np
import matplotlib.colors as mcolors

from PIL import Image

#some functions I will need later

def sign(numero):
    if numero > 0:
        return 1
    elif numero < 0:
        return -1
    else:
        return 0
    







#energy diagrams with molecules pictures

def plot_imgs(enrgs,imgs,states,addstates=True,connection=True):
    """ it takes three argument1s: enrgs which should be an array or a list with the energy values.
     imgs which are the paths for the pictures and the name of the molecule which is optional but it set True.
     also the connection between the molecules is set True, it can be removed.
     All teh list should have the same dimensions."""

    
    fig, ax = plt.subplots(figsize=(10,7),sharex=True,sharey=True)

    #load the pictures
    images=[]
    for i in imgs:
        images.append(plt.imread(i))


    x=np.linspace(1,len(states),len(states))
    enrgs=np.array(enrgs)


    max_y = enrgs.max()+0.2*max(enrgs.max(),enrgs.min())*sign(enrgs.max())
    min_y = enrgs.min()+0.4*max(enrgs.max(),enrgs.min())*sign(enrgs.min())
    if connection:
        ax.plot(x,enrgs,linestyle=":")
    else:
        ax.plot(x,enrgs,color='white',linestyle=":")
    
    #define the limits of the plot
    ax.set_xlim(left=0.5,right=len(states)+0.5)
    ax.set_ylim(bottom=min_y,top=max_y)

    if addstates:
        for i in range(len(states)):
            plt.text(x[i], enrgs[i], s = states[i], ha='center', fontsize='large',bbox = dict(facecolor = 'blue', alpha = 0.5))


    for i in range(len(images)):
        #you can modify the zoom value to fit the picture with your plot
        im = OffsetImage(images[i], zoom=0.35)
        ab = AnnotationBbox(im, (x[i],enrgs[i]), xycoords='data', box_alignment=(0.5,0),frameon=False)
        ax.add_artist(ab)
    

    plt.ylabel("Energy (Kcal/mol)")
    plt.xticks([])
    #this command reove the contour
    ax.spines[['right', 'top', 'bottom']].set_visible(False)
    plt.show()
