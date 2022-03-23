#simulation_static_visualization.py
"""
This program will focus on visualizations, which help me 'get to know' my data.
I will use 2 open-source visualization libraries  - Seaborn and Matplotlib to
display static bar chart showing the final results of six-sided-die-rollingg simulation.
Sample graphs fo 600, 60,000 and 6,000,000 die rolls.
"""
#1.Visualizingg Die-Roll Frequencies and Percentages
import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns

#rolling the die and calculating die frequencies
rolls = [random.randrange(1,7) for i in range(60_000)]
#print(f'rolls={rolls}')
print()

#unpack the tuple returned by unique, which contains 2 ndarrays()
values,frequencies = np.unique(rolls, return_counts=True) #return a tuple of ndarrays containg sorted unique values and corresponding frequencies
print(f'values={values}-->frequencies={frequencies}')

#let's use zip() to get seperated data
for val,freq in zip(values, frequencies):
    print(f'val={val}-->freq={freq}')

print()
#check 2nd solution:
for value, freq in [np.unique(rolls,return_counts=True)]:
    print(f'value={value}-->frequency={freq}')


# Creatingg intial bar plot.
"""
Create bar plot's title, set its style, then graph die faces and frequencies.
"""
#check:
print(f'len(rolls):,={len(rolls):,.2f}')

title = f'Rolling a Six-Sided Die {len(rolls):,} Times'
sns.set_style('whitegrid')
axes = sns.barplot(x=values,y=frequencies,palette='bright') #x,y are ndarrays unpacked from np.unique(rolls, return_counts=True)

#Setting the window title and labelling x,y axes
axes.set_title(title)
axes.set(xlabel='Die Value',ylabel='Frequency')

# axes.set_xlabel('jaja') - also works
# axes.set_ylabel('ggg')  - also works

#Finalizing the bar plot
axes.set_ylim(top=max(frequencies)*1.10) #creating the room above each bar for the text -> highest bar + 10%highest bar

for bar,frequency in zip(axes.patches, frequencies): #axes.patches - collection contains 2 dimentional colored shapes represents the plot's bar
    text_x = bar.get_x() + bar.get_width()/2 #Calculate x-cordinate where text appear = left-edge x-cord ->bar.get_x() + half of the bar's width bar.get_width()/2
    text_y = bar.get_height()
    text = f'{frequency:,}\n{frequency/len(rolls):.3%}' #format specifier :, - seperate big digitd with,
    axes.text(text_x,text_y,text,fontsize=11,ha='center',va='bottom') #ha-hotizontal alignment - center of the bar; va-vertical alignment - bottom of the text with at the y-cordinate


#for check:
print(f'axes.patches={axes.patches}')
print(f'len(axes.patches)={len(axes.patches)}')
print(f'frequencies[0]:{frequencies[0]}/len(rolls):{len(rolls)}:.3%={frequencies[0]/len(rolls):.3%}')  #f' string format specifier :.3% - converts to precentage rounded to 3 digits after dot

plt.savefig(f'die_roll{len(rolls):,}times.pdf')
plt.show()  #seaborn lib is connected with matplotlip lib, and we use plt.show()-matplotlip functions to see seaborn visualization




















