import json
from .mal_soup import get_soup
from .mal_dict import mal_get_all_info

def profile(username):
    """
    Takes a username and iterates over all of the animes, adding them
    to the csv file.

    Parameters
    ----------
    username : str
        MAL profile username

    Returns
    -------
    None
        Returns None upon completion.
    """
    link = "https://myanimelist.net/animelist/{}".format(username)
    mal_soup = get_soup(link)
    table = json.loads(mal_soup.find('table').get('data-items'))
    
    for dic in table:
        link = "https://myanimelist.net{}"
        res = mal_get_all_info(link.format(dic['anime_url']), dic['anime_title'])
        print(res)
    return