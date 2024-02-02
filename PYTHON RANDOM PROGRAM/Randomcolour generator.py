import random
import matplotlib.pyplot as plt
colors=["red","green","blue","yellow","orange","purple"]
random_color=random.choice(colors)
plt.figure(figsize=(1,1),facecolor=random_color)
plt.text(0.5,0.5,random_color,fontsize=20)
plt.axis('off')
plt.show()