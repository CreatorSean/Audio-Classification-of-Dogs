from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier

import numpy as np
import matplotlib.pyplot as plt


def get_feature_importance(config: dict, clf, feature_names: list):
    if config["analysis_method"] is None:
        return
    elif config["analysis_method"] == "importance":
        if config["model_option"] == "GB":
            feature_importance = clf.feature_importances_
            feature_importance = 100.0 * (feature_importance / feature_importance.max())
            print(feature_importance)
            sorted_idx = np.argsort(feature_importance)
            pos = np.arange(sorted_idx.shape[0]) + 0.5
            fig, ax = plt.subplots(figsize=(8, 6))
            ax.barh(
                pos, feature_importance[sorted_idx], align="center", color="#00bfff"
            )
            ax.set_yticks(pos)
            ax.set_yticklabels(np.array(feature_names)[sorted_idx], fontsize=12)
            ax.invert_yaxis()
            ax.set_xlabel("Relative Importance", fontsize=14)
            ax.set_title("Variable Importance", fontsize=16)
            plt.show()
        else:
            raise Exception("model_option: " + config["model_option"] + " is not valid")
    else:
        raise Exception(
            "analysis_method: " + config["analysis_method"] + " is not valid"
        )
