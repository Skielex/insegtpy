#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 12:30:39 2021

@author: vand
"""

import insegtpy
import skimage.data 

image = skimage.data.camera()
insegtpy.annotate(image)


