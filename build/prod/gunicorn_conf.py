"""
Gunicorn config file for the production environment.

For configuration details: http://docs.gunicorn.org/en/stable/configure.html
"""
import multiprocessing

# Server Socket
backlog = 2048  # default
bind = "0.0.0.0:8000"

# Worker Processes
timeout = 60
graceful_timeout = 90
keepalive = 2  # default
max_requests = 0  # default
worker_class = "gthread"
worker_connections = 1000  # default
# These two parameter should be fine-tune on the production platform
workers = multiprocessing.cpu_count()
threads = 2

# Security
# https://docs.gunicorn.org/en/stable/settings.html#security
limit_request_fields = 100  # default
limit_request_field_size = 8190  # default
limit_request_line = 4094  # default

# Server Mechanics
chdir = "/home/appuser/urbandata-test/"
daemon = False  # default
pidfile = "/var/run/gunicorn.pid"
user = None
group = None
umask = 0  # default
worker_tmp_dir = "/dev/shm"   # http://docs.gunicorn.org/en/stable/faq.html#blocking-os-fchmod

# Environment
raw_env = [
    "DJANGO_SETTINGS_MODULE=config.settings.prod",
]

# Logging
accesslog = "-"
errorlog = "-"  # default
loglevel = "info"
