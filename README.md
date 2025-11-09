# SmartName---AI-File-Renamer

Work in Progress :D


SmartName is an AI File Renamer that analyzes user given files and renames them. The user may provide a casing style they prefer to have their filesnames follow. A guide to casing can be found in CASING_GUIDE.md located in this repository.

## Installation

Create a python environment to host all of your installations. We used Python version ______________.

Activate your environment and use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following:
```bash
pip install requests
pip install argparse
pip install PyMuPDF
pip install python-docx
pip install python-pptx
pip install ffmpeg
pip install
pip install 
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

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
