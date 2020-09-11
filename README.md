# text_summarization

This repo is used for abstractive text summarization. The model has to be downloaded first

```
wget https://drive.google.com/file/d/1-Gck6Qu1v0DvDelkPMXVX5fv8glgPbAa/view?usp=sharing
```
unzip the file and copy the path to the model folder(this contains both the model fiels and tokenizer files) in the constants.yaml file

Install the requirements using
```
pip install -r requirements.txt
```
Run the main file for getting the summarization using API.
``` 
Note:- This api will automatically make use of gpu if CUDA is installed or the model will use cpu

```
