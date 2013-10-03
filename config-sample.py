# Django settings for devfit project.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'devfit',  # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '127.0.0.1',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '3306',  # Set to empty string for default.
    }
}