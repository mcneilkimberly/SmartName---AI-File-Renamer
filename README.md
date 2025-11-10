# SmartName---AI-File-Renamer

SmartName is an AI File Renamer that analyzes user given files and renames them. The user may provide a casing style they prefer to have their filesnames follow. A guide to casing can be found in CASING_GUIDE.md located in this repository.

## Installation

First, download the rename_files.py.

Then, create a python environment (version 3.8+) to host all of your installations.

Activate your environment and use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following:
```bash
pip install requests
pip install argparse
pip install PyMuPDF
pip install python-docx
pip install python-pptx
pip install ffmpeg
```

We used models from [Ollama](https://ollama.com/), which you may download from their website. Once installed, activate ollama by either running the application on your system or via the following terminal code: 
```bash
ollama serve
```

The model our SmartName uses as a default is llama3.2-vision. You may either install this model or use another; we will show how to run SmartName using custum models in the Usage Section. To install a model from Ollama, visit their [model library](https://ollama.com/library) on their website and and paste the pull command from your chosen model in your terminal from before. Our [llama3.2-vision](https://ollama.com/library/llama3.2-vision)'s pull command is
```bash
ollama pull llama3.2-vision
```

Once you have everything installed and running, you can use SmartName.

## Usage

Using the termial with your activated environment and with ollama running, navigate to where smartname.py is, then call the following command to perform a dry run, using the path to the folder of files (or an individual file) you would like to rename (data\ is simply the name of the example folder):
```bash
python rename_files.py data/
```
A dry run is a preview mode for safety, as it is always important to test your files with the model and file naming before actually changing your filenames. The argument that will alter your actual files is discussed in the --execute section below. 

Now, let's get into the arguments to customize your experience

### directory
The first argument is required, and it is the directory of the file(s) you wish to rename. If you only provide the relative path, such as just the current folder or filename, ensure that the file is located in the same place that your terminal is currently accessing. If you are using the absolute path, ensure that the folders leading up to your target data folder, as well as this data folder, do not contain any spaces, as they will be read as later arguments

Examples include
```bash
python rename_files.py data/
python rename_files.py examplefile.md
python rename_files.py C:\Users\mememe\Downloads\Fall_2025_Sem\Human_AI\smartname\data\
python rename_files.py C:\Users\mememe\Downloads\Fall_2025_Sem\Human_AI\smartname\data\textpdf.pdf
```

### --execute
The execute argument will alter the files that you give this script. Without this argument, the script will default to a dry run, which will give a preview of what the files _would_ be named. 

Examples include
```bash
python rename_files.py data/ --execute
python rename_files.py C:\Users\mememe\Downloads\Fall_2025_Sem\Human_AI\smartname\data\textpdf.pdf --execute
```

### --model
The model argument will allow you to have a custom model. The default being used is llama3.2-vision, but if you have pulled another model and it is currently running, then you may use _--model modelname_ to change the model being used. 

Examples include
```bash
python rename_files.py data/ --model gemma3:4b
python rename_files.py C:\Users\mememe\Downloads\Fall_2025_Sem\Human_AI\smartname\data\textpdf.pdf --model granite3.3:2
```

In order to see what models you have, run the following command in your terminal
```bash
ollama list
```

### --case
The case argument will allow you to choose how the script will name your files. The six casing options can be found in CASING_GUIDE.md. If the argument is not given, the script will default to snake_case.

Examples include
```bash
python rename_files.py data/ --case snake
python rename_files.py data/ --case kebab
python rename_files.py data/ --case camel
python rename_files.py data/ --case pascal
python rename_files.py data/ --case lower
python rename_files.py data/ --case title
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

