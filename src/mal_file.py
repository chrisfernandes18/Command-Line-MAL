import os.path

file_path = os.path.abspath(__file__).replace("src/mal_file.py", "") + "assets/file/file.txt"

def file_exists():
    """
    Returns a boolean indicating whether the file containing the csv file
    we want to append to exists or not.

    Parameters
    ----------
    None : NoneType

    Returns
    -------
    boolean
        True if file exists, false if it does not exist

    """
    return os.path.exists(file_path)

def create_file(filename):
    """
    Creates a text file containing the name of the file we want to append to.

    Parameters
    ----------
    filename : str
        Name of the file to put into the text file

    Returns
    -------
    None

    """
    open(file_path, 'a+').write(filename + "\n")
    return

def read_file():
    """
    Returns the name of the csv file we are appending to

    Parameters
    ----------
    None: NoneType

    Returns
    -------
    str
        Name of the csv file we want to add to.

    """
    return open(file_path, 'r').readline()