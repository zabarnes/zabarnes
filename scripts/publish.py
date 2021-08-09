import sh
import sys
import nbformat
from datetime import datetime

if __name__ == '__main__':
  for nb_path in sys.argv[1:]:
    print("setting meta for", nb_path)
    nb = nbformat.read(nb_path, nbformat.NO_CONVERT)
    new_title =" ".join(map(str.capitalize, nb_path.replace(".ipynb","").split("/")[-1].split("-")[3:]))
    print("new title", new_title)
    nb.metadata['jekyll'] = {
      "layout": "single",
      "title": new_title,
      "mathjax": "true",
      "toc": "true",
    }
    nbformat.write(nb, nb_path, nbformat.NO_CONVERT)

    print("publishing", nb_path)
    sh.jupyter.jekyllnb("--site-dir", "docs", "--page-dir", "_posts", "--image-dir", "assets/images", nb_path)
