worker_class = 'gevent'
timeout = 60
graceful_timeout = 60
log_file = '-'
error_logfile = '-'
access_logfile = '-'
log_level = 'info'
logger_class = 'safe_transaction_service.history.utils.CustomGunicornLogger'


def post_fork(server, worker):
    try:
        from psycogreen.gevent import patch_psycopg
        patch_psycopg()
        worker.log.info("Made Psycopg2 Green")
    except ImportError:
        worker.log.info("Psycopg2 not patched")
