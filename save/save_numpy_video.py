# save numpy video
import numpy as np
import cv2

for j in range(2,48):
    training_data = np.load("training_data/training_data-"+str(j)+".npy",allow_pickle=True)


    img_array = []

    for i in range(len(training_data)):
        # print(img[0][0])
        img_array.append(training_data[i][0])
        cv2.imwrite("screenshots/training_data_"+str(i)+".jpg",training_data[i][0])
        filename = 'screenshots/training_data_'+str(i)+'.jpg'
        img = cv2.imread(filename)
        img_array.append(img)
 
    size = (480, 270)

    # out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
        
    out = cv2.VideoWriter('project'+str(j)+'.mp4',cv2.VideoWriter_fourcc(*'MP4V'), 15, size)
    
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()