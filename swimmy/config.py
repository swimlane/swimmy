import os


class Config:

    slack = {
        'bot_username': os.environ.get('SLACK_BOT_USERNAME', 'swimmy'),
        'bot_token': os.environ.get('SLACK_BOT_TOKEN', None),
        'bot_signing_secret': os.environ.get('SLACK_BOT_SIGNING_SECRET', None)
    }

    swimlane = {
        'host': os.environ.get('SWIMLANE_HOST', None),
        'username': os.environ.get('SWIMLANE_USERNAME', None),
        'password': os.environ.get('SWIMLANE_PASSWORD', None),
        'access_token': os.environ.get('SWIMLANE_ACCESS_TOKEN', None),
        'verify_ssl': bool(os.environ.get('SWIMLANE_VERIFY_SSL', False)),
        'verify_server_version': bool(os.environ.get('SWIMLANE_VERIFY_SERVER_VERSION', False)),
        'default_timeout': int(os.environ.get('SWIMLANE_DEFAULT_TIMEOUT', 300)),
        'resource_cache_size': int(os.environ.get('SWIMLANE_RESOURCE_CACHE_SIZE', 0)),
        'write_to_read_only': bool(os.environ.get('SWIMLANE_WRITE_TO_READ_ONLY', False)),
    }
    search_results_max_results = int(os.environ.get('SWIMLANE_SEARCH_RESULTS_MAX_RESULTS', 10))
