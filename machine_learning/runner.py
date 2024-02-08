from utils.data_loader import load_data
from utils.imbalance_learn import get_imbalance_algorithm
from utils.models import get_machine_learning_model
from utils.visualization import result_visualization
from utils.analysis import get_feature_importance

from sklearn.metrics import precision_score, recall_score,f1_score, roc_auc_score
from configs.runner_config import runner_config

import numpy as np


config = runner_config


def run():
    train_data, test_data = load_data(
        config=config,
    )

    train_x = train_data[:, 1:]
    train_y = train_data[:, 0]

    print("train data shape: {}".format(train_x.shape))

    imba = get_imbalance_algorithm(config)

    if imba is not None:
        train_x, train_y = imba.fit_resample(train_x, train_y)

    print("train data shape (after imbalance): {}".format(train_x.shape))

    test_x = test_data[:, 1:]
    test_y = test_data[:, 0]

    print("test data shape: {}".format(test_x.shape))

    # train model
    "train model..."
    clf = get_machine_learning_model(config)
    clf.fit(train_x, train_y)

    # test model
    print("{} test result as below:".format(config["model_option"]))
    y_true = test_y
    y_pred = clf.predict(test_x)
    print("accuracy: {}".format(clf.score(test_x, test_y)))

    if config["result_metric"] is not None:
        for metric in config["result_metric"]:
            if metric == "accuracy":
                print("accuracy: {}".format(clf.score(test_x, test_y)))
            elif metric == "f1_score":
                print("f1_score: {}".format(f1_score(y_true, y_pred, average="macro")))
            elif metric == "auc":
                if config["label_type"] == "binary":
                    print("auc: {}".format(roc_auc_score(y_true, y_pred)))
                elif config["label_type"] == "multi_class":
                    raise Exception("auc is not valid for multi_class")
            else:
                raise Exception("result_metric: " + metric + " is not valid")

    # precision and recall
    print("precision: {}".format(precision_score(test_y, y_pred, average = "weighted")))
    print("recall: {}".format(recall_score(test_y, y_pred, average = "weighted")))
    
    # visualize result
    result_visualization(
        config=config,
        y_true=y_true,
        y_pred=y_pred,
    )

    # analysis
    # importances = clf.feature_importances_
    # indices = np.argsort(importances)[::-1]

    # for f in range(train_x.shape[1]):
    #     print("{}: {:.3f}".format(indices[f],importances[indices[f]]))

    get_feature_importance(
        config=config,
        clf=clf,
        feature_names=[
            "hr",
            "cosine_feature",
            "linear_feature",
            "decay_feature",
            "acc_svm",
            # "x_zcm",
            # "y_zcm",
            # "z_zcm",
            "x_mean_abs",
            "y_mean_abs",
            "z_mean_abs",
            "x_var",
            "y_var",
            "z_var",
            "x_skew",
            "y_skew",
            "z_skew",
            "x_kurt",
            "y_kurt",
            "z_kurt",
        ],
    )


if __name__ == "__main__":
    run()
