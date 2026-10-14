# T_C0D3 - Starter Studio v2

Preview and download a tiny HTML/CSS/JavaScript starter in the browser, or create it with the portable Python CLI. Keeps the original three-file intent: `index.html`, `css/style.css`, `js/main.js`. The original Termux script is retained under `legacy/` and is not deployed or executed.

## Browser

Name a project and build its isolated preview. Inspect each generated file, copy it, or download it individually. Downloads do not include folders: create the shown `css` and `js` folders and move the corresponding files into them. The preview hello button works. Message/name input is not saved; only theme is stored. No remote code execution or package installation.

## Python CLI

Python 3.9+, no packages:

```sh
python3 T_C0D3.py my-website --parent .
python3 T_C0D3.py my-website --parent . --apply
```

First command is dry-run. Second creates the project and refuses any existing project path, including a symlink. Parent must already exist. Names use 1-40 ASCII letters/digits/hyphen/underscore, start with a letter, and reject Windows device names.

This is not a hostile-filesystem-safe or transactional tool. Use a trusted parent folder without concurrent writers. A write error can leave a partial new folder; inspect it before removing/retrying. Existing files are never deliberately overwritten. Termux storage requires its usual permissions; physical Android execution has not been tested.

v2 changes the old interactive `/sdcard` CLI to explicit arguments, a chosen parent and opt-in creation. Historical V1.0.0/V1.0.1 tags remain untouched.

## Tests and static build

Node 22 and Python 3:

```sh
npm test
npm run build
python3 -m http.server 8000 --directory dist
```

8 Python + 8 JS tests cover names/path rejection, dry-run, creation, existing paths/symlinks, exact Python/JS template parity and main-only deployment. Pages serves only the browser preview. It does not run the Python CLI.

Project license retained; Lucide icons ISC (`LICENSE-icons`). UI references: https://devdojo.com/pines/docs/button and https://shoogle.dev/.
