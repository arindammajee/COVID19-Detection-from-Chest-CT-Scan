This is my second Image Classification project using CNN. I have used a dataset which I have got from Harvard University’s site. 

Required Libraries:
1. Numpy
2. os
3. Matplotlib
4. Tensorflow & keras
5. sklearn
I haven’t use any kind of CSV file. If you use the CSV file named ‘data.csv’, you also need ‘pandas’ library. I have created this CSV file by writting a python code and running it on my machine. You can also generate the CSV file by running the same python script.
Creating Dataset
At first I download the dataset from havar University Dataset. To dowload the dataset go to the below link:
https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi%3A10.7910%2FDVN%2FSZDUQX
The dataset named covid_ctscan.zip in the website is in .zip format. I have extracted it inside the folder name ‘Dataset’. There are three
 different folder named ‘Covid’, ‘Healthy’ & ‘Others’ inside the folder ‘New_data_cov2’ inside the folder ‘covid_ctscan’. Inside the
  ‘Covid’ folder, there are some directories in which images of covid patiant’s brains CT Scan are kept. Simillarly the images of brain’s CT Scan of healthy patiants and paitaints infected with diseases other than covid are kept in different directories inside the folder ‘Healthy’ and ‘Others’ folder respectively.
Showing some of Images:


Loading Images and labels.
At first I have loaded location of all the images and their respective labels. To do this I have used os library. I have loaded these things in two different arrays named ‘image_name’ and ‘image_label’. After that I load the images in Numpy arrays. To load the images I have used OpenCV. You can also use matplotlib.image or PIL or scikit-image for loading images with which you are comfortable.
There are total 4171 images among them 2000 images belong to Covid patiants, 1000 belong to Healthy pataints and 1000 belong to Others patiants.
Train and Test Dataset
To divide the dataset in train and test dataset, I have used sklearn.spllit_train_test function. I divide the dataset in a ratio of 0.85 and 0.15 . The number of train images is 3545 and test images is 626.
Creating the model
I have used keras Sequential model for this and ‘relu’ and ‘softmax’ as Activation function and SGD as optimizer. You can try
yourself with different optimizer and different Activation function. The summary of my model is:
Model: "sequential_1"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_1 (Conv2D)            (None, 32, 32, 32)        896       
_________________________________________________________________
activation_1 (Activation)    (None, 32, 32, 32)        0         
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 16, 16, 32)        0         
_________________________________________________________________
dropout_1 (Dropout)          (None, 16, 16, 32)        0         
_________________________________________________________________
flatten_1 (Flatten)          (None, 8192)              0         
_________________________________________________________________
dense_1 (Dense)              (None, 512)               4194816   
_________________________________________________________________
activation_2 (Activation)    (None, 512)               0         
_________________________________________________________________
dropout_2 (Dropout)          (None, 512)               0         
_________________________________________________________________
dense_2 (Dense)              (None, 256)               131328    
_________________________________________________________________
activation_3 (Activation)    (None, 256)               0         
_________________________________________________________________
dropout_3 (Dropout)          (None, 256)               0         
_________________________________________________________________
dense_3 (Dense)              (None, 3)                 771       
_________________________________________________________________
activation_4 (Activation)    (None, 3)                 0         
=================================================================
Total params: 4,327,811
Trainable params: 4,327,811
Non-trainable params: 0
_________________________________________________________________
________________________________________________________________
Training the Model
To train the model I have created batches with batch size 8. And set the number of epochs as 10 . It took approximate 3–4 minutes to train the model. Each epoch took approximate 20s to 25s. In every epoch it prints the loss and accuracy. Among the 3545 images of train set, 3013 images are used to train the model and 532 images are used to validate the model.
Accuracy of the CNN model:
I have got a accuracy of 0.7124 on Validation set and 0.7492 on Test set.
The accuracy can be increased by changing BATCH_SIZE, increasing number of images in datset, changing optimizer etc.
Prediction:
To predict the label of a new CT Scan image I have created a function named ‘label_prediction’. I have also created a function named ‘plot_prediction’ which will plot a bar graph of the predictions.
Here is the prediction bar graph of the image X_test[0].


Feel free to fork or download and work on it from my Github Repository. To improve my CNN model, feel free to create an issue or make a pull request in my github repository. Any kind of suggestion is acceptable.
Thanks a lot for reading.


