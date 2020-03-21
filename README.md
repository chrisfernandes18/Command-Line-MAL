# Command Line MA
Inspired by https://github.com/Bryce-Tucker/Command-Line-IMDB

A python script that allows you to look up movies and shows on MyAnimeList.net from the command line.

![Demo Gif](assets/images/cmd_demo.gif)

### Required Python Modules
Requires two third party modules:

1. **requests** : A module for sending HTTP/1.1 requests using Python.

2. **beautifulsoup4** : A module for parsing HTML and XML documents.

### Using The Program

Once the modules are installed, enter the directory which contains the scripts in the terminal. The name of the show or movie can be searched either just running the program and then inputing the name or or the name follows the program as a command line argument.

---
`python3 cmd_mal.py Black Clover`

or

`python3 cmd_mal.py` <br>
`Enter the title of the anime movie or show you want to search for: Black Clover`


---
When a search title has been provided, the program will output the number of results on MyAnimeList.net for that title, and then give a numbered list containing the first 5 results. The user can then select from a result from the list by entering the corresponding number, request the next 5 results by entering m, or exit by hitting enter. The user is able to keep requesting more results until every result has been displayed.

![More Results for Black Clover](assets/images/more_results.png)

Once a result has been selected by the user, the program will output the title, rating, number of episodes, when the show aired, and synopsis. Then it will ask if the user would like to search again.

![Output for Black Clover](assets/images/output.png)

### Coming Soon
Ability to make a new csv file if one does not exist that holds a list of anime that one has searched and wants to keep the information.