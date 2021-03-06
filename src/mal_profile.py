"""Functions used for getting animes from MAL profile."""
import json
from time import sleep
from .mal_soup import get_soup
from .mal_dict import mal_get_all_info
from .mal_csv import export_to_csv

def profile(username):
    """
    Takes a username and iterates over all of the animes, adding them
    to the csv file.

    Parameters
    ----------
    username : str
        MAL profile username.

    Returns
    -------
    None
        Returns None upon completion.
    """
    link = "https://myanimelist.net/animelist/{}".format(username)
    mal_soup = get_soup(link)
    table = json.loads(mal_soup.find('table').get('data-items'))
    print("\nRunning...\n")
    for dic in table:
        link = "https://myanimelist.net{}"
        res = mal_get_all_info(link.format(dic['anime_url']), dic['anime_title'])
        export_to_csv(res, 1)
        sleep(5)
    print("Finished.")
