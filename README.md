# connected-components

This too done as a part of the project pf pest detection. The connected component inbuilt fuction in openCV is used here to
find the components with higher number of pixels with them.

A grayscale image is processed by this algorithm. The algorithm group the pixels to different components by using a 4-connectivity analysis and
then labels are obtained for each pixels representing their component number. This labels then used by me to find and remove un wanted noises and
to localizing and segmenting out the interested parts from the images.

This done after using green removal or k-cluster removal in my project. This can be used in many ways.

I used this for-

      To find and remove the noises in the image after gree removal. This is done by removing the components with number of 
      pixels in them less than a threshold.
      
      Also uses it to localize the necessary parts that had to processed as the last stage of the preprocessing for my project.
