import os

def load_config_generate(dataset_nm):
    config = {
        'model_path': os.path.join(
            'log',
            dataset_nm,
            '20231113_162940/models/epoch2599_model_stete_dict.pt'
        )
    }
    
    return config
