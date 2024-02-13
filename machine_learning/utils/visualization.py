import numpy as np
import seaborn as sns
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt


def result_visualization(config: dict, y_true: np.ndarray, y_pred: np.ndarray):
    if config["result_visualization_method"] is None:
        return
    for vis_method in config["result_visualization_method"]:
        if vis_method == "confusion_matrix":
            if (
                config["label_type"] == "binary"
                or config["label_type"] == "multi_class"
            ):
                cm = confusion_matrix(y_true, y_pred)
                # sns.heatmap(cm / np.sum(cm), annot=True, fmt=".2%", cmap="Blues")
                sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
                plt.show()
            else:
                raise Exception("label_type: " + config["label_type"] + " is not valid")
        elif vis_method == "roc_curve":
            if config["label_type"] == "binary":
                raise NotImplementedError
            elif config["label_type"] == "multi_class":
                raise Exception("roc_curve is not valid for multi_class")
            else:
                raise Exception("label_type: " + config["label_type"] + " is not valid")
        else:
            raise Exception(
                "result_visualization_method: " + vis_method + " is not valid"
            )
