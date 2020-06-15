from .mal_soup import get_soup

def mal_get_all_info(link, title):
    """
    Returns a dictionary containing all relevant information from the 
    anime webpage.

    Parameters
    ----------
    link : str
        Link to specific anime page on MAL.
    title : str
        Name of anime.

    Returns
    -------
    dict
        Dictionary containing all the information from anime page.
    """
    anime_dict = dict()
    mal_soup = get_soup(link)

    anime_dict['Title'] = title
    anime_dict['Rating'] = mal_get_rating(mal_soup)
    anime_dict['Episodes'] = mal_get_episodes(mal_soup)
    anime_dict['Aired'] = mal_get_aired(mal_soup)
    anime_dict['Synopsis'] = mal_get_synopsis(mal_soup)
    anime_dict['Related Anime'] = mal_get_related_anime(mal_soup)
    return anime_dict


def mal_get_rating(mal_soup):
    """
    Given the HTML soup returns the score.

    Parameters
    ----------
    mal_soup : str
        HTML soup from beautiful soup.

    Returns
    -------
    str
        Rating from the soup.
    """
    search_results = mal_soup.findAll('span', itemprop='ratingValue')
    try:
        return search_results[0].string
    except:
        return "?"


def mal_get_episodes(mal_soup):
    """
    Given the HTML soup returns the number of episodes.

    Parameters
    ----------
    mal_soup : str
        HTML soup from beautiful soup.

    Returns
    -------
    str
        Number of episodes from the soup.
    """
    search_results = mal_soup.findAll('span', id='curEps')
    try:
        return search_results[0].string
    except:
        return "?"


def mal_get_aired(mal_soup):
    """
    Given the HTML soup returns time period aired.

    Parameters
    ----------
    mal_soup : str
        HTML soup from beautiful soup.

    Returns
    -------
    str
        Show's time period aired from the soup.
    """
    search_results = mal_soup.findAll('div', class_='spaceit')
    try:
        return search_results[1].contents[2].strip()
    except:
        return "?"


def mal_get_synopsis(mal_soup):
    """
    Given the HTML soup returns the synopsis.

    Parameters
    ----------
    mal_soup : str
        HTML soup from beautiful soup.

    Returns
    -------
    str
        Synopsis from the soup.
    """   
    search_results = mal_soup.findAll('span', itemprop='description')
    res = ""
    for result in search_results:
        for item in result.contents:
            res += str(item).strip()
    res = res.replace("<br/>", "\n")
    res = res.replace("<i>", "")
    res = res.replace("</i>", "")
    return res


def mal_get_related_anime(mal_soup):
    """
    Given the HTML soup returns the related anime information.

    Parameters
    ----------
    mal_soup : str
        HTML soup from beautiful soup.

    Returns
    -------
    str
        Related anime information from the soup.
    """
    search_results = mal_soup.findAll('table', class_='anime_detail_related_anime')
    result = []
    try:
        result = search_results[0].findAll('tr')
    except:
        pass
    string = ""
    for item in result:
        num = 0
        for content in item.contents[:2]:
            if num == 1:
                string += content.find('a').string
            else:
                string += content.string + " "
            num += 1
        string += "\n"
    return string
