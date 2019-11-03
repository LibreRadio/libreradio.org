import os


directory_path = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../public/"))
root_lengt = len(directory_path)

files = []
for directory_name, subdirectory_list, file_list in os.walk(directory_path):
    for file_name in file_list:
        files.append(os.path.join(directory_name, file_name))

exclude = [
	"/assets/error_docs/403.html",
	"/assets/error_docs/404.html",
	"/documentation/api/response.html"
]
exclude_list = []
for file in exclude:
	exclude_list.append(os.path.abspath(os.path.join(directory_path, file[1:])))

sitemap = ""
url_root = "https://libreradio.org/"
for file in files:
	if file.endswith((".html", ".php", "pdf")):
		if file in exclude_list:
			continue
		elif file.endswith("index.html"):
			sitemap += url_root + file[root_lengt:-10] + "\n"
		else:
			sitemap += url_root + file[root_lengt:] + "\n"

file = open(os.path.join(directory_path, "sitemap.txt"), "w")
file.write(sitemap.replace("\\", "/"))
file.close()
