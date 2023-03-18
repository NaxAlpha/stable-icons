# buuild and push to huggingface datasets
import json
import random
from pathlib import Path

import pandas as pd
from PIL import Image
from datasets import load_dataset

base_path = Path("../icon-data-2")
files = list(base_path.glob("*.png"))
# remove files with non-one aspect ratio
img_files = []
tags_info = []
for fn in files:
    im = Image.open(fn)
    w, h = im.size
    if w == h:
        img_files.append(str(fn))
        with open(fn.with_suffix(".json"), "r") as f:
            tags = json.load(f)
        random.shuffle(tags)
        tags_info.append("bw-icon:" + ", ".join(tags))
    im.close()

df = pd.DataFrame({"image": img_files, "tags": tags_info})
df.to_csv("icon_data.csv", index=False)

# build and push to huggingface datasets
dataset = load_dataset("csv", data_files="icon_data.csv")
# also load the images
dataset = dataset.map(
    lambda x: {"image": Image.open(x["image"]).resize((128, 128))},
    remove_columns=["image"],
)
dataset.push_to_hub("naxalpha/stable-icons-128")
