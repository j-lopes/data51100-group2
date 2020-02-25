# -*- coding: utf-8 -*-
"""
This program computes loads the PUMS dataset and prepares some visualizations based on the data
Students:   Jenna Lopes, Geoffrey Stewart, Ryan Wade
Date:       Feb. 24, 2020
Course:     DATA-51100-002: 	Statistical Programming
Semester:   Spring 2020
Assignment: PROGRAMMING ASSIGNMENT #6

"""

import pandas as pd
import matplotlib.pyplot as plt


def main():
    # log the required output header
    print('DATA-51100, Spring 2020')
    print('NAMES: Jenna Lopes, Geoffrey Stewart, Ryan Wade')
    print('PROGRAMMING ASSIGNMENT #6')
    print('')

    df = pd.read_csv('ss13hil.csv')
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    hhl = df['HHL'].value_counts()
    hhl.index = ['English only', 'Spanish', 'Other Indo-European languages', 'Asian and Pacific Island languages', 'Other language']
    axes[0, 0].pie(hhl, startangle=242)
    axes[0, 0].legend(bbox_to_anchor=(-0.4, 1), loc="upper left", labels=hhl.index)
    axes[0, 0].set_title('Household Languages')
    axes[0, 0].set_ylabel('HHL')
    plt.show()

def bar_chart(ax):
    grouped = df.groupby('VEH')['WGTP'].sum()/1000
    ax.bar(grouped.index,grouped.values,width=0.9,bottom=None,color='r',align='center')
    ax.set_title('Vehicles Available in Households',fontsize=8)
    ax.set_xlabel('# of Vehicles',fontsize=8)
    ax.set_ylabel('Thousands of Households',fontsize=8)
    ax.set_xticks(grouped.index)
        
    ax3 = fig.add_subplot(2,2,3)
    bar_chart(ax3)
    ax3.tick_params(axis='both', which='major', labelsize=8)
    ax3.tick_params(axis='both', which='minor', labelsize=8)
    plt.show()
    
if __name__ == "__main__":
    main()
