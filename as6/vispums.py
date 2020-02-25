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


if __name__ == "__main__":
    main()
