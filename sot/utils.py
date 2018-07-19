def try_except(success, exception, error):
    try:
        return success()
    except exception as e:
        return error(e)
