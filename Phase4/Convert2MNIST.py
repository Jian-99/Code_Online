#Author: Jian Gao
#Date: July, 2019
#University of British Columbia
#All rights reserved

import csv,os,cv2

def Convert_img_to_csv(img_dir):
    #Path to the new CSV file
    with open('/Users/johnson/Desktop/Research/Phase4/MNIST/Train.csv',"w",newline="") as file:
        #Set up CSV columns
        column_name = ["label"]
        column_name.extend(["pixel%d"%i for i in range(168*192)])
        writer = csv.writer(file)
        writer.writerow(column_name)
        #There are 40 folders in Phase 2
        # This directory contains a set of faces taken between April 1992 and
        # April 1994 at the Olivetti Research Laboratory in Cambridge, UK.
        for i in range(1,10):
            #Get the directories
            folder = Path(i,img_dir)
            img_list = os.listdir(folder)
            #Loop thru all images
            for img_name in img_list:
                #Discard all subfolders
                if not os.path.isdir(img_name):
                    #Discard all non-pgm files
                    if os.path.splitext(img_name)[1] == '.pgm':
                        print ("Image:",img_name)
                        img_path = os.path.join(folder,img_name)
                        #CV2.imread_grayscale (1) doesn't work here since we are reading .pgm
                        #img = cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)
                        #We need -1 here instead
                        img = cv2.imread(img_path,-1)
                        
                        #Reduce the noice using GaussianBlur
                        blurred = cv2.GaussianBlur(img,(3,3),0)
                        #Detect edges
                        img = cv2.Canny(blurred,55,120,apertureSize = 3)

                        #cv2.imshow('Image', img)
                        #cv2.waitKey(0)

                        #Label of the row
                        row_data = [i]
                        #Capture the pixels
                        row_data.extend(img.flatten())
                        #Write to CSV
                        writer.writerow(row_data)
    #Writing process completed
    print ("All Good")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Path(i,img_dir):
    if (i<10):
        x = [img_dir,'/yaleB0',str(i)]
    else:
        x = [img_dir,'/yaleB',str(i)]
    folder = ''.join(x)
    print ("Path:",folder)
    return folder

def Convert_test():
    with open('/Users/johnson/Desktop/Research/Phase4/Test/Test.csv',"w",newline="") as file:
    #Set up CSV columns
        column_name = (["pixel%d"%i for i in range(0,1)])
        column_name.extend(["pixel%d"%i for i in range(1,168*192)])
        writer = csv.writer(file)
        writer.writerow(column_name)
        folder = './Test'
        img_list = os.listdir(folder)
        #Loop thru all images
        for img_name in img_list:
            if os.path.splitext(img_name)[1] == '.pgm':
                print ("Image:",img_name)
                img_path = os.path.join(folder,img_name)
                img = cv2.imread(img_path,-1)
                blurred = cv2.GaussianBlur(img,(3,3),0)
                img = cv2.Canny(blurred,55,120,apertureSize = 3)
                row_data = (img.flatten())
                writer.writerow(row_data)
