# buuild and push to huggingface datasets
import json
import random
from pathlib import Path

import pandas as pd
from PIL import Image as PILImage
from tqdm import tqdm
from datasets import Dataset, Image, Features, Value

base_path = Path("../icon-data-2")
files = list(base_path.glob("*.png"))
# remove files with non-one aspect ratio
imgs_data = []
tags_info = []
feature = Image()
for fn in tqdm(files):
    im = PILImage.open(fn)
    w, h = im.size
    if w == h:
        im = im.resize((128, 128))
        im = feature.encode_example(im)
        imgs_data.append(im)
        with open(fn.with_suffix(".json"), "r") as f:
            tags = json.load(f)
        random.shuffle(tags)
        tags = ["bw-icon"] + tags
        tags_info.append(", ".join(tags))

dataset = Dataset.from_pandas(
    pd.DataFrame(
        {
            "image": imgs_data,
            "tags": tags_info,
        }
    ),
    features=Features(
        {
            "image": feature,
            "tags": Value("string"),
        }
    ),
)
# next(iter(dataset))
dataset.push_to_hub("naxalpha/stable-icons-128")
