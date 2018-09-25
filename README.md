## Project: Build a Traffic Sign Recognition Program

**Build a Traffic Sign Recognition Project**

The goals / steps of this project are the following:
* Load the data set (see below for links to the project data set)
* Explore, summarize and visualize the data set
* Design, train and test a model architecture
* Use the model to make predictions on new images
* Analyze the softmax probabilities of the new images
* Summarize the results with a written report


### Data Set Summary & Exploration

There are totally 42 types of traffic signs in the dataset. They dataset is heavily imbalanced as well based on the bar chart below.

[sign_labels.png](sign_labels.png)

I applied data normalization to train, validation, and test datasets by subracting 128.0 and dividing by 128.0 which was the recommendation according given in the notebook.

### Model Architecture

| Layer         		|     Description	        					| 
|:---------------------:|:---------------------------------------------:| 
| Input         		| 32x32x3 							| 
| Convolution 	| 1x1 stride, VALID padding, outputs 28x28x6 	|
| RELU					|												|
| Max pooling	      	| 2x2 stride,  outputs 14x14x6 				|
| Convolution     | 1 x 1 stride, VALID padding, outputs 10x10x16
| RELU    | |      									|
| Max pooling	      	| 2x2 stride,  outputs 5x5x6 |
| Flatten    | outputs 400 |  
| Flatten    | outputs 120 |  
| RELU    | |   
| Fully Connected    | outputs 84 |   
| RELU    | |   
| Fully Connected    | outputs 83 |

### Model Training
Created placed holders for X and y where

- X = input images
- y = output labels

For optimizing the difference between actual and predictions, I am using the following

- Activation = softmax, since we are doing multi classification
- Optimizer = Adam
- Loss fn = cross entropy

For training the model

- Batch size = 64
- Epoch count = 25

I tested multiple epochs and ended up using 16 because I was getting better training and validation accuracies at epoch=16

- Training set accuracy = 99 %
- Validation set accuracy = 92.9 %
- Random five images accuracy = 100 %
  
I tried LeNet architecture which was taught in the class and recommended in the notebook.

### Test model on new images

I pulled some images from official site and converted the ppm images to png images.

I got 100 % accuracy on all the test images. 


[00003.png](test_images/00003.png)

[00006.png](test_images/00006.png)

[00009.png](test_images/00009.png)

[00011.png](test_images/00011.png)

[00031.png](test_images/00031.png)

My prediction results are 

[prediction_results_on_5_test_images.png](test_images/prediction_results_on_5_test_images.png)

### Softmax probabilities for the above five test images

- No entry = 1.0
- Turn right ahead = 1.0
- Ahead only = 10.0
- General caution = 1.0
- Speed limit = 1.0
