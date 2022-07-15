# deploy_tools/fabfile.py
from fabric.contrib.files import append, exists, sed  # noqa:F401
from fabric.api import env, local, run  # noqa:F401
import random  # noqa:F401

REPO_URL = "https://github.com/kevinbowen777/superlists.git"


def deploy():
    site_folder = f"/home/{env.user}/sites/{env.host}"
    source_folder = site_folder + "/source"
    _create_directory_structure_if_necessary(site_folder)  # noqa:F821
    _get_latest_source(source_folder)  # noqa:F821
    _update_settings(source_folder, env.host)  # noqa:F821
    _update_virtualenv(source_folder)  # noqa:F821
    _update_static_files(source_folder)  # noqa:F821
    _update_database(source_folder)  # noqa:F821
