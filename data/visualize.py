import glob
import json
import random
from PIL import Image
import matplotlib.pyplot as plt

icon_path = "../icon-data-2/*.png"
files = glob.glob(icon_path, recursive=True)
random.shuffle(files)

# take 16 random icons
plt.figure(figsize=(32, 32))
for i, fn in enumerate(files[:16]):
    im = Image.open(fn).resize((128, 128))
    with open(fn.replace("png", "json"), "r") as f:
        tags = json.load(f)
    plt.subplot(4, 4, i + 1)
    plt.imshow(im)
    tags = ", ".join(tags)
    # split the tags into multiple lines by num of chars
    tags = '\n'.join([tags[i:i+50] for i in range(0, len(tags), 50)])
    plt.title(tags, fontsize=8)
    plt.axis("off")
# save the figure
plt.savefig("samples/icons.png", dpi=300, bbox_inches="tight")
