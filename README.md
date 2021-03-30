# blender remote render

This project is for remote rendering blender projects on 
another machine. This project use `socket`, `PyQt5` and `bpy` 
(blender-py)

<br/>

In `constants.py` you must change path to blender launch file:
```python
BLENDER_EXE = os.path.normpath('your/path/to/blender.exe')
```
<br/>

Also you can change settings in `constants.py`:
```python
REMOVING_FILES = 1  # 1 - remove, 0 - leave
```

<br/>

