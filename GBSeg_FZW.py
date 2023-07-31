#######-----------Image segmentation and Visualization-----------#######

import matplotlib.pyplot as plt
import skimage.io
import skimage.segmentation
from skimage.color import label2rgb
from skimage.measure import label, regionprops

# Setting the path of the input image and adjusting the parameters.
image_path = "C:/Users/nchez/Desktop/inp_im.jpg"

# Parameter controlling the size of segments
scale = 100

# Sigma parameter for width of Gaussian kernel
sigma = 0.5

# Threshold to merge small segments
size_threshold = 200  

# Loading the input image.
image = skimage.io.imread(image_path)

# Perform Felzenszwalb segmentation by using 
# the in-built function felzenszwalb().
segments = skimage.segmentation.felzenszwalb(image, scale=scale, sigma=sigma)

# In this section, the smaller segments are merged.
label_image = label(segments)
props = regionprops(label_image)
for prop in props:
    if prop.area < size_threshold:
        label_image[label_image == prop.label] = 0

# Creating the boundary overlay for visualization.
boundaries = skimage.segmentation.mark_boundaries(image, label_image, color=(1, 0, 0), outline_color=None)

# Creating a color overlay for the segmented regions for visualization.
overlay = label2rgb(label_image, image, bg_label=0)

# Determines the number of segments generated, for the sake of analysis.
segment_count = len(regionprops(label_image))
print("Number of segments:", segment_count)

# Displaying the original image and segmented images with overlays.
fig, ax = plt.subplots(2, 2, figsize=(10, 5))
ax[0, 0].imshow(image, cmap="gray")
ax[0, 0].set_title("Original Image")
ax[0, 0].axis("off")

ax[0, 1].imshow(label_image, cmap="jet")
ax[0, 1].set_title("Segmented Image (Jet Colormap Visualization)")
ax[0, 1].axis("off")

ax[1, 0].imshow(overlay)
ax[1, 0].set_title("Segmented Image with Color Overlay")
ax[1, 0].axis("off")

ax[1, 1].imshow(boundaries)
ax[1, 1].set_title("Boundary Overlay")
ax[1, 1].axis("off")

plt.tight_layout()
plt.show()
