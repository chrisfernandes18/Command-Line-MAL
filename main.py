"""Executes the entire program"""
from src.mal_cmd import  get_user_input, search_mal, print_mal_dict
from src.mal_csv import export_to_csv
from src.mal_dict import mal_get_all_info

def main(flag=0):
    """
    Given a flag that is presumed to be 0, runs the command line program.

    Parameters
    ----------
    flag : int
        flag is set to changed to 1 if we are searching again.
        Otherwise the flag is 0.

    Returns
    -------
    int
        Returns 0 upon completion.
    """
    while True:
        link, title = search_mal(get_user_input(flag))
        if link is None:
            continue
        mal_dict = mal_get_all_info(link, title)
        print_mal_dict(mal_dict)
        flag = export_to_csv(mal_dict)
    return 0

if __name__ == "__main__":
    main()
