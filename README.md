# Opera rich presence (Windows only!)
Discord Rich Presence support for the Opera and Opera GX browsers.
# How to install
Requires [python](https://www.python.org/downloads/) (3.9.2 or above recommended)
Clone the repository:
![Tutorial](https://i.imgur.com/fnULDpG.png "Tutorial")

Extract the downloaded .zip file.

Next, open a command prompt in the folder you extracted (Shift+Right Click). Then enter `pip install -r requirements.txt`

Double click "main.py".
# Configuration
Add the names of websites that you want to display on rich presence to sites.json. Make sure they include their name in the tab name, or else this won't work! Make sure to follow JSON syntax! Don't know what JSON is? It's a format for storing information readable by both computers and humans. All you need to know is that you put everything inside square brackets and each value inside quotes, and put commas in between them. eg. `["Website One", "Website Two", "Website 3"]`
