import os


directory = os.path.abspath(input())

if not os.path.isdir(directory):
    raise SystemExit(f"Directory not found: {directory}")

files_by_extension = {}

for current_directory, subdirectories, files in os.walk(directory):
    if current_directory != directory:
        subdirectories.clear()

    for file_name in files:
        extension = os.path.splitext(file_name)[1]

        if extension not in files_by_extension:
            files_by_extension[extension] = []

        files_by_extension[extension].append(file_name)

report_path = os.path.join(directory, "report.txt")

with open(report_path, "w", encoding="utf-8") as report:
    for extension, file_names in sorted(files_by_extension.items()):
        report.write(f"{extension}\n")

        for file_name in sorted(file_names):
            report.write(f"- - - {file_name}\n")
