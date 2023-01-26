# image_caption_generator

This was a program i made to learn more about how CV and ML can be utilized in various applications

<h2>Installation</h2>
<ul>
  <li>clone the repo</li>
  <li>use pip to install requirements</li>
</ul>

<h2>Usage</h2>

<h3>I just want to run the program</h3>
If you just want to run the program then you just need to run the caption_generator file.
This will automatically use the model found in the __models__ folder<br>

<h3>I want to train my own model</h3>
If you want to train your own model and test it, run the model_trainer file.
The model will automatically be named <code> model_x.h5 </code> where x is the amount of epochs and are automaticallyt saved to the <code>models</code> folder.
If you want to change the model name you can do so at the bottom of the note book in the model.save function by replacing <code>model_</code>
with your desired name
Once the notebook is finished, change the model path in the caption_generator file to your saved model and run the file.
