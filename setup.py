import cx_Freeze

executables = [cx_Freeze.Executable('Car Crash!.py', shortcutName = 'Car Crash!!', shortcutDir = 'DesktopFolder', icon = 'crash.ico')]

cx_Freeze.setup(
    name='Car Crash!!',
    options={"build_exe": {"packages":["pygame", "random", "Tkinter", "PIL", "tkMessageBox", "pickle", "os", "uuid"], "include_files":["red.png", "yellow.png", "logo.png", "MACFILE.dat", "help.txt", "car.mp3", "crash.ico"]}},

    description="Car crash Game",
    executables = executables
    )
