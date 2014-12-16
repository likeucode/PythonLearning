import numpy as np
from scipy import misc
from scipy import ndimage
import matplotlib.pyplot as plt

lena = misc.lena()
print lena.shape,lena.dtype
plt.imshow(lena, cmap=plt.cm.gray)
plt.show()

plt.imshow(lena[200:220, 200:220], cmap=plt.cm.gray)

#plt.contour(l, [60, 211])
plt.show()

lena.mean()
lena.min()
lena.max()

# Cropping
lx, ly = lena.shape
crop_lena=lena[lx/4:-lx/4,ly/4:-ly/4]
plt.imshow(crop_lena, cmap=plt.cm.gray)
plt.show()

# up <-> down flip
flip_ud_lena=np.flipud(lena)
plt.imshow(flip_ud_lena, cmap=plt.cm.gray)
plt.show()

# rotation
rotate_lena = ndimage.rotate(lena, 45)
rotate_lena_noreshape = ndimage.rotate(lena, 45, reshape=False)
plt.imshow(rotate_lena, cmap=plt.cm.gray)
plt.show()

blurred_lena = ndimage.gaussian_filter(lena, sigma=3)
very_blurred = ndimage.gaussian_filter(lena, sigma=5)
local_mean = ndimage.uniform_filter(lena, size=11)
plt.figure(figsize=(9, 3))
plt.subplot(131)
plt.imshow(blurred_lena, cmap=plt.cm.gray)
plt.axis('off')
plt.subplot(132)
plt.imshow(very_blurred, cmap=plt.cm.gray)
plt.axis('off')
plt.subplot(133)
plt.imshow(local_mean, cmap=plt.cm.gray)
plt.axis('off')

plt.subplots_adjust(wspace=0, hspace=0., top=0.99, bottom=0.01,
                    left=0.01, right=0.99)

plt.show()
