#!/usr/bin/python3.6

# Command line options (custom output dir, auto-archive, archive type, etc)
# Progress bar
# Get all albums from a profile
# Get all albums from a search
# Output modes
# Improve command line output

import os
import shutil
import sys
import time
import getopt


try:
	import requests
except:
	print('You don\'t have requests installed. Please install via "pip3 install requests".')


try:
	from bs4 import BeautifulSoup
except:
	print('You don\'t have BeautifulSoup4 installed. Please install via "pip3 install beautifulsoup4".')


#print(len(sys.argv))

def get_gallery_id(gallery_input):
	# If "gallery/" link, take end of URL
	if 'imagefap.com' in gallery_input:
		if 'imagefap.com/gallery/' in gallery_input:
			gallery_id = gallery_input.split('imagefap.com/gallery')[1]
		else:
			gallery_id = gallery_input.split('imagefap.com/pictures/')[1]
			gallery_id = gallery_id.split('/')[0]
	else:
		print('This doesn\'t look like an ImageFap URL. Program may not work properly. You have been warned...\n\n\n')


	return gallery_id


def download_gallery(request, page=0, recursive=False):
	gallery_soup = BeautifulSoup(request.content, 'html.parser')

	user_div = gallery_soup.find(id='menubar')

	gallery_uploader = user_div.find_all('table')[0].find_all('font')[1].text.lower().split('uploaded by ')[1]

	# Overall Gallery Div
	gallery_div = gallery_soup.find(id='gallery')

	# Checking if gallery exists
	gallery_not_found = gallery_div.find('font').find('span').text

	if 'could not' in gallery_not_found.lower():
		print('\nDownloaded gallery!')

		os.chdir('..')

		return


	# Table containing images (4x3)
	gallery_table = gallery_div.find('table')
	gallery_rows = gallery_table.find_all('tr')

	# Row of images within table row
	gallery_row_images = gallery_table.find_all('td')

	images = []

	gallery_id = get_gallery_id(request.url)


	if not recursive:
		if not os.path.exists(os.path.join(os.getcwd(), gallery_id)):

			os.mkdir(gallery_id)

		os.chdir(gallery_id)


	for image in gallery_row_images:

		image_id = image.get('id')

		if image.get('id') is not None:

			img = { 'id': image_id, 'name': image.find_all('tr')[1].find('td').find_all('font')[1].find('i').text }

			# If name is truncated
			if img['name'].endswith('...'):

				img_req = requests.get('http://' + 'imagefap.com' + image.a.get('href'))

				img_req_soup = BeautifulSoup(img_req.content, 'html.parser')

				img['name'] = img_req_soup.title.text.split(' in gallery')[0]

			images.append(img)


	print()

	for image in images:

		url = 'http://x.imagefapusercontent.com/u/' + gallery_uploader + '/' + gallery_id + '/' + image['id'] + '/' + image['name']

		image_file = requests.get(url, stream=True)

		with open(image['name'], 'wb') as f:
			print('Downloading image \'' + str(url) + '\'')

			shutil.copyfileobj(image_file.raw, f)

	r = requests.get(request.url + '?gid=' + str(gallery_id) + '&page=' + str(page + 1) + '&view=0')

	download_gallery(r, page=page + 1, recursive=True)


# Change to profile/gallery and decide whether it's a gallery or profile later
gallery_input = input('Enter Gallery Link: ')

galleries = []

start = time.time()

if gallery_input.count('://') >= 1:
	galleries.extend(gallery_input.split(' '))
else:
	galleries.append(gallery_input)


if len(galleries) > 1:
	for gallery in galleries:

		try:
			gallery_request = requests.get(gallery)
		except:
			print('\nE: Gallery link invalid: ' + gallery)

			continue

		download_gallery(gallery_request)

else:
	try:
		gallery_request = requests.get(galleries[0])
	except:
		print('\nE: Gallery link invalid: ' + galleries[0])

		sys.exit()

	download_gallery(gallery_request)


end = time.time() - start

print('\nScript executed in ' + str(round(end, 3)) + 's.')
