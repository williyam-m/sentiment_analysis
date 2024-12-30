def get_arguments():
    args_dict = {
        "maxlen_train": 30,
        "maxlen_val": 50,
        "batch_size": 32,
        "lr": 2e-5,
        "num_eps": 2,
        "num_threads": 1,
        "output_dir": "my_model",
        "model_name_or_path": None,
    }

    return args_dict
