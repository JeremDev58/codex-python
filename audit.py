import os
import requests
from github import Github
from enum import Enum
import re
import json


LST_FILE = {
    "default.py": "./assets/theme/default.py",
    "default": "./controller/setting/default",
    "Tbutton.py": "./controller/imports/Tbutton.py",
    "theme_manager.py": "./controller/theme/theme_manager.py",
    "category.json": "./search/category.json",
    "custom_search.json": "./search/custom_search.json",
    "file.json": "./search/file.json",
    "subtitle.json": "./search/subtitle.json",
    "tags.json": "./search/tags.json",
    "title.json": "./search/title.json",
    "menu_top.py": "./views/models/menu_top.py",
    "menu_side.py": "./views/models/menu_side.py",
    "view_codex.py": "./views/view/view_codex.py",
    "view_new.py": "./views/view/view_new.py",
    "view_search.py": "./views/view/view_search.py"}

LST_DIR = {"uuid": "./uuid", "codex": os.path.expanduser("~") + "/Codex"}

LST_FILES_INTEGRITY = {
    "default.py": "./assets/theme/default.py",
    "default": "./controller/setting/default",
    "Tbutton.py": "./controller/imports/Tbutton.py",
    "theme_manager.py": "./controller/theme/theme_manager.py",
    "menu_top.py": "./views/models/menu_top.py",
    "menu_side.py": "./views/models/menu_side.py",
    "view_codex.py": "./views/view/view_codex.py",
    "view_new.py": "./views/view/view_new.py",
    "view_search.py": "./views/view/view_search.py"}

LST_FILES_REBUILD = {
    "category.json": "./search/category.json",
    "custom_search.json": "./search/custom_search.json",
    "file.json": "./search/file.json",
    "subtitle.json": "./search/subtitle.json",
    "tags.json": "./search/tags.json",
    "title.json": "./search/title.json"}

LST_PATH_INTEGRITY = {
    "all_path":
        [
            "./assets",
            "./assets/theme",
            "./assets/theme/icons",
            "./assets/theme/images",
            "./controller",
            "./controller/setting",
            "./controller/imports",
            "./controller/theme",
            "./search",
            "./uuid",
            "./views",
            "./views/models",
            "./views/view",
            "./uuid",
            os.path.expanduser("~") + "/Codex"
        ]}


"""
check_start() --> Vérifie au lancement du logiciel si tout est en état.
audit_all_integrity() --> Vérifie et répare tous les fichier du logiciel.
get_file_online() --> Téléchage les fichier du logiiciel sur un serveur distant.
get_file_online_github() --> Téléchage les fichier du logiiciel sur GitHub avec mon compte.
rebuild_search_file() --> Reconstruit le fichier "file.json" dans ./search.
rebuild_path_integrity() --> Reconstruit tous les dossier du logiciel.
list_files_cdx() --> Renvoie une list des path des fichiers .cdx située dans le dossier Codex.
"""


def check_start():
    for k, v in LST_FILE.items():
        print(v)
        if not os.path.exists(v):
            try:
                audit_all_integrity()
            except:
                print("Error: Problème dans f:check_start() avec la fonction audit_all_integrity().")


def audit_all_integrity():
    rebuild_path_integrity()
    for k, v in LST_FILES_INTEGRITY.items():
        print(v)
        path = v[2:]
        try:
            with open(v, "w") as f:
                f.write(get_file_online_github(path))
        except FileNotFoundError:
            try:
                with open(v, "x") as f:
                    f.write(get_file_online_github(path))
            except:
                print(f"Error: Problème f:audit_all_integrity() impossible d'écrire le fichier {k}.")
        except:
            print(f"Problème f:audit_all_integrity() avec le fichier:{k}.")
    for k, v in LST_FILES_REBUILD.items():
        print(v)
        try:
            with open(v, "w") as f:
                f.write("")
        except FileNotFoundError:
            try:
                with open(v, "x") as f:
                    f.write("")
            except:
                print(f"Error: Problème f:audit_all_integrity() impossible d'écrire le fichier {k}.")
        except:
            print(f"Problème f:audit_all_integrity() avec le fichier:{k}.")
    if not rebuild_search_file():
        try:
            with open(LST_FILE["file.json"], "r") as f:
                ls_files = json.loads(f.read())
        except:
            print(f"Problème f:audit_all_integrity() avec la fonction json.loads().")
        else:
            for path in ls_files["path"]:
                try:
                    with open(path, "r") as f:
                        file = json.loads(f.read())
                    with open(LST_FILES_REBUILD["title.json"], "r") as f:
                        title = json.loads(f.read())
                    title["title"].append(file["title"])
                    hex_title = file["title"].encode("utf-8").hex()
                    conf = file[hex_title]
                    for k, v in LST_FILES_REBUILD.items():
                        print(v)
                        s_replace = k.replace(".json", "")
                        if not s_replace == "file" and not s_replace == "title":
                            with open(v, "r") as f:
                                data = json.loads(f.read())
                            for x in conf[s_replace]:
                                data[s_replace].append(x)
                            with open(v, "w") as f:
                                f.write(json.dumps(data))
                except:
                    pass


def get_file_online(pathfile=""):
    res = requests.get(f"https://raw.githubusercontent.com/Jerem08/Codex/main/{pathfile}")
    if res.status_code == 200:
        return res.text
    else:
        raise Exception("Error: Impossible d'acceder au fichier distant.")


def get_file_online_github(pathfile=""):

    git = Github(login_or_token="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")
    repo = git.get_user().get_repo("Codex")
    file = repo.get_contents(pathfile)
    return file.decoded_content.decode("utf-8")


def rebuild_search_file():
    # --> True si il n'y a pas de fichier .cdx

    ls_files = list_files_cdx()
    if len(ls_files):
        dict_file = {"path": ls_files}
        try:
            with open(LST_FILES_REBUILD["file.json"], "w") as f:
                f.write(json.dumps(dict_file))
        except FileNotFoundError:
            with open(LST_FILES_REBUILD["file.json"], "x") as f:
                f.write(json.dumps(dict_file))
        except:
            print("Error: Problème inconnu f:rebuild_search_file().")
    else:
        return True
    return False


def rebuild_path_integrity():
    for repo in LST_PATH_INTEGRITY["all_path"]:
        if not os.path.isdir(repo):
            try:
                os.mkdir(repo)
            except:
                print(f"Error: Problème f:rebuild_path_integrity() avec le dossier {dir}.")


def list_files_cdx():
    ls_files = []
    regex = re.compile(".*cdx")
    num_path_base = len(LST_DIR["codex"].split("/"))
    for root, repo, files in os.walk(LST_DIR["codex"]):
        limit_recursion = len(list(root.split("/")))
        if not limit_recursion > (20 + num_path_base):
            for f in files:
                path_cdx = root.replace((LST_DIR["codex"] + "/"), "")
                ls_files.append(os.path.join(path_cdx, f))

    for f in ls_files:
        if not regex.match(f):
            ls_files.remove(f)

    return ls_files
