import requests

PAGEURL = "https://playoverwatch.com/en-us/career/pc/{region}/{tag}"


def find_user(battletag, region):
    if not region:
        regions = ["us", "eu", "kr"]
    else:
        regions = [region]

    for reg in regions:
        user = get_user_page(battletag, reg)

        if user is not None:
            return user, reg
    else:
        return None


def get_user_page(battletag, region):
    """
    Downloads a users playoverwatch.com page
    """
    url = PAGEURL.format(region=region, tag=battletag)

    page = get_page(url)

    if not page:
        return None

    return (page, region, battletag)


def get_page(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.text


def parseInt(input):
    """
    Attempts to parse an int or return original
    """
    a = input.replace(",", "")
    try:
        return float(a)
    except ValueError:
        return a
