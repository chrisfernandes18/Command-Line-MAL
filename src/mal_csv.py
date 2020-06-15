import csv, os, operator
from .mal_soup import search_again
from .mal_file import file_exists, read_file, create_file

dir = ""
if os.name == 'nt':
    dir = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop/')
else:
    dir = "~/Desktop/"

def export_to_csv(mal_dict, option=0):
    """
    Returns a string containing user provided csv filename.

    Parameters
    ----------
    mal_dict : dict
        Dictionary containing information about the title.
    option : int
        Refers to if exporting singluar anime or profile.

    Returns
    -------
    search_again() | None
        Function to search another title or returns None upon copmletion.

    """
    export = 'y'
    if (option == 0):
        export = input("Would you like to add this to a csv file (Y/N)? ")
        export = export[0].lower()
    
    while True:
        if (export == 'y'):
            csv_file = ""
            if file_exists():
                csv_file = read_file()
                csv_file = csv_file.strip()
            else:
                csv_file = input("What is the name of your CSV file (include .csv extension)?: ")
                create_file(csv_file)
            os.chdir(os.path.expanduser(dir))
            
            col_names = []
            for key in mal_dict.keys():
                col_names.append(key)
            if os.path.exists(csv_file):
                try:
                    sort_csv(csv_file, col_names, mal_dict)
                    if (option == 0):
                        print("Title was appended to an existing csv file.")
                        return search_again()
                    else:
                        return None
                except IOError:
                    print("I/O error")
            else:
                try:
                    with open(csv_file, 'a+') as csvfile:
                        writer = csv.DictWriter(csvfile, fieldnames=col_names)
                        writer.writeheader()
                        writer.writerow(mal_dict)
                    print("CSV file was created and the title was added to the file.")
                    if (option == 0):
                        return search_again()
                    else:
                        return None
                except IOError:
                    print("I/O error")
        elif (export == 'n'):
            return search_again()
        else:
            print("Please enter Y or N.")


def sort_csv(filename, col_names, mal_dict):
    """
    
    Sorts the csv file by first column and removes if the one to insert is
    already in the file.

    Parameters
    ----------
    filename : str
        The name of the file.
    col_names : list
        Contains the column names for the csv file.
    mal_dict : dict
        Contains the new, to-be-inserted title's information.

    Returns
    -------
    None 
        Returns None upon completion.
    """
    reader = csv.reader(open(filename), delimiter=",")
    sortedlist = sorted(reader, key=operator.itemgetter(0), reverse=False)
    curr = []
    
    for vals in mal_dict.values():
        curr.append(vals)
    
    if curr in sortedlist:
        sortedlist.remove(curr)
        print("Title exists in csv file. Updating the row.")
    
    sortedlist.append(curr)
    sortedlist = sorted(sortedlist, key=operator.itemgetter(0))
    sortedlist.remove(col_names)
    sortedlist.insert(0, col_names)
    os.remove(filename)
    
    with open(filename, 'a+') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(sortedlist)
    return
