import sys, shutil
from .mal_soup import get_soup
from .mal_file import edit_file
from .mal_options import options_menu, new_csv_filename, get_animes_from_userprofile

def get_user_input(flag): 
    """
    Returns a string containing user provided movie/tv title.

    Parameters
    ----------
    flag : int
        flag is set to changed to 1 if we are searching again.
        Otherwise the flag is 0.

    Returns
    -------
    str
        User input.

    """
    if (flag == 0):
        if len(sys.argv) > 1:
            return " ".join(sys.argv[1:])
        else:
            return input("Enter the title of the anime movie or show you want to search for or M for more options: ")
    else:
        return input("Enter the title of the anime movie or show you want to search for or M for more options: ")


def search_mal(title):
    """
    Shows search results for given title and returns the link to user's selection.

    Parameters
    ----------
    title : str
        Title of anime movie or show.

    Returns
    -------
    str
        Link of user's selection.
    str
        Title name of link.
    """
    if (title == ""):
        print("Did not provide a title.")
        return None, None
    
    if (title.lower() == "m"):
        options_menu()
        while True:
            selection = input("Selection: ")
            #try:
            if selection:
                selection = int(selection)
                new_csv_filename(selection)
                get_animes_from_userprofile(selection)
                break
            else:
                print("\nPlease select again\n")
            #except ValueError:
               # print("\nPlease input selection again\n")
        return None, None
    else:
        link = 'https://myanimelist.net/anime.php?q={}&show={}'
        num = 0
        search_soup = get_soup(link.format('+'.join(title.split()), num))
        search_results = search_soup.findAll('a', class_='hoverinfo_trigger fw-b fl-l')
        try:
            path = __file__
            path = path.replace("cmd_mal.py", "")
            shutil.rmtree(path + "__pycache__")
        except:
            pass
        if search_results:
            options = []

            for search_field in search_results:
                options.append(search_field)
            
            if options:
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
                            if (num < length):
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


def print_mal_dict(mal_dict):
    """
    Given the dictionary filled with information from anime page,
    prints the information out to screen.

    Parameters
    ----------
    mal_dict : dict
        Dictionary filled with information from anime page.

    Returns
    -------
    None
        Returns none upon completion.
    """
    print("")
    print("--------------------------------------------------------------------")
    print("")
    print(mal_dict['Title'])
    print("Rating: " + mal_dict['Rating'])
    print("Number of Episodes: " + mal_dict['Episodes'])
    print("Aired: " + mal_dict['Aired'])
    print("Synopsis: " + mal_dict['Synopsis'])
    print("")
    print("Related Anime:\n" + mal_dict['Related Anime'])
    print("--------------------------------------------------------------------")
    print("")
    return
