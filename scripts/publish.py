import sh
import os
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
    if nb.cells[0]["source"].replace(" ", "").startswith("<!--jekyll-->"):
      for metaline in nb.cells[0]["source"].replace("<!--jekyll-->","").split("\n"):
        if ":" in metaline:
          split = metaline.index(":")
          nb.metadata['jekyll'][metaline[:split].strip()] = metaline[split+1:].strip()
      nb.cells = nb.cells[1:]

    os.makedirs(".temp", exist_ok=True)
    temp_nbpath = ".temp/"+nb_path.split("/")[-1]

    nbformat.write(nb, temp_nbpath, nbformat.NO_CONVERT)

    print("publishing", nb_path)
    sh.jupyter.jekyllnb("--site-dir", "docs", "--page-dir", "_posts", "--image-dir", "assets/images", temp_nbpath)
