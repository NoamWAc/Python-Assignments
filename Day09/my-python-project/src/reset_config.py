import os

def reset_config():
    """
    This function resets the configuration settings for the number guessing game.
    It sets the debug mode and move mode to their default values (False).
    """
    
    try:
        import config
        config.DEBUG_MODE_IS_ON=False
        config.MOVE_MODE_IS_ON=False
    except:
        config_file_path = "config.py"
        if not os.path.exists(config_file_path):
                with open(config_file_path, "w") as f:
                    f.write("DEBUG_MODE_IS_ON = false\n")
                    f.write("MOVE_MODE_IS_ON = False\n")
                print("Created default config.py")
        else:
            raise ImportError("config.py exists but import failed. Please check the file for errors.")