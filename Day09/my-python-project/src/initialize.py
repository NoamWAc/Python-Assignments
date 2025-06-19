import os
import rng_1_to_20

def initialize_game():
    
    # Try to import the config module and reset it. If it doesn't exist, create a default one
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
    
    game_num = rng_1_to_20.generate_new_num()
    
    return game_num
