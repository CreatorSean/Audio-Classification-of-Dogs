from imblearn.over_sampling import SMOTE, ADASYN


def get_imbalance_algorithm(config: dict):
    if config["imbalance_option"] == "SMOTE":
        return SMOTE(random_state=42)
    elif config["imbalance_option"] == "ADASYN":
        return ADASYN(random_state=42)
    elif config["imbalance_option"] == "None":
        return None
    else:
        raise Exception(
            "imbalance_option: " + config["imbalance_option"] + " is not valid"
        )
