# image_caption_generator

This was a program i made to learn more about how CV and ML can be utilized in various applications

<h2>Installation</h2>
<ul>
  <li>clone the repo</li>
  <li>Download the Flickr8k dataset: https://github.com/jbrownlee/Datasets/releases/download/Flickr8k/Flickr8k_Dataset.zip</li>
  <li>use pip to install requirements</li>
</ul>

<h2>Usage</h2>

<h3>I just want to run the program</h3>
<ul>
  <li>
    Run the caption_generator file.<br>
    This will automatically use the model found in the <code>models</code> folder
  </li>
</ul>
<br>
<h3>I want to train my own model</h3>
 
In addition to the Flickr8k Dataset you will also need to download the captions for the images:
Flickr8k_text.zip https://github.com/jbrownlee/Datasets/releases/download/Flickr8k/Flickr8k_text.zip

<ul>
  <li>Run the model_trainer file.</li>
 <li> The model will automatically be saved to the <code>models</code> folder and be named <code> model_x.h5 </code> where x is the amount of epochs.<br>
  If you want to change the model name you can do so at the bottom of the note book in the model.save function by replacing <code>model_</code>
  with your desired name.</li>
  <li> the notebook is finished, change the model path in the caption_generator file to your saved model and run the file.</li>
</ul>
