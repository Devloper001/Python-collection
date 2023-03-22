from time import ctime
from pathlib import Path
path = Path("9-Python Standard Library/__init__.py")
path.exists()
path.is_file()
path.is_dir()
# returns file name
print(path.name)
# returns file name with extension
print(path.stem)
# returns suffix
print(path.suffix)
# returns parent folder
print(path.parent)
# create new path only change extension of file
path = path.with_name("file.txt")
print(path)
# prints absolute value of file
print(path.absolute())


# // Working with Directories //
paths = [p for p in path.iterdir()]
print(paths)
py_files = [p for p in path.rglob("*.py")]
# all the py files and its children
print(py_files)


# // Working with files //
path(ctime(path.stat().st_ctime))
