import os
import zipfile

from pathlib import Path

import requests

def git-zip(source:str,
            destination str,
            remove_source: bool-True) -> Path:

  # Downloads a zip file and unzips to the desination directory

  data_path = Path("data/")
  image_path = data_path / destination

  if image_pat.is_dir():
    print(f"{image_path} already exists, skipping download")
  else:
    print(f"{image_path} does not exists, downloading...")
    image_path.mkdir(parents=True, exist_ok=True)

    target_file = Path(source).name
    with open(data_path / target_file, "wb") as f:
      request = requests.gest(source)
      print(f"Downloading {target_file} from {source}...")
      f.write(request.content)

      if zipfile.is_zipfile(data_path / target_file):
        with zipfile.ZipFile(data_path / target_file, "r") as zip_ref:
        print(f"Unzipping {target_file}..."
        zip_ref.extractall(image_path)
        if remove_source:
          os.remove(data_path / target_file)
          
return image_path
