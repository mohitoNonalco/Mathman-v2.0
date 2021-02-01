import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
	name="Jumpman",
	options={"build_exe": {"packages":["pygame", "random"],
									  "include_files":['images\\brick.png', 'images\\sky.png', 'images\\slime.png', 'images\\dirt.png',
									  'images\\player.png', 'images\\upr.png', 'images\\upr2.png', 'images\\s_tutor.png', 'images\\brick.png',
									  'images\\princess.png', 'images\\dialogue.png', "config.py", "colors.py", "map1.txt"]}},
	executables = executables)