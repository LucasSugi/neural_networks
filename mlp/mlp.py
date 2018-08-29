'''
Author: Lucas Yudi Sugi - 9293251
Discipline: SCC0270 - Introducao a Redes Neurais 
Title: Recognize A and A inverted with Adaline
'''

import numpy as np
import random as rd

#Activation function - Sigmoid
def activaction_function(net):
    return 1/(1+(np.exp(-net)))

#Multilayer-Perceptron Architecture
def mlp_architecture(data,hidden_length,output_length):

    #Size data
    row,col = data.shape
    
    #Create and populate the weigths of hidden layer
    hidden_weights = np.zeros([hidden_length,col])
    for i in range(hidden_length):  
        for j in range(col):
            hidden_weights[i][j] = rd.uniform(-0.5,0.5)


    #Create and populate the weigths of output layer
    output_weights = np.zeros([output_length,hidden_length+1])
    for i in range(output_length):
        for j in range(hidden_length+1):
            output_weights[i][j] = rd.uniform(-0.5,0.5)

    return hidden_weights,output_weights


#Normalizing
def normalizing(data):
    
    #Size data
    row,col = data.shape

    for i in range(1,col):
        data[:,i] = (data[:,i] - min(data[:,i]))/(max(data[:,i])-min(data[:,i]))
    return data

#Multilayer-Perceptron Forward
def mlp_forward(tuple_data,hidden_weights,output_weights):
    
    #Computes the net and f(net) - Hidden
    net_h = np.sum(np.multiply(tuple_data,hidden_weights),axis=1)
    f_h = activaction_function(net_h)

    #Set the theta
    temp_f_h = np.append(f_h,1)

    #Computes the net and f(net) - Output
    net_o = np.sum(np.multiply(temp_f_h,output_weights),axis=1)
    f_o = activaction_function(net_o)
        
    return net_h,f_h,net_o,f_o


#Multilayer-Perceptron Backward
def mlp_backward(data,hidden_weights,output_weights):

    #Extract class
    temp_classes = np.unique(data[:,0])
    
    #Create classes for each neuron
    classes = np.zeros([data.shape[0],len(temp_classes)])
    
    #Populate class
    temp_data = data[:,0]
    for i in range(len(temp_classes)):
        for j in range(len(temp_data)):
            if(temp_classes[i] == temp_data[j]):
                classes[j,i] = 1
    
    #Extract the attributes and set theta
    attributes = np.copy(data)
    attributes[:,0] = 1
    
    #Conditions of stop
    threshold = 1e-2
    sqerror = 2 * threshold
    while(sqerror > threshold):
        sqerror = 0

        #For each row verify apply the forward and backpropagation
        for i in range(attributes.shape[0]):
            net_h,f_h,net_o,f_o = mlp_forward(attributes[i,:],hidden_weights,output_weights)

            #Calculates the error
            error = classes[i,:] - f_o

            #Squared error
            sqerror =  sqerror + np.sum((error*error))

            #Backpropagation

        sqerror = sqerror / attributes.shape[0]
        print(sqerror)
        sqerror = -1

#Read the data that will be used in ml
def readData():
    
    #Read the name or path of data
    pathData = str(input()).rstrip()

    #Number of neurons hidden layer
    hidden_length = int(input())

    #Number of neurons output layer
    output_length = int(input())

    #Load data
    return np.genfromtxt(pathData, delimiter=","),hidden_length,output_length
    

#Call for read data
data,hidden_length,output_length = readData();

#MLP - Architecture
hidden_weights, output_weights = mlp_architecture(data,hidden_length,output_length);

#Normalizing data
data = normalizing(data)

#MLP - Backward
mlp_backward(data,hidden_weights,output_weights)
