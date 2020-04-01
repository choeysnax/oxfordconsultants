from fabric.api import local


def prep():
    local('pip freeze > requirements-temp.txt')
    with open('requirements-temp.txt', 'r') as f:
        content = f.read()
        final_requirements = content.replace('pkg-resources==0.0.0', '')
        with open('requirements.txt', 'w+') as x:
            x.write(final_requirements)
    local('rm requirements-temp.txt')


def run(args):
    local(f'heroku run python manage.py {args} -a oxfordconsultants')


def prod_mgr():
    local('heroku run python manage.py migrate --app=oxfordconsultants')


def prod_tail():
    local('heroku logs --tail --app=oxfordconsultants')


def prod_shell():
    local('heroku run python manage.py shell_plus --app=oxfordconsultants')


def shell():
    local('python manage.py shell_plus')


def all():
    prep()
    dev()
    master()


def dev():
    local('git push')
    local('git checkout dev')
    local('git merge master')


def master():
    local('git checkout master')
    local('git merge dev')
    local('git push')
    local('git checkout dev')
