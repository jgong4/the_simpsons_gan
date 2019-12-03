# the_simpsons_gan
## GAN
### Data
###### Over 30k images collected
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

#### *500_epoch_frame_extracted*
500_epoch.gif splitted by each frame using https://ezgif.com/split
#### Sample Images
- 001/500 Epoch
![Sample Image 1](https://github.com/jgong4/the_simpsons_gan/blob/master/500_epoch_frame_extracted/frame_00_delay-0.2s.gif)
- 250/500 Epoch
![Sample Image 2](https://github.com/jgong4/the_simpsons_gan/blob/master/500_epoch_frame_extracted/frame_49_delay-0.2s.gif)
- 500/500 Epoch
![Sample Image 3](https://github.com/jgong4/the_simpsons_gan/blob/master/500_epoch_frame_extracted/frame_97_delay-0.2s.gif)
- 750 Epoch gif
![Final Result 750 Epochs](https://github.com/jgong4/the_simpsons_gan/blob/master/750_epoch.gif)

## GPT-2
### Data
#### *script.txt*
The Simpsons movie script obtained from https://simpsonswiki.com/wiki/The_Simpsons_Movie/Transcript

### Training
Train a GPT-2 Text-Generating Model w/ GPU For Free by Max Woolf (https://colab.research.google.com/drive/1VLG8e7YSEwypxU-noRNhsv5dW4NfTGce#forceEdit=true&sandboxMode=true&scrollTo=H7LoMj4GA4n)
Result was converted to an .mp3 file (gpt2_result.mp3) using https://ttsmp3.com/

## Final Product
The .gif file made from GAN and the .mp3 were combined using https://www.kapwing.com/
