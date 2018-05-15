# FapLater
ImageFap Gallery Downloader Written In Python


## What is this?
This Python script allows you to download files from the explicit image-hosting website, [ImageFap](https://imagefap.com/). Currently, you can only download from gallery links and not from search results or from profiles. The script requires at minimum Python 3.x, however it was written and tested using Python 3.6.5.

## Dependencies
This project relies on the following Python libraries:

- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) - Scraping the webpage
- [Requests](http://docs.python-requests.org/en/master/) - Retrieving webpage

## Installation
To install the script, download the repository and put it in your directory of choice. Keep in mind that the script will download images into the folder which it is located within. Also, ensure that Python is installed. It should come preinstalled on most Linux distributions, however macOS may have a slightly older version of Python. if in doubt, install any version of Python 3 from [the official Python website](https://python.org).

Once Python is installed, be sure to install all of the external dependencies. The easiest way to install these dependencies is using the `pip` command (or `pip3` depending on your system), like so:

```bash
pip3 install beautifulsoup4 requests
```

On macOS/Linux, you may need to run this command with superuser privileges. Packages may also be available to install from source. Check the respective websites for each of the dependencies if you wish to go about installation in this way.

## Usage
All downloads will install into the same folder as the script file. Folders will also be named according to their gallery ID, so keep this in mind if you are downloading multiple galleries and wish to keep them organised. The script will download galleries in the order which the links are passed. You can use this to rename galleries if you wish through sorting from the last date added in your file manager.

### Downloading a Gallery

```bash
python3.6 main.py http://www.imagefap.com/pictures/6011052/Lucy-Pinder
```

### Downloading Multiple Galleries

```bash
python3.6 main.py http://www.imagefap.com/pictures/6011052/Lucy-Pinder http://www.imagefap.com/pictures/6433324/Emma-Glover-See-Thru http://www.imagefap.com/pictures/6288310/Lucy-V
```

## Future plans

There are a number of planned features for this downloader. There is no date on when these features will be implemented, but with time hopefully this list gets shorter.

- Command Line Arguments for output folder(s). If one folder is provided, all images should be put into this folder. Unless specified otherwise with another flag, images should be put into folders based on their Gallery ID (for instance, folder may be called `schoolwork` and the structure inside would be something like `12723/ 14576/ 444553/ 22468/`)
- Ability to pass in links from search links and download all galleries from that link. If there is a duplicate link from one that has been passed in, the link on the search page should be ignored for the sake of downloading links in order passed in. Possibly also/instead of, the script could warn the user of this conflict and ask them which one to go with
- Duplicate checking. If the same link has been passed in multiple times, they should either be ignored or the user should be prompted (or both, perhaps with a flag)
- A `-f` flag, to ignore all warnings and push ahead, downloading everything without checking
- Ability to pass in links to profiles. I think ImageFap profiles can vary in structure, and therefore this may be a difficult task. I have only briefly looked into it
- Ability to name folders using a flag, for example `python3.6 main.py http://www.imagefap.com/pictures/6011052/Lucy-Pinder http://www.imagefap.com/pictures/6433324/Emma-Glover-See-Thru http://www.imagefap.com/pictures/6288310/Lucy-V -o lucy-pinder-gallery emma-glover-gallery lucy-collett-gallery`
- Add more cake

## License
This project is licensed under the MIT license. See `license.txt` for more information.

##

Happy Trails, friend.
