import os

def get_dataset_path():
    return os.path.join(os.path.dirname(__file__), 'dataset', 'intention_dataset.json')

def get_model_path():
    return os.path.join(os.path.dirname(__file__), 'model_intention.joblib')
