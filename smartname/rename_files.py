"""

"""
import argparse
import os
import requests
import base64


# CLI - Command-Line Interface
def main():
    """
    Command-line interface for smart file renaming using Ollama AI models
      Dry run (preview): python rename_files.py data/
      Execute renaming: python rename_files.py data/ --execute
      Custom model: python rename_files.py data/ --model modelname
    """
    
    # Create argument parser object
    parser = argparse.ArgumentParser(
        description='Smart file renaming tool using Ollama AI models'
    )

    # Add directory argument
    parser.add_argument(
        'directory',
        type=str,
        help='Directory containing files to rename'
    )

    # Add execute flag
    parser.add_argument(
        '--execute',
        action='store_true', # defaults to False when --execute is not included (for dry-run mode)
        help='Execute the renaming. If not set, performs a dry run'
    )

    # Add model selection argument
    parser.add_argument(
        '--model',
        type=str,
        default='llama3.2-vision',
        help='Specify the Ollama model to use (default: llama3.2-vision)'
    )

    # Add casing style argument
    parser.add_argument(
        '--case',
        type=str,
        default='snake',
        choices=['snake', 'kebab', 'camel', 'pascal', 'lower', 'title'],
        help='Casing style for new filenames (default: snake)'
    )

    # Parse arguments
    args = parser.parse_args()

    # Does the directory exist?
    if not os.path.isdir(args.directory):
        print(f"Error: Directory '{args.directory}' does not exist")
        return

    # Print mode (dry run or execute)
    mode = "EXECUTE" if args.execute else "DRY RUN"
    print(f"\nMode: {mode}")
    print(f"Using model: {args.model}")
    print(f"Casing style: {args.case}")
    print(f"Directory: {os.path.abspath(args.directory)}\n")
    
    # Process all files in the directory
    for filename in os.listdir(args.directory):
      file_path = os.path.join(args.directory, filename)
      
      # Skip if it's not a file
      if not os.path.isfile(file_path):
        continue
          
      # Get the file extension
      name, ext = os.path.splitext(filename)
      
      # Generate new filename
      suggested_name = generate_filename_for_file(file_path, args.model)
      
      # If a suggestion was made, proceed to rename
      if suggested_name:
        # Apply casing and sanitization
        suggested_name = sanitize_filename(suggested_name)
        suggested_name = apply_casing(suggested_name, args.case)
        
        # Add back the extension
        new_filename = f"{suggested_name}{ext}"
        new_file_path = os.path.join(args.directory, new_filename)
        
        # Print the proposed change
        print(f"'{filename}' -> '{new_filename}'")
        
        # Execute the rename if in execute mode
        if args.execute:
          try:
            os.rename(file_path, new_file_path)
            print("Renamed successfully!")
          except Exception as e:
            print(f"Error renaming: {e}")
      
      # Otherwise, skip file, as no suggestion was made due to unsupported type or error
      else:
        print(f"Skipping '{filename}' - unsupported file type or error in processing")

    # Print mode (dry run or execute)
    mode = "DRY RUN" 
    if args.execute:
      mode = "EXECUTE"  
    
    print(f"\nMode: {mode}")
    print(f"Using model: {args.model}")
    print(f"Directory: {os.path.abspath(args.directory)}\n")



# API - Application Programming Interface
def call_ollama_vision(image_path: str, model: str) -> str:
  """
  Call Ollama's vision model to analyze an image and suggest a filename.
  Returns: string of suggested filename (without extension)
  """

  # Read and encode the image
  with open(image_path, 'rb') as image_file:
    b64 = base64.b64encode(image_file.read()).decode('utf-8')
  
  # Prepare the API request
  url = "http://localhost:11434/api/generate"
  payload = {
    "model": model,
    "prompt": "Analyze this file's content and suggest a concise, 5-8 word, descriptive filename that captures its main content. " + 
              "Respond with *ONLY* the filename suggestion with *NO* additional text or explanation. Do *NOT* include a file extension.",
    "images": [b64],
    "stream": False
  }
  
  try:
    response = requests.post(url, json=payload)

    if response.status_code == 200:
      result = response.json()
      # Clean up the response to get just the filename suggestion
      suggested_name = result['response'].strip()
      return suggested_name
    else:
      print(f"Error: API call failed with status code {response.status_code}")
      return None
  except Exception as e:
    print(f"Error calling Ollama API: {e}")
    return None


# API - Application Programming Interface 
def call_ollama_text(file_path: str, model: str) -> str:
  """
    Call Ollama's text model to analyze an text/code file and suggest a filename.
    Returns: string of suggested filename (without extension)
    """
  # Read the text content
  with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
    text_content = f.read()

  # Prepare the API request
  url = "http://localhost:11434/api/generate"
  payload = {
    "model": model,
    "prompt": "Analyze this file's content and suggest a concise, 5-8 word, descriptive filename that captures its main content. " + 
              "Respond with *ONLY* the filename suggestion with *NO* additional text or explanation. Do *NOT* include a file extension." + 
              "\n\nFile Content:\n{text_content}",
    "stream": False
  }

  # Call the API
  try:
    response = requests.post(url, json=payload)

    if response.status_code == 200:
      result = response.json()
      # Clean up the response to get just the filename suggestion
      suggested_name = result['response'].strip()
      return suggested_name
    else:
      print(f"Error: API call failed with status code {response.status_code}")
      return None
  except Exception as e:
    print(f"Error calling Ollama API: {e}")
    return None


