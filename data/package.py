import glob
from PIL import Image
from tqdm import tqdm
from zipfile import ZipFile
from collections import Counter

base_path = "../icon-data/*.png"
files = glob.glob(base_path, recursive=True)
files.sort()

with open("dataset.zip", "wb") as f:
    with ZipFile(f, "w") as zip:
        sizes = []
        for i, file in enumerate(tqdm(files)):
            im = Image.open(file)
            sizes.append(im.size)
            if im.size == (512, 512):
                with zip.open(f"icons/{i:05d}.png", "w") as zf:
                    im = im.resize((256, 256), Image.LANCZOS).convert("RGBA")
                    new = Image.new("RGB", (256, 256), (255, 255, 255))
                    new.paste(im, (0, 0), im)
                    new.save(zf, format="PNG")
            im.close()

print(Counter(sizes).most_common(10))
