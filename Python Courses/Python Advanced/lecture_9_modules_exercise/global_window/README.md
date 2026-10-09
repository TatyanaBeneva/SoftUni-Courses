# GUI Product Shop

Run main.py with Python 3 and Tkinter. Paths are resolved from the project folder,
so the working directory does not matter:

```powershell
& "D:\SoftUni Courses\.venv\Scripts\python.exe" "D:\SoftUni Courses\SoftUni-Courses\Python Courses\Python Advanced\lecture_9_modules_exercise\global_window\main.py"
```

In PyCharm, run main.py using the workspace .venv interpreter.
You can also run with -m global_window.main from lecture_9_modules_exercise.

Register an account, log in, and buy a sample product. Usernames accept 3-30
letters, digits, or underscores; passwords require at least 8 characters.
Passwords are salted and hashed. The active login lasts only for this process.
The old empty user_credentials_db.txt is no longer used.

Users and products are stored as one JSON object per line in db. Sample products
are included. Images are optional: place files named by img_path in an images
folder next to products.py and install Pillow with your Python interpreter's
`-m pip install Pillow` command. Missing images or Pillow show a placeholder.

This is a single-process learning application. Run one instance at a time.
Individual file replacements are atomic and purchase writes roll back stock on
an ordinary user-file write failure. A database transaction would be needed to
guarantee consistency across a process crash or simultaneous app instances.
