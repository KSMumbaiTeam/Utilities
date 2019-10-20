from glob import glob                                                           
import cv2 
import os 

# Image path 
image_path = glob('F:\ChinaSet_AllFiles\CXR_png\*.png')

# Image directory 
directory = 'E:\png_to_jpg_dataset'

try:
    for j in image_path:
        print(j[29:])
        filename = j[29:] 
        img = cv2.imread(j)
        print(directory+os.sep+filename[:-4]+ '-.jpg')
        cv2.imwrite(directory+os.sep+filename[:-4]+ '.jpg', img)
except:
    print('exception')
    
print('Successfully saved') 
