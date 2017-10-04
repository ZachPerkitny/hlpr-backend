import hashlib


def get_gravatar_url(email):
    """
    Gets the users gravatar url
    """
    return "https://www.gravatar.com/avatar/%s" % hashlib.md5(email.lower().encode()).hexdigest()
