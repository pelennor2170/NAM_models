import json
import numpy as np
import os

path = os.getcwd() # get the current directory path

_, dirs, _ = next(os.walk(path)) # get the list of subdirectories only from the current directory

for dir in dirs:
    subfolder_path = os.path.join(path, dir)
    configFN = os.path.join(subfolder_path, "config.json")
    weightFN = os.path.join(subfolder_path, "weights.npy")
    outFN = os.path.join(path, subfolder_path + '.nam')
    print(outFN)

    with open(configFN, "r") as fr:
        config = json.load(fr)
        config["version"] = "0.5.0"
        config["weights"] = np.load(weightFN).tolist()
    with open(outFN, "w") as fw:
        json.dump(config, fw, indent=4)
