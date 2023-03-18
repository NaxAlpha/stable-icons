import os
import json
import yaml
from pathlib import Path

from tqdm import tqdm


def ion_icon_processor(output_path, output_start_idx=0):
    base_path = Path("../ionicons/src/")
    data_file = base_path / "data.json"
    icon_path = base_path / "svg"
    with open(data_file, "r") as f:
        data = json.load(f)
    for icon in tqdm(data["icons"], desc=f"Processing {base_path}"):
        svg_file = icon_path / (icon["name"] + ".svg")
        target_fn = f"{output_path}/{output_start_idx:05d}.png"
        os.system(f"rsvg-convert {svg_file} -o {target_fn}")
        with open(target_fn.replace("png", "json"), "w") as f:
            json.dump(icon["tags"], f)
        output_start_idx += 1
    return output_start_idx


def font_awesome_icon_processor(output_path, output_start_idx=0):
    base_path = Path("../Font-Awesome/")
    data_file = base_path / "metadata/icons.yml"
    icon_path = base_path / "svgs"
    with open(data_file, "r") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    for iid, icon in tqdm(data.items(), desc=f"Processing {base_path}"):
        for style in icon['styles']:
            svg_file = icon_path / style / (iid + ".svg")
            target_fn = f"{output_path}/{output_start_idx:05d}.png"
            os.system(f"rsvg-convert {svg_file} -o {target_fn}")
            tags = [icon['label'], style] + icon['search']['terms']
            with open(target_fn.replace("png", "json"), "w") as f:
                json.dump(tags, f)
            output_start_idx += 1
    return output_start_idx


def tabler_icon_processor(output_path, output_start_idx=0):
    base_path = Path("../tabler-icons/")
    data_file = base_path / "tags.json"
    icon_path = base_path / "icons"
    with open(data_file, "r") as f:
        data = json.load(f)
    for icon in tqdm(data.values(), desc=f"Processing {base_path}"):
        svg_file = icon_path / (icon["name"] + ".svg")
        target_fn = f"{output_path}/{output_start_idx:05d}.png"
        os.system(f"rsvg-convert {svg_file} -o {target_fn} -w 512 -h 512")
        tags = [icon["name"], icon['category']] + icon["tags"]
        with open(target_fn.replace("png", "json"), "w") as f:
            json.dump(tags, f)
        output_start_idx += 1
    return output_start_idx



if __name__ == "__main__":
    idx = 0
    out = "../icon-data-2"
    idx = ion_icon_processor(out, idx)
    idx = font_awesome_icon_processor(out, idx)
    idx = tabler_icon_processor(out, idx)
