import glob
import random
from PIL import Image
from torchvision.utils import save_image
from torchvision.transforms.functional import to_tensor

icon_path = "../icon-data/*.png"
files = glob.glob(icon_path, recursive=True)
random.shuffle(files)

# take 16 random icons
grid = []
for fn in files[:16]:
    im = Image.open(fn).resize((128, 128))
    grid.append(to_tensor(im))
    # im.close()

# save as grid
save_image(grid, "grid.png", nrow=4)
