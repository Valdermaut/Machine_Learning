import numpy as np
import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import *
from sklearn.metrics import confusion_matrix
from keras.preprocessing.image import img_to_array
import itertools
from IPython.display import display
from PIL import Image
import matplotlib.pyplot as plt
import cv2
import h5py
import cv2
import glob

class DataLoader:

    def __int__(self, folderpath):


        path =folderpath


        batches = ImageDataGenerator().flow_from_directory(
            path,
            target_size=(224, 224),
            classes=[
                'Pepper__bell___Bacterial_spot',
                'Pepper__bell___healthy',
                'Potato___Early_blight',
                'Potato___healthy',
                'Potato___Late_blight',
                'Tomato_Bacterial_spot',
                'Tomato_Early_blight',
                'Tomato_healthy',
                'Tomato_Late_blight',
                'Tomato_Leaf_Mold',
                'Tomato_Septoria_leaf_spot',
                'Tomato_Spider_mites_Two_spotted_spider_mite',
                'Tomato__Target_Spot',
                'Tomato__Tomato_mosaic_virus',
                'Tomato__Tomato_YellowLeaf__Curl_Virus'
             ],
             batch_size=10
        )


        # plots images with labels within jupyter notebook
        def plots(ims, figsize=(12,6), rows=1, interp=False, titles=None):

            if type(ims[0]) is np.ndarray:
                ims = np.array(ims).astype(np.uint8)
                if (ims.shape[-1] != 3):
                    ims = ims.transpose((0,2,3,1))
            f = plt.figure(figsize=figsize)
            cols = len(ims)//rows if len(ims) % 2 == 0 else len(ims)//rows + 1
            for i in range(len(ims)):
                sp = f.add_subplot(rows, cols, i+1)
                sp.axis('Off')
                if titles is not None:
                    sp.set_title(titles[i], fontsize=16)
                plt.imshow(ims[i], interpolation=None if interp else 'none')


        imgs, labels = next(batches)
        plots(imgs, titles=labels)


    
    def load_images_from_folder(self,folder):

        file1  = glob.glob (os.path.join(folder,'Pepper__bell___Bacterial_spot','*.JPG'))
        file2  = glob.glob (os.path.join(folder,'Pepper__bell___healthy','*.JPG'))
        file3  = glob.glob (os.path.join(folder,'Potato___Early_blight','*.JPG'))
        file4  = glob.glob (os.path.join(folder,'Potato___healthy','*.JPG'))
        file5  = glob.glob (os.path.join(folder,'Potato___Late_blight','*.JPG'))
        file6  = glob.glob (os.path.join(folder,'Tomato_Bacterial_spot','*.JPG'))
        file7  = glob.glob (os.path.join(folder,'Tomato_Early_blight','*.JPG'))
        file8  = glob.glob (os.path.join(folder,'Tomato_healthy','*.JPG')) 
        file9  = glob.glob (os.path.join(folder,'Tomato_Late_blight','*.JPG'))
        file10 = glob.glob (os.path.join(folder,'Tomato_Leaf_Mold','*.JPG'))
        file11 = glob.glob (os.path.join(folder,'Tomato_Septoria_leaf_spot','*.JPG'))
        file12 = glob.glob (os.path.join(folder,'Tomato_Spider_mites_Two_spotted_spider_mite','*.JPG'))
        file13 = glob.glob (os.path.join(folder,'Tomato__Target_Spot','*.JPG'))
        file14 = glob.glob (os.path.join(folder,'Tomato__Tomato_mosaic_virus','*.JPG'))
        file15 = glob.glob (os.path.join(folder,'Tomato__Tomato_YellowLeaf__Curl_Virus','*.JPG'))



    def saveDataToh5(self,datapath ):
        with h5py.File(os.path.join(datapath, 'main.h5'), 'a') as hdf:
            G = hdf.create_group('Group')
            X1_data=[]
            for myFile in file1:
                #print(myFile)
                image = cv2.imread (myFile)
                X1_data.append (image)
            X1_data=np.array(X1_data)
            G1 = hdf.create_group('G/Group1')
            G1.create_dataset('dataset1',data=X1_data)
            X1_data=[]
            
            for myFile in file2:
                #print(myFile)
                image = cv2.imread (myFile)
                X1_data.append (image)
            X1_data=np.array(X1_data)
            G2 = hdf.create_group('G/Group2')
            G2.create_dataset('dataset2',data=X1_data)
            X1_data=[]
            for myFile in file3:
                #print(myFile)
                image = cv2.imread (myFile)
                X1_data.append (image)
            X1_data=np.array(X1_data)
            G3 = hdf.create_group('G/Group3')
            G3.create_dataset('dataset3',data=X1_data)
            X1_data=[]
            for myFile in file4:
                #print(myFile)
                image = cv2.imread (myFile)
                X1_data.append (image)
            X1_data=np.array(X1_data)
            G4 = hdf.create_group('G/Group4')
            G4.create_dataset('dataset4',data=X1_data)
            X1_data=[]
            for myFile in file5:
                #print(myFile)
                image = cv2.imread (myFile)
                X1_data.append (image)
            X1_data=np.array(X1_data)
            G5 = hdf.create_group('G/Group5')
            G5.create_dataset('dataset5',data=X1_data)
            X1_data=[]
            for myFile in file6:
                #print(myFile)
                image = cv2.imread (myFile)
                X1_data.append (image)
            X1_data=np.array(X1_data)
            G6 = hdf.create_group('G/Group6')
            G6.create_dataset('dataset6',data=X1_data)
            X1_data=[]
            for myFile in file7:
                #print(myFile)
                image = cv2.imread (myFile)
                X1_data.append (image)
            X1_data=np.array(X1_data)
            G7 = hdf.create_group('G/Group7')
            G7.create_dataset('dataset7',data=X1_data)
            X1_data=[]
            for myFile in file8:
                #print(myFile)
                image = cv2.imread (myFile)
                X1_data.append (image)
            X1_data=np.array(X1_data)
            G8 = hdf.create_group('G/Group8')
            G8.create_dataset('dataset8',data=X1_data)
            X1_data=[]
            for myFile in file9:
                #print(myFile)
                image = cv2.imread (myFile)
                X1_data.append (image)
            X1_data=np.array(X1_data)
            G9 = hdf.create_group('G/Group9')
            G9.create_dataset('dataset9',data=X1_data)
            X1_data=[]
            for myFile in file10:
                #print(myFile)
                image = cv2.imread (myFile)
                X1_data.append (image)
            X1_data=np.array(X1_data)
            G10 = hdf.create_group('G/Group10')
            G10.create_dataset('dataset10',data=X1_data)
            X1_data=[]
            for myFile in file11:
                #print(myFile)
                image = cv2.imread (myFile)
                X1_data.append (image)
            X1_data=np.array(X1_data)
            G11 = hdf.create_group('G/Group11')
            G11.create_dataset('dataset11',data=X1_data)
            X1_data=[]
            for myFile in file12:
                #print(myFile)
                image = cv2.imread (myFile)
                X1_data.append (image)
            X1_data=np.array(X1_data)
            G12 = hdf.create_group('G/Group12')
            G12.create_dataset('dataset12',data=X1_data)
            X1_data=[]
            for myFile in file13:
                #print(myFile)
                image = cv2.imread (myFile)
                X1_data.append (image)
            X1_data=np.array(X1_data)
            G13 = hdf.create_group('G/Group13')
            G13.create_dataset('dataset13',data=X1_data)
            X1_data=[]
            for myFile in file14:
                #print(myFile)
                image = cv2.imread (myFile)
                X1_data.append (image)
            X1_data=np.array(X1_data)
            G14 = hdf.create_group('G/Group14')
            G14.create_dataset('dataset14',data=X1_data)
            X1_data=[]
            for myFile in file15:
                #print(myFile)
                image = cv2.imread (myFile)
                X1_data.append (image)
            X1_data=np.array(X1_data)
            G15 = hdf.create_group('G/Group15')
            G15.create_dataset('dataset15',data=X1_data)

