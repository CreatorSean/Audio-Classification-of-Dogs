from glob import glob
import numpy as np


def load_data(config: dict):
    return shuffle_n_split_data(config=config, data_dict=load_featured_data())


def load_featured_data():
    glob_path = "processed_data/*/feature.csv"

    data_dict = {}
    for data_path in glob(glob_path):
        new_data = np.loadtxt(data_path, delimiter=",")

        id = data_path.split("\\")[1].split("_")[0]
        data_dict[id] = new_data

    return data_dict


def shuffle_n_split_data(
    config: dict,
    data_dict: dict,
    fold_now: int = 0,
):
    train_data = None
    test_data = None

    if config["validation_method"] == "LOSO":
        for id in data_dict.keys():
            if id == config["validation_subject"]:
                test_data = data_dict[id]
            else:
                if train_data is None:
                    train_data = data_dict[id]
                else:
                    train_data = np.concatenate([train_data, data_dict[id]])

        return np.array(train_data), np.array(test_data)
    
    elif config["validation_method"] == "k_fold":
        data_bunch = []

        for id in data_dict.keys():
            data_bunch.append(data_dict[id])

        
        np.random.shuffle(data_bunch)

        # split data
        split_start_idx = int(len(data_bunch) * fold_now / config["validation_fold"])
        split_end_idx = int(
            len(data_bunch) * (fold_now + 1) / config["validation_fold"]
        )

        train_data = data_bunch[:split_start_idx] + data_bunch[split_end_idx:]
        test_data = data_bunch[split_start_idx:split_end_idx]

        return np.array(train_data), np.array(test_data)
    elif config["validation_method"] == "random_split":
        data_bunch = None

        for data in data_dict.keys():
            if data_bunch is None:
                data_bunch = data_dict[data]
            else:
                data_bunch = np.concatenate([data_bunch, data_dict[data]])

        print(data_bunch)
        np.random.shuffle(data_bunch)

        # split data
        split_idx = int(len(data_bunch) * config["validation_ratio"])

        train_data = data_bunch[split_idx:]
        test_data = data_bunch[:split_idx]

        return np.array(train_data), np.array(test_data)
    else:
        raise Exception(
            "validation_method: " + config["validation_method"] + " is not valid"
        )
