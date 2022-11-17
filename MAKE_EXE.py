# pip install pyinstaller
# pyinstaller ./make_exe.py
# pyinstaller -F ./make_exe.py
# pyinstaller -w ./win_exe.py
# pyinstaller -w --add-data './gui_basic/*.png;gui_basic' ./win_exe.py
# pyinstaller -w --add-data './gui_basic/*.png;gui_basic' -F ./win_exe.py
# pyinstaller -w -F win_exe.py

# pyinstaller -w --add-data './pygame_basic/*.png;pygame_basic' -F ./F_pygame.py
# pyinstaller -w --add-data './pygame_basic/*.png;pygame_basic' -F ./F2_pygame.py
# pyinstaller -w --add-data './images/*.png;images' -F ./6_gameover.py


import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


print('hello world!!!')