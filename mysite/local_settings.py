# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q=8nr3y=-6di(&)y0)n%!abb)l#e&fm%-w=o+zdutkzjn+u!w@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DB_NAME = 'biblioteca'
DB_USER = 'bibliotecario'
DB_PASS = 'bib'
DB_HOST = 'localhost'

#para funcionar, comentar 'django.contrib.admin' do settings.py nos apps instalados, comentar path('admin/', admin.site.urls)
# e from django.contrib import admin do urls.py do mysite, fazer MIGRATE começando pelo users, depois blog e por último biblioteca
# depois disso descomentar o que foi comentado