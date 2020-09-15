#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 16:48:26 2020

@author: shub

"""
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

''' Run data_creation.py first and then this '''

plt.style.use('BSGIP_style')
# Make a dictionary for each dataset so that you can just add functions to plot what you want
# import the data here

def bar_plot(dict_name, title_header, ylab, xlab= None):
    
    """ Function plotting number of times the dataset has been used 
    
    Args: 
        dict_name: Dictionary containg the number of times dataset(s) has been used
        title(str): The title of the graph
    
    Returns:
        Nothing
        
        Only used for plotting
    
    """
    
    dataset, performance = [],[]
    for key, values in dict_name.items():
        print(key,values)
        dataset.append(key)
        performance.append(values)

    y_pos = np.arange(len(dataset))
    
    plt.figure()
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, dataset)
    plt.ylabel(ylab)
    if xlab:
        plt.xlabel(xlab)
    plt.title(title_header)
    
    plt.tight_layout()


def return_dict_of_vars(data):
    v  = sum(item['v'] for item in data)
    i  = sum(item['i'] for item in data)
    p  = sum(item['p/e'] for item in data)
    q  = sum(item['q'] for item in data)
    f  = sum(item['f'] for item in data)
    ph = sum(item['ph'] for item in data)
    dict_of_vars = {'v':v , 'i':i, 'p':p, 'q':q, 'f':f, 'ph':ph}
    return dict_of_vars

def return_dict_of_nodes(data):
    n1 = sum(item['1-10'] for item in data)
    n2 = sum(item['11-50'] for item in data)
    n3 = sum(item['51-300'] for item in data)
    n4 = sum(item['301-1000'] for item in data)
    n5 = sum(item['>1000'] for item in data)
    dict_of_nodes = {'1-10':n1 , '11-50':n2, '51-300':n3, '301-1000':n4, '>1000':n5}    
    return dict_of_nodes

def return_dict_of_generation(data):
    n1 = sum(item['pv'] for item in data)
    n2 = sum(item['no-pv'] for item in data)
    n3 = sum(item['unknown'] for item in data)
    dict_of_generation = {'PV':n1 , 'No PV':n2, 'Unknown':n3}   
    return dict_of_generation

def return_dict_of_reso(data):
    n1 = sum(item['<1s'] for item in data)
    n2 = sum(item['1-10s'] for item in data)
    n3 = sum(item['1min'] for item in data)
    n4 = sum(item['1-10min'] for item in data)
    n5 = sum(item['>10mins'] for item in data)
    dict_of_reso = {'<1s':n1 , '1-10s':n2, '1min':n3, '1-10min':n4, '>10mins':n5}        
    return dict_of_reso
    

dict_of_vars       = return_dict_of_vars(diffVars)
dict_of_nodes      = return_dict_of_nodes(numOfNodes)
dict_of_generation = return_dict_of_generation(pv_gen)
dicr_of_reso       = return_dict_of_reso(reso)

print('Number of Papers/ Reports for the Datasets from their Websites')
bar_plot(numOfPapers, 'Number of Papers/Reports from the Websites ', 'Number of papers', 'Datasets')

print('Number of Citations for the Official paper of the Datasets')
bar_plot(papersCited, 'Number of Citations of the Official Dataset Paper', 'Number of papers', 'Datasets')

print('Number of times variable has been used')
bar_plot(dict_of_vars, 'Variables Used in Different Datasets', 'Number of datasets', 'Variables')

print('Number of Nodes')
bar_plot(dict_of_nodes, 'Datasets with different Number of Nodes ', 'Number of datasets', 'Number of Nodes')

print('Generation')
bar_plot(dict_of_generation, 'Datasets with and without PV Generation ', 'Number of datasets',)

print('Resolution')
bar_plot(dicr_of_reso, 'Datasets with different Resolution ', 'Number of datasets', 'Resolution')

ylab = 'Number of papers'
xlab = 'Datasets'
title_header = 'Number of Papers/Reports from the Websites'
dataset, performance = [],[]
for key, values in dict_of_vars.items():
    print(key,values)
    dataset.append(key)
    performance.append(values)

y_pos = np.arange(len(dataset))
dataset = ['Voltage', 'Current', 'Power','Reactive Power', 'freq','phase']

plt.figure()
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, dataset)
plt.ylabel(ylab)
if xlab:
    plt.xlabel(xlab)
plt.title(title_header)
#    
#labels = ['Voltae', 'Current', 'Power','Reactive', 'freq','phase']
#handles = ['Voltae', 'Current', 'Power','Reactive', 'freq','phase']
##plt.legend(('v','i','p','q','r','s'),labels)
##plt.legend(handles,labels)
##plt.legend(plt.xticks,labels)
##plt.legend((v, i, p, q. r. ph), ('Voltage', 'label2', 'label3', 'label4', 'label5', 'label6'))
##plt.legend(('Alpha','Beta'), loc='best')
#v = mpatches.Patch( label='North America')
#i = mpatches.Patch(label='Europe')
#p = mpatches.Patch( label='Asia/Pacific')
#q = mpatches.Patch( label='South America')
#f = mpatches.Patch( label='South America')
#ph = mpatches.Patch( label='South America')
#plt.legend(handles=handles, loc=2)
#
#plt.tight_layout()