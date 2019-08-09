import csv,os,cv2

def convert_img_to_csv(img_dir):
    #Path to the new CSV file
    with open('/Users/johnson/Desktop/Research/Phase3/MNIST/Test.csv',"w",newline="") as f:
        #Set up CSV columns
        column_name = ["label"]
        column_name.extend(["pixel%d"%i for i in range(92*112)])
        writer = csv.writer(f)
        writer.writerow(column_name)
        #There are 40 folders in Phase 2
        #This directory contains a set of faces taken between April 1992 and
        # April 1994 at the Olivetti Research Laboratory in Cambridge, UK.
        for i in range(1,4):
            #Get the directories
            x = [img_dir,'/s',str(i)]
            folder = ''.join(x)
            print ("Path:",folder)
            img_list = os.listdir(folder)
            #Loop thru all images
            for img_name in img_list:
                #Discard all subfolders
                if not os.path.isdir(img_name):
                    print ("Image:",img_name)
                    img_path = os.path.join(folder,img_name)
                    #CV2.imread_grayscale (1) doesn't work here since we are reading .pgm
                    #img = cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)
                    #We need -1 instead
                    img = cv2.imread(img_path,-1)
                    cv2.imshow('Image', img)
                    cv2.waitKey(0)
                    #img = Image.open(img_path)
                    #img.show()
                    #lines = img.readlines()
                    #for l in list(lines):

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
