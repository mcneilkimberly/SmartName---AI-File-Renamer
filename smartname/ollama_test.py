import requests
import json

def test_ollama_api():
    # # Ollama API endpoint (default running on localhost:11434)
    # url = "http://localhost:11434/api/generate"
    
    # # Request payload
    # payload = {
    #     "model": "gemma3:1b",  # Replace with your installed model name
    #     "prompt": "Tell me a fun fact about Python programming.",
    #     "stream": False  # Set to False to get complete response at once
    # }
    
  
    # try:
    #     # Make the API call
    #     response = requests.post(url, json=payload)
        
    #     # Check if the request was successful
    #     if response.status_code == 200:
    #         result = response.json()
    #         print("API Call Successful!")
    #         print("\nResponse:")
    #         print(result['response'])
    #     else:
    #         print(f"Error: API call failed with status code {response.status_code}")
    #         print(response.text)
            
    # except requests.exceptions.RequestException as e:
    #     print(f"Error making API call: {e}")


  # test_multipart_image.py
  import requests, sys

  url = "http://localhost:11434/api/generate"
  model = "gemma3:1b"
  image_path = "data\\Screenshot 20240923 123456 copy.JPG"
  #sys.argv[1] if len(sys.argv) > 1 else "data/test.png"

  # Some servers expect a 'file' field; others may accept 'image' or 'images[]'.
  files = {
      "file": open(image_path, "rb")
  }
  data = {
      "model": model,
      "prompt": "Suggest a filename for this image (ONLY the filename, no extension).",
      "stream": "false"
  }

  print(image_path)

  resp = requests.post(url, data=data, files=files)
  print("STATUS:", resp.status_code)
  print("TEXT:", resp.text)


def other():
  # test_json_image.py
  import requests, base64, sys

  url = "http://localhost:11434/api/generate"
  model = "gemma3:1b"
  image_path = "data\\Screenshot 20240923 123456 copy.JPG"

  with open(image_path, "rb") as f:
      b64 = base64.b64encode(f.read()).decode("utf-8")

  payload = {
      "model": model,
      "prompt": "Suggest a filename for this image (ONLY the filename, no extension).",
      "images": [b64],
      "stream": False
  }

  resp = requests.post(url, json=payload)
  print("STATUS:", resp.status_code)
  print("TEXT:", resp.text)



def youtubeVideo():
  import ollama
  repsonse = ollama.chat(
    model="llama3.2-vision",
    messages=[
      {
        "role": "user",
        "content": "Analyze this file's content and suggest a concise, 5-8 word, descriptive filename that captures its main content. Respond with *ONLY* the filename suggestion with *NO* additional text or explanation. Do *NOT* include a file extension.",
        "images": "\data\\Screenshot 20240923 123456 copy.JPG"
      }
    ]
  )

  print(repsonse['response']['message'])




if __name__ == "__main__":
    #test_ollama_api()
    #other()
    youtubeVideo()