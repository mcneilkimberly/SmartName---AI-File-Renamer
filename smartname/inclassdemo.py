import argparse
import requests
from pypdf import PdfReader

def main():
  parser = argparse.ArgumentParser(description="Rename files based on content using Ollama API.")
  parser.add_argument("file", nargs="+", help="List of files to rename.")
  parser.add_argument("--model", default="llama3.2-vision", help="Ollama model to use.")
  parser.add_argument("--execute", action="store_true", help="Actually rename the files.")
  args = parser.parse_args()

  text = PdfReader(args.file).pages[0].extract_text()[:2000]


  prompt = f"Generate ONE descriptive filename (3 to 5 words, snake_case) for a file based on the following content. Respond with ONLY the filename, no extension or additional text.\n\nContent:\n{text}"
  response = requests.post(
      "http://localhost:11434/api/generate",
      json={
          "model": args.model,
          "prompt": prompt,
          "stream": False
      },
      timeout=15)
  
  suggested = response.json().get("response", "rename-me").strip()

  safe = "".join(c if c.isalnum() or c in (' ', '_') else '_' for c in suggested.lower()).strip("_") or "rename_me"

  new_name = safe + "." + args.file.split(".")[-1]

  if args.execute:
    import pathlib, os
    p = pathlib.Path(args.file)
    p.rename(p.with_name(new_name))
    print(f"Renamed '{args.file}' to '{new_name}'")
  else:
    print(f"Suggested filename for '{args.file}': {new_name} (not renamed, use --execute to rename)")

main()