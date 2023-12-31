# MLP-notations

## What is this?
This is a project that relates to my compositional practice. The idea is to train an MLP network to generate $n$-dimensional notational parameter space from a 2-dimensional input $(x, y)$. This is a project in progress.
<br>
<br>
<p align="center">
<img width="646" alt="Screen Shot 2023-06-12 at 8 35 55 PM" src="https://github.com/hayakzan/MLP-notations/assets/61164329/722b5d78-b56d-41d6-9ac5-06eee9acc8c4"> 
</p>
<br>

## Creating training data
`MLP-notations_GENERATING DATA.ipynb` is used to generate new notations and prepare for the training.

The 2-dimensional input can be provided in an interactive way by using `/xy_data/for_training.py`. The code allows you to draw a path by clicking on a 2D space. This path is used as input features for the MLP network. Note that this code runs under a local Python environment (in lieu of a cloud-based environment).
<br>
<br>
<p align="center">  
<img width="489" alt="Screen Shot 2023-06-12 at 8 47 15 PM" src="https://github.com/hayakzan/MLP-notations/assets/61164329/a3b5eaae-abbe-40ab-898c-5907a7ff2d7c">
</p>  
<br>
Notational parameters are used as output features for the MLP network. At the moment, there are six notational parameters, controlling the durations between the notes, number of notes, pitch range, offsets in both dimensions, as well as rhythmic irregularity with a standard deviation value. When the SD = 0, the rhythmic pulse becomes regular. 
<br>
<br>
<p align="center">
<img width="397" alt="Screen Shot 2023-06-12 at 8 42 36 PM" src="https://github.com/hayakzan/MLP-notations/assets/61164329/a478952d-c539-48cb-a004-e676b8e80c5c">
</p>  
<br>
<p align="center">  
<img width="900" alt="example" src="https://github.com/hayakzan/MLP-notations/assets/61164329/7d0e6049-9b34-4be8-b715-b813ca7087c6">
</p>  
<br>

The number of points created with the 2-dimensional interface (`for_training.py`) and the number of notation excerpts created with this notebook (`MLP-notations_GENERATING DATA.ipynb`) should be equal. This can be checked within this notebook and the missing data can be added manually or via filling in random values (see the notebook).
<br>
The rest of the code uploads the files to Google Drive (permission required).
<br>

## Training & predicting
`MLP-notations_TRAINING-PREDICTING.ipynb` is used to train the network and to create new notational excerpts via inference. After training is performed with the data created in the previous notebook, the 2D input for prediction is processed. Similar to the 2D input features for the training data, input features for the prediction is created with an interactive interface run locally (`for_predicting.py`). 
<br>
<br>
<p align="center">  
<img width="489" alt="Screen Shot 2023-06-12 at 11 55 20 PM" src="https://github.com/hayakzan/MLP-notations/assets/61164329/6bf3a99f-4a8e-4de0-82c6-143f31d51f85">
</p>  
<br>
The model predicts a notational excerpt per each 2D input, and prints the results at the end. 
<br>

## Converting into MIDI/Waveform Audio File Format
`MLP-notations_CONVERSION.ipynb` is used to convert the resultant notational excerpts into MIDI and .wav files. The next step is to process the .wav files with networks with timbre-transfer capabilities.
