from pathlib import Path
import subprocess
import json
import sys
import yaml

git = f"https://fortierq:{sys.argv[1]}@github.com/fortierq/cours-src.git"
dir_repo = Path("/tmp/cours-src")
if not dir_repo.exists():
    subprocess.run(["git", "config", "--global", "user.email", "qpfortier@gmail.com"])
    subprocess.run(["git", "config", "--global", "user.name", "Quentin Fortier"])
    subprocess.run(["git", "clone", git, dir_repo])
else:
    subprocess.run(["git", "config", "pull.rebase", "false"], cwd=dir_repo)
    subprocess.run(["git", "pull"], cwd=dir_repo)
menu, td = 0, 0

def iframe_td(p):
    global td
    td += 1
    return f"""
<script>
    $(function() {{
        document.getElementById("main-content").style.maxWidth = "90%";
        button_{td} = button_cor(
            'https://raw.githubusercontent.com/fortierq/cours/main/{p}',
            '{td}',
            'button_{td}'
        );
    }});
</script>

```{{margin}}
<input type="button" id="button_{td}" onclick="button_{td}.switch()" />
```

<iframe id="{td}" height=1100 width=100% allowfullscreen></iframe>
"""

def iframe(p):
        return f'<iframe src=https://mozilla.github.io/pdf.js/web/viewer.html?file=https://raw.githubusercontent.com/fortierq/cours/main/{p}#zoom=page-fit&pagemode=none height=500 width=100% allowfullscreen></iframe>'

def get_dl(d):
    global menu
    if isinstance(d, list):
        for v in d: 
            get_dl(v)
    elif isinstance(d, dict):
        for k in d.copy():
            if k in ["tp", "cor", "slides_ipynb"]:
                p = Path("files") / "dl" / d[k]
                p.parent.mkdir(parents=True, exist_ok=True)
                subprocess.run(["cp", (dir_repo / d[k]).absolute(), p])
                cmd = f"jupyter nbconvert {p} --to ipynb --output {p.name} --allow-errors --TagRemovePreprocessor.enabled=True --TagRemovePreprocessor.remove_input_tags hide"
                if k != "cor": 
                    cmd += " --TagRemovePreprocessor.remove_cell_tags cor"
                subprocess.run(cmd, shell=True)
                if k == "slides_ipynb":
                    nb = json.load(p.open())
                    if len(nb["cells"]) > 0 and nb["cells"][0]["cell_type"] == "markdown":
                        nb["cells"][0]["source"][0] += f'\n{iframe(Path(d[k]).with_suffix(".pdf"))}'
                        json.dump(nb, p.open("w"))
                d["file"] = str(p.relative_to("files"))
                subprocess.run(["git", "add", p])
                subprocess.run(["git", "commit", "-m", f"Add {p.name}"])
                subprocess.run(["git", "push"])
            if k in ["menu", "slides", "td"]:
                if k == "menu":
                    name = f"{menu}"
                    menu += 1
                else:
                    name = Path(d["file"]).stem
                p = (Path(f"files/{k}/{name}")).with_suffix(".md")
                p.parent.mkdir(parents=True, exist_ok=True)
                s = f"# {d[k]}"
                if k == "slides":
                    s += f'\n{iframe(Path(d["file"]))}'
                if k == "td":
                    s += f'\n{iframe_td(Path(d["file"]))}'                    
                p.write_text(s)
                d["file"] = str(p.relative_to("files"))
            if k in ["tp", "cor", "menu", "slides", "slides_ipynb", "td"]:
                del d[k]
            else:
                get_dl(d[k])

d = yaml.safe_load(Path("_toc.yml").read_text())
get_dl(d)
yaml.dump(d, Path("files/_toc.yml").open("w"))
