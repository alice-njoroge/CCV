import random

from decouple import config
from fabric.api import cd, env, run, local, sudo
from fabric.contrib.files import exists, append

REPO_URL = 'git@github.com:alice-njoroge/CCV.git'


def deploy():
    site_folder = f'/home/nanoafrika/CCV'
    run(f'mkdir  -p {site_folder}')
    with cd(site_folder):
        _get_latest_source()
        _update_virtualenv()
        _create_or_update_dotenv_live()
        _update_static_files()
        _update_database()
        _create_main_server_folders()
        _create_main_webserver_files()
        _restart_live_server()


def _get_latest_source():
    if exists('.git'):
        run('git fetch')
    else:
        run(f'git init')
        run(f'git remote add origin {REPO_URL}')
        run('git fetch')
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run(f'git reset --hard {current_commit}')


def _update_virtualenv():
    if not exists('venv/bin/pip'):
        run(f'python3.6 -m venv venv')
    run('./venv/bin/pip install --upgrade pip')
    run('./venv/bin/pip install -r requirements.txt')


def _create_or_update_dotenv_live():
    append('.env', f'DEBUG =false')
    append('.env',
           f'ALLOWED_HOSTS=site.ccvkenya.org')
    append('.env', f'DATABASE_URL={config("LIVE_DATABASE_URL")}')
    append('.env', f'EMAIL_BACKEND = {config("EMAIL_BACKEND")}')
    append('.env', f'EMAIL_HOST = {config("EMAIL_HOST")}')
    append('.env', f'EMAIL_PORT = {config("EMAIL_PORT")}')
    append('.env', f'EMAIL_HOST_USER = {config("EMAIL_HOST_USER")}')
    append('.env', f'EMAIL_HOST_PASSWORD = {config("EMAIL_HOST_PASSWORD")}')
    current_contents = run('cat .env')
    if 'SECRET_KEY' not in current_contents:
        new_secret = ''.join(random.SystemRandom().choices(
            'abcdefghijklmnopqrstuvwxyz0123456789', k=50))
        append('.env', f'SECRET_KEY={new_secret}')


def _update_static_files():
    run('./venv/bin/python manage.py collectstatic --noinput')


def _update_database():
    run('./venv/bin/python manage.py migrate --noinput')


def _create_main_server_folders():
    run(f'mkdir  -p /home/nanoafrika/run/')
    run(f'mkdir  -p /home/nanoafrika/logs')


def _create_main_webserver_files():
    if not exists('/home/nanoafrika/ccv_supervisior'):
        run('cp deploy_tools/ccv_supervisior /home/nanoafrika/')
        run('chmod u+x /home/nanoafrika/ccv_supervisior')
        run('touch /home/nanoafrika/logs/ccv.log')
        sudo('cp deploy_tools/ccv.conf /etc/supervisor/conf.d/')
        sudo('sudo supervisorctl reread')
        sudo('sudo supervisorctl update')
        sudo('sudo supervisorctl status ccv')
        sudo('cp deploy_tools/nginx.template.conf /etc/nginx/sites-available/ccv')
        sudo('ln -s /etc/nginx/sites-available/ccv /etc/nginx/sites-enabled/ccv')
        sudo('service nginx restart')


def _restart_live_server():
    sudo('supervisorctl restart ccv')
