"""Functions used to create menu of more options on command line."""
from .mal_file import edit_file
from .mal_profile import profile

# Constants of options available
NEW_CSV_NUM = 1
ITER_PROFILE_NUM = 2

def options_menu():
    """
    Prints the options menu to the screen.

    Parameters
    ----------
    None
        Does not take any input.

    Returns
    -------
    None
        Returns None upon completion.
    """
    print("\nMore Options:\n")
    print("({}). Change csv file name".format(NEW_CSV_NUM))
    print("({}). Get anime from MAL profile".format(ITER_PROFILE_NUM))
    print("")

def new_csv_filename(selection):
    """
    Edit the csv filename to be a different csv file to append to.

    Parameters
    ----------
    selection : int
        The selection from the options menu chosen by user.

    Returns
    -------
    None
        Returns none upon completion.
    """
    if selection == NEW_CSV_NUM:
        fname = ""
        while True:
            fname = input("New csv file name (include .csv file extension): ")
            if fname == "":
                print("Please enter a valid name.")
            else:
                break
        edit_file(fname)

def get_animes_from_userprofile(selection):
    """
    Gets a username to go to profile page and add animes from page to csv file.

    Parameters
    ----------
    selection : int
        The selection from the options menu chosen by user.

    Returns
    -------
    None
        Returns none upon completion.
    """
    if selection == ITER_PROFILE_NUM:
        uname = ""
        while True:
            uname = input("\nMAL Profile Username: ")
            if uname == "":
                print("Please enter a valid name.")
            else:
                break
        profile(uname)
