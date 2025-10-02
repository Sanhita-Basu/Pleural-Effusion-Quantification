#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 12 18:00:09 2023

@author: bassa192
"""

from urllib import request
import pathlib
import zipfile
import os

os.environ["nnUNet_raw_data_base"] = 'nnUNet_raw_data_base/'

os.environ["nnUNet_preprocessed"] = 'nnUNet_preprocessed/'

os.environ["RESULTS_FOLDER"] = 'nnUNet_result/'

export nnUNet_raw_data_base=nnUNet_raw_data_base

export nnUNet_preprocessed=nnUNet_preprocessed

export RESULTS_FOLDER=RESULTS_FOLDER

