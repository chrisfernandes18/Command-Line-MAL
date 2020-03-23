import csv, os, operator
from .cmd_mal import search_again


def export_to_csv(mal_dict):
    """
    Returns a string containing user provided csv filename

    Parameters
    ----------
    mal_dict : dict
        Dictionary containing information about the title

    Returns
    -------
    search_again()
        function to search another title

    """
    export = input("Would you like to add this to a csv file (Y/N)? ")
    export = export[0].lower()
    while True:
        if (export == 'y'):
            csv_file = input("What is the name of your CSV file (include filepath and .csv extension)?: ")
            col_names = []
            for key in mal_dict.keys():
                col_names.append(key)
            if os.path.exists(csv_file):
                try:
                    sort_csv(csv_file, col_names, mal_dict)
                    print("Title was appended to an existing csv file.")
                    return search_again()
                except IOError:
                    print("I/O error")
            else:
                try:
                    with open(csv_file, 'a+') as csvfile:
                        writer = csv.DictWriter(csvfile, fieldnames=col_names)
                        writer.writeheader()
                        writer.writerow(mal_dict)
                    print("CSV file was created and the title was added to the file.")
                    return search_again()
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