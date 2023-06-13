# MLP-notations

## What is this?
This is a project that relates to my compositional practice. The idea is to train an MLP network to generate $n$-dimensional notational parameter space from a 2-dimensional input $(x, y)$. Please note that this is an ongoing project.
<br>
<br>
<p align="center">
<img width="646" alt="Screen Shot 2023-06-12 at 8 35 55 PM" src="https://github.com/hayakzan/MLP-notations/assets/61164329/722b5d78-b56d-41d6-9ac5-06eee9acc8c4"> 
</p>
<br>

## Creating training data
MLP-notations_GENERATING DATA.ipynb is used to generate new notations and prepare for the training.

The 2-dimensional input can be provided in an interactive way by using `/xy_data/for_training.py`. The code allows you to draw a path by clicking on a 2D space. This path is used as input features for the MLP network. Note that this code runs under a local Python environment (in lieu of Colab).
<br>
<br>
<p align="center">  
<img width="489" alt="Screen Shot 2023-06-12 at 8 47 15 PM" src="https://github.com/hayakzan/MLP-notations/assets/61164329/a3b5eaae-abbe-40ab-898c-5907a7ff2d7c">
</p>  
<br>
Notational parameters are used as output features for the MLP network. At the moment, there are 8 notational parameters, controlling the durations between the notes, number of notes, pitch range, offsets in both dimensions, as well as rhythmic irregularity with a standard deviation value. When the SD = 0, the rhythmic pulse becomes regular. 
<br>
<br>
<p align="center">
<img width="397" alt="Screen Shot 2023-06-12 at 8 42 36 PM" src="https://github.com/hayakzan/MLP-notations/assets/61164329/a478952d-c539-48cb-a004-e676b8e80c5c">
</p>  
<br>
<p align="center">  
<img width="900" alt="Notation excerpt" src="https://github.com/hayakzan/MLP-notations/assets/61164329/407a6857-72cf-4d29-a0f4-07b8658c1b2e">
</p>  
<br>
The number of points created with the 2-dimensional interface (`for_training.py`) and the number of notation excerpts created with this notebook (`MLP-notations_GENERATING DATA.ipynb`) should be equal. This can be checked within this notebook and the missing data can be added manually or via filling in random values (see the notebook).
<br>
The rest of the code uploads the files to Google Colab (permission required).
<br>

## Training & predicting
MLP-notations_TRAINING-PREDICTING.ipynb is used to train the network and to create new notational excerpts via inference. After training is performed with the data created in the previous notebook, the 2D input for prediction is processed. Similar to the 2D input features for the training data, input features for the prediction is created with an interactive interface run locally (`for_predicting.py`). 
<br>
<p align="center">  
<img width="468" alt="Screen Shot 2023-06-12 at 9 36 17 PM" src="https://github.com/hayakzan/MLP-notations/assets/61164329/101a1848-021d-49d8-9bbe-fb90cff763f7">
</p>  
<br>
The model predicts a notational excerpt per each $(x, y)$ input, and prints the results at the end. The next step involves transforming these first into MIDI files, then into .wav files in order to process them with networks with timbre-transfer capabilities.

