Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3.8+
* virtualenv + pip
* Git

eg, on Ubuntu:
    `sudo apt-get install nginx git python36 python3.6-venv`

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, e.g., staging.my-domain.com
```
sed "s/SITENAME/<your_site_name>/g" \
source/deploy_tools/nginx.template.conf \
| sudo tee /etc/nginx/sites-available/<your_site_name>
```
- Activate with a symlink:
    - `sudo ln -s ../sites-available/<your_site_name> \
/etc/nginx/sites-enabled/<your_site_name>`

## Systemd service

* see gunicorn-systemd.template.service
* replace SITENAME with, e.g., staging.my-domain.com
```
sed "s/SITENAME/<your_site_name>/g" \
source/deploy_tools/gunicorn-systemd.template.service \
| sudo tee /etc/systemd/system/gunicorn-<your_site_name>.service
```

## Start both services
```
sudo systemctl reload nginx
sudo systemctl enable <your_site_name>
sudo systemctl start gunicorn-<your_site_name>
```

## Folder structure:
Assume we have a user account at /home/username

/home/username
└── sites
    └── SITENAME
        ├── database
        ├── source
        ├── static
        └── virtualenv
