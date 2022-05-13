# WebPageDownload

Python script that downloads web pages for URLs passed in as arguments.\
Also displays metadata for each web page (Number of Links, Number of Images, Date and Time of Fetch).

Project includes Dockerfile and requirements.txt files for running the script through a Docker container.\
Modify inputs on line 13 of Dockerfile. Download path and urls can be modified. There can be any number of URLs passed in, must have a minimum of one.\
Sample inputs are provided in current version of Dockerfile.

main.py can also be run locally after installing Python 3 and the necessary dependencies (listed in requirements.txt).\
Example of running from Windows cmd: $ python main.py C:\\\\Temp https://jisho.org/ https://www.tokyodev.com/ \
Specify python3 if both versions of Python are installed.\
Use double backslashes for Windows file paths to avoid escaping characters i.e. C:\\\\Temp
