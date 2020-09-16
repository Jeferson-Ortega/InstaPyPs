# Automate Instagram Post Creation with Python and Photoshop

Python script to generate Instagram posts based on a Photoshop template

## Preparing the Photoshop template

You can create your own designs using the Photoshop file in the *template* folder

The only required layers are *post-title* and *post-image*

## How to use 

1. Place your images in *content/images* folder

2. If you want to add texts to the images save a txt file with the same name of the image in *content/texts*. 

3. In the command-line run the file with the command 
    ````
    python photoshop.py
    ````
4. When the script finish running you can find the images inside the *generated/posts* folder