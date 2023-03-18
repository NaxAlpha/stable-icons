import os
import glob
from tqdm import tqdm

svg_dirs = [
    "../fontawesome-free-6.3.0-desktop/svgs/*/*.svg",
    "../ionicons.designerpack/*.svg",
    "../tabler-icons/icons/*.svg",
]

idx = 0
for i, svg_dir in enumerate(svg_dirs):
    svg_dir = os.path.expanduser(svg_dir)
    svg_files = glob.glob(svg_dir, recursive=True)
    svg_files.sort()
    size_str = "-w 512 -h 512" if i == 2 else ""  # tabler icons very small
    # all_files += svg_files
    for svg_file in tqdm(svg_files, desc=f"Processing {svg_dir}"):
        target_fn = f"../icon-data/{idx:05d}.png"
        os.system(f"rsvg-convert {svg_file} -o {target_fn} {size_str}")
        idx += 1
