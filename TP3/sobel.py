#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 22 May 2019

@author: M Roux
"""
# %%
import math
import numpy as np
import matplotlib.pyplot as plt
import skimage as sk

from scipy import ndimage
from scipy import signal

from skimage import io

from skimage import filters

import mrlab as mr

# %%
plt.close("all")

# %%
ima = io.imread("images./cell.tif")
sigma = 0
seuilnorme = 0.1

# %%
gfima = filters.gaussian(ima, sigma)

plt.figure("Image originale")
plt.imshow(ima, cmap="gray")
plt.show()

plt.figure("Image filtrée (passe-bas)")
plt.imshow(gfima, cmap="gray")
plt.show()

# %%
gradx = mr.sobelGradX(gfima)
grady = mr.sobelGradY(gfima)

plt.figure("Gradient horizontal")
plt.imshow(gradx, cmap="gray")
plt.show()

plt.figure("Gradient vertical")
plt.imshow(grady, cmap="gray")
plt.show()

# %%
norme = np.sqrt(gradx * gradx + grady * grady)

plt.figure("Norme du gradient")
plt.imshow(norme, cmap="gray")
plt.show()

# %%
direction = np.arctan2(grady, gradx)

plt.figure("Direction du Gradient")
plt.imshow(direction, cmap="gray")
plt.show()

# %%
contoursnorme = norme > seuilnorme

plt.figure("Norme seuillée")
plt.imshow(255 * contoursnorme, cmap="gray")
plt.show()

# %%
contours = np.uint8(mr.maximaDirectionGradient(gradx, grady))

plt.figure("Maxima du gradient dans la direction du gradient")
plt.imshow(255 * contours, cmap="gray")
plt.show()

# %%
valcontours = (norme > seuilnorme) * contours

plt.figure()
plt.imshow(255 * valcontours, cmap="gray")
plt.show()

# %%
