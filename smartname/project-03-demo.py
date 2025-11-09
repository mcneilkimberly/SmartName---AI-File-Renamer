import argparse
import requests
from pypdf import PdfReader

def main():
    parser = argparse.ArgumentParser(description='Rename a file with Ollama.')
    parser.add_argument('file',help='Path to file')
    parser.add_argument('--model',default='gemma3:4b',help='Ollama model')
    parser.add_argument('--execute',action='store_true',help='Actually rename the file')

    args = parser.parse_args()

    text = PdfReader(args.file).pages[0].extract_text()[:2000]

    prompt = f"Generate ONE descriptive filename (3-5 words, snake_case, no extension) for\n\n{text}"
    response = requests.post(
        'http://localhost:11434/api/generate',
        json={'model': args.model, 'prompt': prompt, 'stream': False},
        timeout = 15
    )

    suggested = response.json().get('response', 'rename-me').strip()

    safe = "".join(c if c.isalnum() or c == "_" else "_" for c in suggested.lower()).strip("_") or "rename_me"

    new_name = safe + ".pdf"

    if args.execute:
        import pathlib
        p = pathlib.Path(args.file)
        p.rename(p.with_name(new_name))
        print(f'Renamed to {new_name}')
    else:
        print(f"DRY RUN: would rename to {new_name}")
        print('Add --execute to apply')

main()