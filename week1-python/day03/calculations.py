def calculate_pending(total, completed):
    return total - completed


def calculate_completion_rate(total, completed):
    if total == 0:
        return 0

    return completed / total * 100