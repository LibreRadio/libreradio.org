import os


exclude_list = [
    "assets/error_docs/403.html",
    "assets/error_docs/404.html",
    "documentation/api/response.html"
]

directory_path = os.path.abspath(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), "../public/"))
root_lengt = len(directory_path)

files = []
for directory_name, subdirectory_list, file_list in os.walk(directory_path):
    for file_name in file_list:
        files.append(os.path.join(directory_name, file_name))

pages = []
url_root = "https://libreradio.org/"
for file in files:
    file = file.replace("\\", "/")
    if file.endswith((".html", ".php", "pdf")):
        if file.endswith("index.html"):
            pages.append(file[root_lengt:-10])
        else:
            pages.append(file[root_lengt:])

file = open(os.path.join(directory_path, "sitemap.txt"), "w")
for page in pages:
    if page not in exclude_list:
        file.write(url_root + page + "\n")
file.close()
