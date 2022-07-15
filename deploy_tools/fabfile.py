# deploy_tools/fabfile.py
from fabric.contrib.files import append, exists, sed  # noqa:F401
from fabric.api import env, local, run  # noqa:F401
import random  # noqa:F401

REPO_URL = "https://github.com/kevinbowen777/superlists.git"


def deploy():
    site_folder = f"/home/{env.user}/sites/{env.host}"
    source_folder = site_folder + "/source"
    _create_directory_structure_if_necessary(site_folder)
    _get_latest_source(source_folder)
    _update_settings(source_folder, env.host)  # noqa:F821
    _update_virtualenv(source_folder)  # noqa:F821
    _update_static_files(source_folder)  # noqa:F821
    _update_database(source_folder)  # noqa:F821


def _create_directory_structure_if_necessary(site_folder):
    for subfolder in ("database", "static", "virtualenv", "source"):
        run(f"mkdir -p {site_folder}/{subfolder}")


def _get_latest_source(source_folder):
    if exists(source_folder + "/.git"):
        run(f"cd {source_folder} && git fetch")
    else:
        run(f"git clone {REPO_URL} {source_folder}")
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run(f"cd {source_folder} && git reset --hard {current_commit}")
