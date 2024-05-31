# MLP-notations

## What is this?
This is a project that relates to my compositional practice. The idea is to train an MLP network to generate $n$-dimensional notational parameter space from a 3-dimensional input $(x, y, z)$.
<br>
<br>
<p align="center">
<img width="847" alt="Screen Shot 2024-05-30 at 8 08 57 PM" src="https://github.com/hayakzan/MLP-notations/assets/61164329/a4ea71d8-7ef2-4cf1-ba77-6d9628918e44">
</p>
<br>

`MLP_notations_generate.ipynb` is used to generate notations as dataset. The training and testing data provided here in `/data/train_xyz.json` and `/data/predict_xyz.json` is small, and only for a quick demonstration. 

<br>
The training data (i.e. `/data/train_xyz.json`) and testing data (i.e. `/data/predict_xyz.json`) can be created via adding points in a 3D space by using `MLP-notation datasets.ipynb`. As for now, `MLP-notation datasets.ipynb` only works under a local Python environment such as JupyterLab due to its callback functions.
<br>
<br>
<p align="center">
<img width="521" alt="Screen Shot 2024-05-30 at 9 11 03 PM" src="https://github.com/hayakzan/MLP-notations/assets/61164329/a6d5272e-488c-4d15-8478-b2dd96ebcb57">
</p>
<br>

As the 3D points provide input features, the notational parameters constitute output features for the MLP network. At the moment, there are 25 notational parameters. 
