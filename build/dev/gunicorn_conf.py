"""
Gunicorn config file for local/dev environments.

For configuration details: http://docs.gunicorn.org/en/stable/configure.html
"""

# Server Socket
backlog = 2048  # default
bind = "0.0.0.0:8000"

# Worker Processes
timeout = 60
graceful_timeout = 30
keepalive = 2  # default
max_requests = 0  # default
worker_class = "sync"
worker_connections = 1000  # default
workers = 2

# Server Mechanics
chdir = "/opt/urbandata-test/"
daemon = False  # default
pidfile = "/var/run/gunicorn.pid"
umask = 0  # default
worker_tmp_dir = "/dev/shm"   # http://docs.gunicorn.org/en/stable/faq.html#blocking-os-fchmod

# Environment
raw_env = [
    "DJANGO_SETTINGS_MODULE=config.settings.dev",
]

# Debugging
reload = True

# Logging
accesslog = "-"
errorlog = "-"  # default
loglevel = "debug"
