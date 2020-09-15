#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 09:46:17 2020

@author: shub
"""

''' Number of Papers'''
# From their Respective Website
numOfPapers = {'acn':7, 'pecan':230, 'nextgen':3, 'uMass':11}

# From the number of citations of the main paper
papersCited = {'uMass':360, 'redd':958, 'ampd':88, 'ukdale':292, 'blond':16, 'blued':33+251, 'cooll':31, 
               'dred':57, 'eco':192, 'greend':113, 'iawe':112, 'refit':73, 'tbs':193} 


''' Different Variables uses'''

#'dataset':'acn',   'v':0, 'i':0, 'p/e':, 'q':, 'f':, 'ph': Not counting acn
diffVars = [
{'dataset':'pecan', 'v':0, 'i':0, 'p/e':1, 'q':0, 'f':0, 'ph':0},
{'dataset':'sgsc',  'v':0, 'i':0, 'p/e':1, 'q':0, 'f':0, 'ph':0},
{'dataset':'lzsa',  'v':0, 'i':0, 'p/e':1, 'q':0, 'f':0, 'ph':0},
{'dataset':'ng',    'v':1, 'i':0, 'p/e':1, 'q':1, 'f':1, 'ph':0},
{'dataset':'lclp',  'v':0, 'i':0, 'p/e':1, 'q':0, 'f':0, 'ph':0},
{'dataset':'shed',  'v':0, 'i':0, 'p/e':1, 'q':0, 'f':0, 'ph':0},
{'dataset':'tuva',  'v':1, 'i':0, 'p/e':1, 'q':1, 'f':0, 'ph':0},
{'dataset':'epri',  'v':0, 'i':0, 'p/e':1, 'q':1, 'f':0, 'ph':0},
{'dataset':'umass', 'v':0, 'i':0, 'p/e':1, 'q':0, 'f':0, 'ph':0},
{'dataset':'redd',  'v':0, 'i':1, 'p/e':1, 'q':0, 'f':1, 'ph':0},
{'dataset':'ampd',  'v':1, 'i':1, 'p/e':1, 'q':1, 'f':0, 'ph':0},
{'dataset':'dale',  'v':1, 'i':1, 'p/e':1, 'q':1, 'f':0, 'ph':0},
{'dataset':'rbsa',  'v':0, 'i':0, 'p/e':1, 'q':0, 'f':0, 'ph':0},
{'dataset':'uci',   'v':1, 'i':1, 'p/e':1, 'q':1, 'f':0, 'ph':0},
{'dataset':'blond', 'v':1, 'i':1, 'p/e':0, 'q':0, 'f':0, 'ph':0},
{'dataset':'blued', 'v':1, 'i':1, 'p/e':0, 'q':0, 'f':0, 'ph':0},
{'dataset':'cooll', 'v':1, 'i':1, 'p/e':0, 'q':0, 'f':0, 'ph':0},
{'dataset':'dred',  'v':0, 'i':0, 'p/e':1, 'q':0, 'f':0, 'ph':0},
{'dataset':'eco',   'v':1, 'i':1, 'p/e':0, 'q':0, 'f':0, 'ph':1},
{'dataset':'greend','v':0, 'i':0, 'p/e':1, 'q':0, 'f':0, 'ph':0},
{'dataset':'iawe', 'v':1, 'i':1, 'p/e':1, 'q':0, 'f':1, 'ph':1},
{'dataset':'refit', 'v':0, 'i':0, 'p/e':1, 'q':0, 'f':0, 'ph':0},
{'dataset':'tbs',   'v':0, 'i':0, 'p/e':1, 'q':0, 'f':0, 'ph':0}
]


''' NUmber of Nodes in Datasets '''
# Not Counting ACN
numOfNodes = [
{'dataset':'pecan', '1-10':0, '11-50':0, '51-300':0, '301-1000':1, '>1000':0,},
{'dataset':'sgsc',  '1-10':0, '11-50':0, '51-300':0, '301-1000':0, '>1000':1,},
{'dataset':'lzsa',  '1-10':0, '11-50':1, '51-300':0, '301-1000':0, '>1000':0,},
{'dataset':'ng',    '1-10':0, '11-50':0, '51-300':0, '301-1000':0, '>1000':1,},
{'dataset':'lclp',  '1-10':0, '11-50':0, '51-300':0, '301-1000':0, '>1000':1,},
{'dataset':'shed',  '1-10':0, '11-50':0, '51-300':1, '301-1000':0, '>1000':0,},
{'dataset':'tuva',  '1-10':0, '11-50':1, '51-300':0, '301-1000':0, '>1000':0,},
{'dataset':'epri',  '1-10':0, '11-50':1, '51-300':0, '301-1000':0, '>1000':0,},
{'dataset':'umass', '1-10':0, '11-50':0, '51-300':0, '301-1000':1, '>1000':0,},
{'dataset':'redd',  '1-10':1, '11-50':0, '51-300':0, '301-1000':0, '>1000':0,},
{'dataset':'ampd',  '1-10':1, '11-50':0, '51-300':0, '301-1000':0, '>1000':0,},
{'dataset':'dale',  '1-10':1, '11-50':0, '51-300':0, '301-1000':0, '>1000':0,},
{'dataset':'rbsa',  '1-10':0, '11-50':0, '51-300':1, '301-1000':0, '>1000':0,},
{'dataset':'uci',   '1-10':1, '11-50':0, '51-300':0, '301-1000':0, '>1000':0,},
{'dataset':'blond', '1-10':1, '11-50':0, '51-300':0, '301-1000':0, '>1000':0,},
{'dataset':'blued', '1-10':1, '11-50':0, '51-300':0, '301-1000':0, '>1000':0,},
{'dataset':'cooll', '1-10':0, '11-50':1, '51-300':0, '301-1000':0, '>1000':0,},
{'dataset':'dred',  '1-10':1, '11-50':0, '51-300':0, '301-1000':0, '>1000':0,},
{'dataset':'eco',   '1-10':1, '11-50':0, '51-300':0, '301-1000':0, '>1000':0,},
{'dataset':'greend','1-10':1, '11-50':0, '51-300':0, '301-1000':0, '>1000':0,},
{'dataset':'iawe', '1-10':1, '11-50':0, '51-300':0, '301-1000':0, '>1000':0,},
{'dataset':'refit', '1-10':0, '11-50':1, '51-300':0, '301-1000':0, '>1000':0,},
{'dataset':'tbs',   '1-10':0, '11-50':0, '51-300':1, '301-1000':0, '>1000':0,}
]

''' Datasets with PV Gen'''
pv_gen = [
{'dataset':'acn',   'pv':0, 'no-pv':1, 'unknown':0,},        
{'dataset':'pecan', 'pv':1, 'no-pv':0, 'unknown':0,},
{'dataset':'sgsc',  'pv':0, 'no-pv':1, 'unknown':0,},
{'dataset':'lzsa',  'pv':0, 'no-pv':1, 'unknown':0,},
{'dataset':'ng',    'pv':1, 'no-pv':0, 'unknown':0,},
{'dataset':'lclp',  'pv':0, 'no-pv':1, 'unknown':0,},
{'dataset':'shed',  'pv':1, 'no-pv':0, 'unknown':0,},
{'dataset':'tuva',  'pv':0, 'no-pv':1, 'unknown':0,},
{'dataset':'epri',  'pv':1, 'no-pv':0, 'unknown':0,},
{'dataset':'umass', 'pv':1, 'no-pv':0, 'unknown':0,},
{'dataset':'redd',  'pv':0, 'no-pv':1, 'unknown':0,},
{'dataset':'ampd',  'pv':0, 'no-pv':1, 'unknown':0,},
{'dataset':'dale',  'pv':0, 'no-pv':1, 'unknown':0,},
{'dataset':'rbsa',  'pv':0, 'no-pv':1, 'unknown':0,},
{'dataset':'uci',   'pv':0, 'no-pv':1, 'unknown':0,},
{'dataset':'blond', 'pv':0, 'no-pv':1, 'unknown':0,},
{'dataset':'blued', 'pv':0, 'no-pv':1, 'unknown':0,},
{'dataset':'cooll', 'pv':0, 'no-pv':1, 'unknown':0,},
{'dataset':'dred',  'pv':0, 'no-pv':1, 'unknown':0,},
{'dataset':'eco',   'pv':0, 'no-pv':1, 'unknown':0,},
{'dataset':'greend','pv':0, 'no-pv':1, 'unknown':0,},
{'dataset':'iawe', 'pv':0, 'no-pv':1, 'unknown':0,},
{'dataset':'refit', 'pv':0, 'no-pv':1, 'unknown':0,},
{'dataset':'tbs',   'pv':0, 'no-pv':1, 'unknown':0,}
]

''' Datasets with resolution '''
# Not including ACN
reso = [
{'dataset':'pecan', '<1s':0, '1-10s':1, '1min':1, '1-10min':0, '>10mins':1,},
{'dataset':'sgsc',  '<1s':0, '1-10s':0, '1min':0, '1-10min':0, '>10mins':1,},
{'dataset':'lzsa',  '<1s':0, '1-10s':0, '1min':0, '1-10min':0, '>10mins':1,},
{'dataset':'ng',    '<1s':0, '1-10s':0, '1min':0, '1-10min':1, '>10mins':0,},
{'dataset':'lclp',  '<1s':0, '1-10s':0, '1min':0, '1-10min':0, '>10mins':1,},
{'dataset':'shed',  '<1s':0, '1-10s':0, '1min':0, '1-10min':0, '>10mins':1,},
{'dataset':'tuva',  '<1s':0, '1-10s':1, '1min':0, '1-10min':0, '>10mins':0,},
{'dataset':'epri',  '<1s':0, '1-10s':1, '1min':1, '1-10min':0, '>10mins':1,},
{'dataset':'umass', '<1s':0, '1-10s':1, '1min':0, '1-10min':0, '>10mins':0,},
{'dataset':'redd',  '<1s':1, '1-10s':1, '1min':0, '1-10min':0, '>10mins':0,},
{'dataset':'ampd',  '<1s':0, '1-10s':0, '1min':1, '1-10min':0, '>10mins':0,},
{'dataset':'dale',  '<1s':0, '1-10s':1, '1min':0, '1-10min':0, '>10mins':0,},
{'dataset':'rbsa',  '<1s':0, '1-10s':0, '1min':0, '1-10min':0, '>10mins':1,},
{'dataset':'uci',   '<1s':0, '1-10s':0, '1min':1, '1-10min':0, '>10mins':0,},
{'dataset':'blond', '<1s':1, '1-10s':0, '1min':0, '1-10min':0, '>10mins':0,},
{'dataset':'blued', '<1s':1, '1-10s':0, '1min':0, '1-10min':0, '>10mins':0,},
{'dataset':'cooll', '<1s':1, '1-10s':0, '1min':0, '1-10min':0, '>10mins':0,},
{'dataset':'dred',  '<1s':0, '1-10s':1, '1min':0, '1-10min':0, '>10mins':0,},
{'dataset':'eco',   '<1s':0, '1-10s':1, '1min':0, '1-10min':0, '>10mins':0,},
{'dataset':'greend','<1s':0, '1-10s':1, '1min':0, '1-10min':0, '>10mins':0,},
{'dataset':'iawe', '<1s':0, '1-10s':1, '1min':0, '1-10min':0, '>10mins':0,},
{'dataset':'refit', '<1s':0, '1-10s':1, '1min':0, '1-10min':0, '>10mins':0,},
{'dataset':'tbs',   '<1s':0, '1-10s':1, '1min':0, '1-10min':0, '>10mins':0,}
]