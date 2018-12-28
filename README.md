# PHYS250Final
Repository for Physics 250 final project on image classification in Fourier space

The goal of this project is to see if we can classify images in fourier space and also if we can improve the accuracy of the classification if we introduce various image transformations (particularly rotation and blurring). I used the MNIST dataset for the classification task. The model used is a simple feedforward network with two hidden layers. 

The results were surprising in that the fourier data did significantly worse than the regular data. However, after introducing the transformations, the fourier data did much better than without the transformations. 

Here is a link to a google drive containing the tensorboard logs with information on the plots of accuracy and validation and histograms of the weights and biases for each of the datasets: 

https://drive.google.com/open?id=1KoqMJi9Smpp8iL0lTNdekJAB2qhiWbP1
