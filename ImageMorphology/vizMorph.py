import cv2
import numpy as np

# Load the image
src = cv2.imread('../ImageRepresentation/images/brick.jpeg')
# Create a window to attach trackbars
title_window = 'Morphology Operations'
cv2.namedWindow(title_window)

# Specify the morphological operations and Structuring elements
morph_op_dic = {0: 'ERODE', 1: 'DILATE', 2: 'OPEN', 3: 'CLOSE', \
                4: 'GRADIENT', 5: 'TOPHAT', 6: 'BLACKHAT', 7: 'HITMISS'}
element_dic = {0: 'RECT', 1: 'CROSS', 2: 'ELLIPSE'}

# Define callback function
def morphology_operations(val):
    # get current trackbar position
    morph_operator = cv2.getTrackbarPos('Operator', title_window)
    kernel_size = cv2.getTrackbarPos('kernel', title_window)
    val_type = cv2.getTrackbarPos('SE', title_window)
    iter_num = cv2.getTrackbarPos('iterations', title_window)
    # create structuring element
    element = cv2.getStructuringElement(val_type, (2*kernel_size + 1, 2*kernel_size+1))
    # apply morphological operation
    dst = cv2.morphologyEx(src, morph_operator, element,iterations=iter_num)
    # Display the operation and structuring element
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(dst,'Op:{}, SE: {}'.format(morph_op_dic[morph_operator],element_dic[val_type]),(10,40), font, 0.5,(0,255,255),1,cv2.LINE_AA)
    cv2.imshow(title_window, dst)
    
# Create Trackbars
cv2.createTrackbar('Operator', title_window , 0, 7, morphology_operations)
cv2.createTrackbar('SE', title_window , 0, 2, morphology_operations)
cv2.createTrackbar('kernel', title_window , 0, 10, morphology_operations)
cv2.createTrackbar('iterations', title_window , 0, 10, morphology_operations)

# Instantiate the function
morphology_operations(0)
cv2.waitKey(0)
