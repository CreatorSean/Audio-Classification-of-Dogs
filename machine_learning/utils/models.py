from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier

from configs.model_configs.svm_config import svm_config
from configs.model_configs.rf_config import rf_config
from configs.model_configs.knn_config import knn_config
from configs.model_configs.dnn_config import dnn_config
from configs.model_configs.gb_config import gb_config


def get_machine_learning_model(config: dict):
    if config["model_option"] == "SVM":
        return SVC(
            kernel=svm_config["kernel"],
            gamma=svm_config["gamma"],
            degree=svm_config["degree"],
            C=svm_config["C"],
            verbose=True,
        )
    elif config["model_option"] == "RF":
        return RandomForestClassifier(
            n_estimators=rf_config["n_estimators"],
            min_samples_split=rf_config["min_samples_split"],
            min_samples_leaf=rf_config["min_samples_leaf"],
            max_features=rf_config["max_features"],
            max_depth=rf_config["max_depth"],
            n_jobs=rf_config["n_jobs"],
            verbose=1,
        )
    elif config["model_option"] == "GB":
        return GradientBoostingClassifier(
            n_estimators=gb_config["n_estimators"],
            random_state=42,
        )
    elif config["model_option"] == "KNN":
        return KNeighborsClassifier(
            weights=knn_config["weights"],
            n_neighbors=knn_config["n_neighbors"],
            metric=knn_config["metric"],
            n_jobs=-1,
        )
    elif config["model_option"] == "DNN":
        return MLPClassifier(
            hidden_layer_sizes=dnn_config["hidden_layer_sizes"],
            activation=dnn_config["activation"],
            alpha=dnn_config["alpha"],
            solver=dnn_config["solver"],
            learning_rate=dnn_config["learning_rate"],
            random_state=42,
            verbose=True,
        )
    else:
        raise Exception("model_option: " + config["model_option"] + " is not valid")
