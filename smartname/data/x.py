
import argparse 
import requests
from pypdf import PdfReader

def main():
    parser = argparse.ArgumentParser(description="Rename a File with Ollama.")
    parser.add_argument("file", help="Path to file") # help is the description of the argument
    parser.add_argument("--model", default="moondream", help="Ollama model")
    parser.add_argument("--execute", action="store_true", help="Actually rename the file") # action is the type of the argument store_true means it will be True if the argument is present
    args = parser.parse_args() # parse_args() parses the arguments and returns them as an object

    # Read first page
    text = PdfReader(args.file).pages[0].extract_text()[:2000]

    # Ask Ollama
    prompt = f"Generate ONE descriptive filename (3-5 words, snake_case, no extension) for:\n\n{text}"
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": args.model, "prompt": prompt, "stream": False},
        timeout=15
    )
    suggested = response.json().get("response", "rename_me").strip()

    # Clean it up
    safe = "".join(c if c.isalnum() or c == "_" else "_" for c in suggested.lower()).strip("_") or "rename_me"
    new_name = safe + ".pdf"

    # Dry run or execute
    if args.execute:
        import pathlib # pathlib is a module that provides a way to work with files and directories
        p = pathlib.Path(args.file) # Path is a class that represents a file or directory path
        p.rename(p.with_name(new_name))
        print(f"Renamed to {new_name}")
    else:
        print(f"DRY RUN: would rename to {new_name}")
        print("Add --execute to apply")


main()
