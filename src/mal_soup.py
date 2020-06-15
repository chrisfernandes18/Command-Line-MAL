import bs4, requests

def get_soup(link):
    """
    Gets the HTML for a link. Throws error if it does not connect to website.

    Parameters
    ----------
    link : str
        URL to the webpage

    Returns
    -------
    str
        HTML of the link

    """
    page = requests.get(link)
    page.raise_for_status()
    soup = bs4.BeautifulSoup(page.text, 'html.parser')
    return soup