# Extractor
def extract_pdf_image():
  print("PDF extraction not implemented yet")


# Extractor
def extract_docx_content():
  print("DOCX extraction not implemented yet")


# Extractor
def extract_pptx_content():
  print("PPTX extraction not implemented yet")


# Extractor
def extract_video_frame():
  print("Video frame extraction not implemented yet")


# Extractor
def read_text_snippet():
  print("Text snippet reading not implemented yet")


# Routing
def generate_filename_for_file(file_path: str, model: str) -> str:
  """
  Generate a new filename based on the file type and content.
  Returns: string of suggested filename (without extension)
  """
  # Get the file extension
  _, ext = os.path.splitext(file_path)
  ext = ext.lower()
  
  # Route based on file type

  # Image files
  if ext in ('.png', '.jpg', '.jpeg', '.webp', '.gif'):
    result = ("image", file_path)  # direct pass-through for image files
  # Text/Code - based files
  elif ext in ('.txt', '.md', '.csv', '.json', '.xml', '.py', '.java', '.c', '.cpp', '.html', '.css', '.js', '.ipynb'):
    result = ("text", file_path)  # direct pass-through for text/code files
  # PDF files
  # elif ext == '.pdf':
  #   result = extract_pdf_image(file_path)
  # # DOCX files
  # elif ext in ('.docx',):
  #   result = extract_docx_content(file_path)
  # # PPTX files
  # elif ext in ('.pptx',):
  #   result = extract_pptx_content(file_path)
  # # Video files
  # elif ext in ('.mp4', '.mov', '.avi'):
  #   result = extract_video_frame(file_path)
  # Other text files (we're not handling these)
  else:
    return None
  
  if not result:
    return None

  # Take media type and call corresponding Ollama function
  media, payload = result
  if media == "image":
    suggested = call_ollama_vision(payload, model) # payload is image path
  elif media == "text":
    suggested = call_ollama_text(payload, model) # payload is text path
  else:
    suggested = None

  return suggested


# UX - User Experience
def apply_casing(text: str, case_style: str) -> str:
    """
    Apply the specified casing style to the text.
        text (str): Input text to transform
        case_style (str): One of 'snake', 'kebab', 'camel', 'pascal', 'lower', 'title'
    Returns: a string transformed text in the specified case style
    """

    # First, normalize the text by splitting into words
    # Convert to lowercase and split on spaces, dashes, underscores, or camel case boundaries    
    words = [] # List to hold the extracted words
    current_word = "" # Temporary variable to build the current word
    
    # For each character in the text
    for i, char in enumerate(text):
        
        # Split on spaces, dashes, and underscores
        if char.isspace() or char in ['-', '_']:
            # Check that current_word is not empty
            if current_word:
                # Append the current word (lowercase) to words list and reset current_word
                words.append(current_word.lower())
                current_word = ""
        
        # Split on camel case boundaries (uppercase letter directly following a lowercase letter)
        elif char.isupper() and i > 0 and text[i-1].islower():
            # Check that current_word is not empty
            if current_word:
                # Append the current word (lowercase) to words list and reset current_word
                words.append(current_word.lower())
                current_word = char
        
        # Otherwise, continue building the current word (because it's part of the same word)
        else:
            current_word += char
    
    # Append the last word if exists
    if current_word:
        words.append(current_word.lower())
    
    # Apply the requested case style
    if case_style == 'snake':
        return '_'.join(words)
    elif case_style == 'kebab':
        return '-'.join(words)
    elif case_style == 'camel':
        return words[0].lower() + ''.join(word.capitalize() for word in words[1:])
    elif case_style == 'pascal':
        return ''.join(word.capitalize() for word in words)
    elif case_style == 'lower':
        return ' '.join(words)
    elif case_style == 'title':
        return ' '.join(word.capitalize() for word in words)
    else:
        return '_'.join(words)  # Default to snake_case

# UX - User Experience
def sanitize_filename(filename: str) -> str:
    """
    Sanitize the proposed filename to remove invalid characters and ensure it's safe for all operating systems.
    Returns: a string of the sanitized filename
    """

    # Define invalid characters (\\ is the escape char for \, allowing us to include '\' in the string)
    invalid_chars = '<>:"/\\|?*'
    
    # Replace invalid characters with underscores
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    
    # Remove leading/trailing spaces and dots
    filename = filename.strip('. ')
    
    # Ensure the filename isn't empty
    if not filename:
        filename = 'unnamed'
    
    return filename


# Run main
if __name__ == "__main__":
    main()