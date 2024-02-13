runner_config = {
    # data options
    "label_type": "multi_class",  # it could be... "binary", "multi_class"
    # validation options
    "validation_method": "LOSO",  # it could be... "k_fold", "LOSO", "random_split"
    "validation_subject": "1066528",  # if validation_method is "LOSO", this value is subject id
    "validation_fold": 5,  # if validation_method is "k_fold", this value is k, split ratio will be 1/k
    "validation_ratio": 0.2,  # if validation_method is "random_split", this value is ratio
    # model options
    "model_option": "GB",  # it could be... "SVM", "RF", "GB", "KNN", "DNN"
    "model_save_path": "model",  # model save path
    "result_save_path": "result",  # result save path
    "result_metric": [
        "accuracy",
        "f1_score",
    ],  # it could be... "accuracy", "f1_score", "auc" (if you want to use multiple metrics, use list)
    # and it could be... None (if you don't want to use any metric)
    "result_visualization_method": [
        "confusion_matrix",
    ],
    # it could be... ["confusion_matrix", "roc_curve"...] (if you want to use multiple methods, use list)
    # and it could be... None (if you don't want to use any visualization method)
    # imbalance options
    "imbalance_option": "SMOTE",  # it could be... "SMOTE", "ADASYN", "None"
    # anaylsis options
    "analysis_method": "importance",  # it could be... "importance", "None"
}
