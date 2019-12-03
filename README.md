# the_simpsons_gan

### Data
#### *bbid.py*
Bulk Bing Image Downloader
Obtained from https://github.com/ostrolucky/Bulk-Bing-Image-downloader.git
*bbid.py* was used to download images from Bing using *search_input.txt*.
```
python3 bbid.py -f search_input.txt
```

#### *The Simpsons Characters Data*
Obtained from https://www.kaggle.com/alexattia/the-simpsons-characters-dataset/download

### Preprocessing
*preprocess.py* goes through every image and shapes each to 300x300 pixels

### Training
#### *gan.py*
Obtained and modified from PyTorch DCGAN Tutorial (https://pytorch.org/tutorials/beginner/dcgan_faces_tutorial.html)
- This saves a plot of generator loss and discriminator loss for a given number of epochs.
- This also saves a gif of 64 sample images (in 8x8 grid) over the course of training (fps = 5).

Approximate training time with one CUDA 10.0 in a Brown CS department machine:
- 150 epochs: ~ 1.5 hours
- 500 epochs: ~ 5 hours
- 750 epochs: ~ 8 hours

#### *500_epoch_frame_extracted.zip*
500_epoch.gif splitted by each frame using https://ezgif.com/split
