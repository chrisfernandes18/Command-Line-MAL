import csv, os.path
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
                    with open(csv_file, 'a+') as csvfile:
                        writer = csv.DictWriter(csvfile, fieldnames=col_names)
                        writer.writerow(mal_dict)
                    print("Title was added to csv file.")
                    return search_again()
                except IOError:
                    print("I/O error")
            else:
                try:
                    with open(csv_file, 'a+') as csvfile:
                        writer = csv.DictWriter(csvfile, fieldnames=col_names)
                        writer.writeheader()
                        writer.writerow(mal_dict)
                    print("Title was added to csv file.")
                    return search_again()
                except IOError:
                    print("I/O error")
        elif (export == 'n'):
            return search_again()
        else:
            print("Please enter Y or N.")

