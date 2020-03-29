import sys, re
import bs4, requests
from .mal_file import edit_file

def get_user_input(flag): 
    """
    Returns a string containing user provided movie/tv title

    Parameters
    ----------
    flag : int
        flag is set to changed to 1 if we are searching again.
        Otherwise the flag is 0.

    Returns
    -------
    str
        User input

    """
    if flag == 0:
        if len(sys.argv) > 1:
            return " ".join(sys.argv[1:])
        else:
            return input("Enter the title of the anime movie or show you want to search for or M for more options: ")
    else:
        return input("Enter the title of the anime movie or show you want to search for or M for more options: ")


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


def search_mal(title, choice='m'):
    """
    Shows search results for given title and returns the link to user's selection.

    Parameters
    ----------
    title : str
        Title of anime movie or show
    choice : str
        Either the letter 'M' | 'm' or a number

    Returns
    -------
    str
        Link of user's selection
    str
        Title name of link
    """
    if title == "":
        print("Did not provide a title.")
        return None, None
    
    if title.lower() == "m":
        print("\nMore Options:\n")
        print("(1). Change csv file name")
        print("")
        while True:
            selection = input("Selection: ")
            if (selection == "1"):
                fname = ""
                while True:
                    fname = input("New csv file name (include .csv file extension): ")
                    if fname == "":
                        print("Please enter a valid name.")
                    else:
                        break
                edit_file(fname)
                break
            else:
                print("\nPlease select again\n")
        return None, None
    else:
        link = 'https://myanimelist.net/anime.php?q={}&show={}'
        num = 0
        search_soup = get_soup(link.format('+'.join(title.split()), num))
        search_results = search_soup.findAll('a', class_='hoverinfo_trigger fw-b fl-l')

        if search_results:
            options = []

            for search_field in search_results:
                options.append(search_field)
            
            if options != []:
                i = 0
                length = len(options)
                temp = 0

                if (length > 5):
                    num = 5
                else:
                    num = length
                
                while True:
                    print("")
                    print("{} results were found for {}".format(num, title))
                    print("")

                    if (i == num):
                        i = temp
                    else:
                        temp = i

                    for i in range(i, num):
                        print('({}). {}'.format(i + 1, options[i].string))
                        i += 1

                    choice = input('\nEnter the number corresponding with your choice, (M)ore for more results, or <Enter> to quit: ')
                    
                    try: 
                        if (choice[0].lower() == 'm'):
                            if num < length:
                                num += 5
                            else:
                                search_results = get_soup(link.format('+'.join(title.split()), num)).findAll('a', class_='hoverinfo_trigger fw-b fl-l')
                                for search_field in search_results:
                                    options.append(search_field.string)
                                length = len(options)
                        elif (choice.isdigit()):
                            try:
                                return options[int(choice) - 1].get('href'), options[int(choice) - 1].string
                            except: 
                                pass
                        else:
                            continue
                    except:
                        quit()

        else:
            print("No Results Found")
            return None, None


def mal_get_all_info(link, title):
    """
    Given the HTML soup returns the score.

    Parameters
    ----------
    mal_soup : str
        HTML soup from beautiful soup
    title : str
        Name of anime

    Returns
    -------
    str
        Rating from the soup
    """
    anime_dict = dict()
    mal_soup = get_soup(link)

    anime_dict['Title'] = title
    anime_dict['Rating'] = mal_get_rating(mal_soup)
    anime_dict['Episodes'] = mal_get_episodes(mal_soup)
    anime_dict['Aired'] = mal_get_aired(mal_soup)
    anime_dict['Synopsis'] = mal_get_synopsis(mal_soup)

    return anime_dict


def mal_get_rating(mal_soup):
    """
    Given the HTML soup returns the score.

    Parameters
    ----------
    mal_soup : str
        HTML soup from beautiful soup

    Returns
    -------
    str
        Rating from the soup
    """
    search_results = mal_soup.findAll('span', itemprop='ratingValue')
    return search_results[0].string


def mal_get_episodes(mal_soup):
    """
    Given the HTML soup returns the number of episodes.

    Parameters
    ----------
    mal_soup : str
        HTML soup from beautiful soup

    Returns
    -------
    str
        Number of episodes from the soup
    """
    search_results = mal_soup.findAll('span', id='curEps')
    return search_results[0].string


def mal_get_aired(mal_soup):
    """
    Given the HTML soup returns time period aired.

    Parameters
    ----------
    mal_soup : str
        HTML soup from beautiful soup

    Returns
    -------
    str
        Show's time period aired from the soup
    """
    search_results = mal_soup.findAll('div', class_='spaceit')
    return search_results[1].contents[2].strip()


def mal_get_synopsis(mal_soup):
    """
    Given the HTML soup returns the synopsis.

    Parameters
    ----------
    mal_soup : str
        HTML soup from beautiful soup

    Returns
    -------
    str
        Synopsis from the soup
    """   
    search_results = mal_soup.findAll('span', itemprop='description')
    res = ""
    for result in search_results:
        for item in result.contents:
            res += str(item).strip()
    res = res.replace("<br/>", "\n")
    return res


def print_mal_dict(mal_dict):
    """
    Given the dictionary filled with information from anime page,
    prints the information out to screen.

    Parameters
    ----------
    mal_dict : dict
        Dictionary filled with information from anime page

    Returns
    -------
    None
        Prints to screen
    """
    print("")
    print("--------------------------------------------------------------------")
    print("")
    print(mal_dict['Title'])
    print("Rating: " +  mal_dict['Rating'])
    print("Number of Episodes: " +  mal_dict['Episodes'])
    print("Aired: " +  mal_dict['Aired'])
    print("Synopsis: " +  mal_dict['Synopsis'])
    print("")
    print("--------------------------------------------------------------------")
    print("")
    return


def search_again():
    """
    Gives the option to search again if wanted.

    Parameters
    ----------
    None

    Returns
    -------
    int | function()
        Either 1 if we want to search again or 
        quit() if we do not want to search again
    """
    while True:
        choice = input("Would you like to restart program? (Y/N): ")
        try:
            if choice[0].lower() == 'y':
                return 1
            elif choice[0].lower() == 'n':
                return quit()
            else:
                print("Incorrect input. Please enter Y/y or N/n.")
        except:
            return quit()