import kagglehub
import shutil
import os
from config.config import Config

# Awesome dataset (Vikorist standard cache cache)
path = kagglehub.dataset_download(Config.get_kagle_repo())
print("Downloaded to (cache):", path)

# Way, where do you want to move
destination_dir = "data/weather/initial"

# Create a directory if you don't mind
os.makedirs(destination_dir, exist_ok=True)

# Copying all files from the cache to a folder
for file_name in os.listdir(path):
    src = os.path.join(path, file_name)
    dst = os.path.join(destination_dir, file_name)
    shutil.copy2(src, dst)

print("Переміщено до:", destination_dir)
