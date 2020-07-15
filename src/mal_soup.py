""""Functions used to gete the html soup and to search again in command line."""
import bs4
import requests

def get_soup(link):
    """
    Gets the HTML for a link. Throws error if it does not connect to website.

    Parameters
    ----------
    link : str
        URL to the webpage.

    Returns
    -------
    str
        HTML of the link.

    """
    page = requests.get(link)
    page.raise_for_status()
    soup = bs4.BeautifulSoup(page.text, 'html.parser')
    return soup


def search_again():
    """
    Gives the option to search again if wanted.

    Parameters
    ----------
    None

    Returns
    -------
    int | function()
        Either 1 if we want to search again o
        quit() if we do not want to search again.
    """
    while True:
        choice = input("Would you like to restart program? (Y/N): ")
        try:
            if choice[0].lower() == 'y':
                return 1
            if choice[0].lower() == 'n':
                return quit()
            print("Incorrect input. Please enter Y/y or N/n.")
        except IndexError:
            return quit()
