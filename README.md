# Descargar repositorio:
git clone git@github.com:gon64/tasks.git
cd tasks

# instalar virtualenv
pip install virtualenv

# Crear entorno virtual
python -m venv venv

# cambiar a virtualenv
source venv/bin/activate

# Instalar composer:

php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
php -r "if (hash_file('sha384', 'composer-setup.php') === '55ce33d7678c5a611085589f1f3ddf8b3c52d662cd01d4ba75c0ee0459970c2200a51f492d557530c71c15d8dba01eae') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
php composer-setup.php
php -r "unlink('composer-setup.php');"

# Instalar bootstrap via composer
composer require twbs/bootstrap
