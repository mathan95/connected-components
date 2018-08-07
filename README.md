# connected-components

This too done as a part of the project pest detection. The connected component inbuilt fuction in openCV is used here and I have made use of
it's outputs to complete some important tasks in my project.

A grayscale image is processed by this algorithm. The algorithm group the pixels to different components by using a 4-connectivity analysis and
then labels are obtained for each pixels representing their component number. This labels then used by me to find and remove un wanted noises and
to localizing and segmenting out the interested parts from the images.

This done after using green removal or k-cluster removal in my project. This can be used in many ways.

I used this for-

      To find and remove the noises in the image after gree removal. This is done by removing the components with number of 
      pixels in them less than a threshold.
      
      Also uses it to localize the necessary parts that had to processed as the last stage of the preprocessing for my project.
      
      
The files in the repository-

      k_means.py-  This file include the code for doing the green removal and then to seperate each connected components in the resulting image       
                   with number of pixels in them more than athreshold and each of them are displayed separately.
      
      k_means_with_connected_components2.py- This file include the code for green removal using k-cluster and then to separate each each        
                                             connected components in the resulting image with number of pixels in them more than athreshold 
                                             and each of them are displayed separately.
      
