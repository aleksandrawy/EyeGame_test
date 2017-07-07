import time


def wait_until(condition, timeout=10, raise_exception=True, msg=""):
    start = time.time()
    while (time.time() - start < timeout):
        if condition():
            return True
        else:
            time.sleep(0.1)

    if raise_exception:
        return TimeoutError(f"Condition not fulfilled {msg} after {timeout} sec")
    else:
        return False
