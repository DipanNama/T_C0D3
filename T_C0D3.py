"""Portable static website scaffold. Dry-run unless --apply is supplied."""
import argparse
import json
import re
from pathlib import Path
RESERVED = {"con", "prn", "aux", "nul"} | {f"{x}{n}" for x in ("com", "lpt") for n in range(1, 10)}

def validate_name(name):
    if not isinstance(name, str) or not re.fullmatch(r"[a-zA-Z][a-zA-Z0-9_-]{0,39}", name) or name.lower() in RESERVED:
        raise ValueError("Use 1-40 ASCII letters, digits, hyphens or underscores, starting with a letter. Reserved device names are not allowed.")
    return name

def scaffold(name):
    validate_name(name)
    return {
        "index.html": f'<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1">\n<title>{name}</title>\n<link rel="stylesheet" href="css/style.css">\n</head>\n<body>\n<main><h1>{name}</h1><p>Your next website starts here.</p><button id="hello" type="button">Say hello</button><p id="message" role="status"></p></main>\n<script src="js/main.js"></script>\n</body>\n</html>\n',
        "css/style.css": '*{box-sizing:border-box}body{margin:0;font:16px/1.6 system-ui;background:#111113;color:#f4f4f5}main{max-width:680px;margin:12vh auto;padding:24px}button{border:1px solid #3f3f46;border-radius:999px;padding:12px 20px;background:#f4f4f5;color:#18181b;cursor:pointer}button:focus-visible{outline:2px solid #a1a1aa;outline-offset:4px}\n',
        "js/main.js": 'document.getElementById("hello").addEventListener("click",()=>{document.getElementById("message").textContent="Hello, world!";});\n'
    }

def create_project(parent, name, apply=False):
    files = scaffold(name)
    parent = Path(parent).resolve(strict=True)
    if not parent.is_dir():
        raise ValueError("Parent must be an existing directory.")
    target = parent / name
    if target.exists() or target.is_symlink():
        raise FileExistsError("Project path already exists. Choose another name.")
    if apply:
        target.mkdir()  # exclusive: refuses an existing path
        (target / "css").mkdir()
        (target / "js").mkdir()
        for relative, contents in files.items():
            with (target / relative).open("x", encoding="utf-8", newline="") as file:
                file.write(contents)
    return {"directory": str(target), "files": list(files), "created": apply}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Static starter generator. Use a trusted parent folder; dry-run by default.")
    parser.add_argument("name")
    parser.add_argument("--parent", default=".")
    parser.add_argument("--apply", action="store_true", help="Create the project; refuses an existing path")
    args = parser.parse_args()
    try:
        print(json.dumps(create_project(args.parent, args.name, args.apply), indent=2))
    except (ValueError, OSError) as error:
        parser.error(str(error))
