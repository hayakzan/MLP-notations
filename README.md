# MLP-notations

## What is this?
This is an ongoing project that relates to my compositional practice. The idea is to train a MLP network to generate $n$-dimensional notational parameter space from a 2-dimensional input $(x, y)$.

<img width="646" alt="Screen Shot 2023-06-12 at 8 35 55 PM" src="https://github.com/hayakzan/MLP-notations/assets/61164329/722b5d78-b56d-41d6-9ac5-06eee9acc8c4">
<br>
<br>
<br>

## Creating training data
This 2-dimensional input can be provided in an interactive way by using `/xy_data/for_training.py`. The code allows you to draw a path by clicking on a 2D space. This path is used as input features for the MLP network. 
<br>
<br>
<img width="489" alt="Screen Shot 2023-06-12 at 8 47 15 PM" src="https://github.com/hayakzan/MLP-notations/assets/61164329/a3b5eaae-abbe-40ab-898c-5907a7ff2d7c">
    
<img width="251" alt="Screen Shot 2023-06-12 at 8 48 57 PM" src="https://github.com/hayakzan/MLP-notations/assets/61164329/029011e8-af8b-4b92-81a2-2afa5cf61117">
<br>
<br>
<br>
Notational parameters are used as output features for the MLP network. At the moment, there are 8 notational parameters, controlling the durations between the notes, number of notes, pitch range, offsets in both dimensions, as well as rhythmic irregularity with a standard deviation value. When the SD = 0, the rhythmic pulse becomes regular. 
<br>
<br>
<img width="397" alt="Screen Shot 2023-06-12 at 8 42 36 PM" src="https://github.com/hayakzan/MLP-notations/assets/61164329/a478952d-c539-48cb-a004-e676b8e80c5c">

The 
