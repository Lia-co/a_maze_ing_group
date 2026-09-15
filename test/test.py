def open_file() -> None:
	with open("test.txt") as f:
		print(f.read())