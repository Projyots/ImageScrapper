from bs4 import BeautifulSoup as bs
import os
import json
import time
import urllib.request
import urllib.parse
import urllib.error
import requests
import html5lib
from urllib.request import urlretrieve




class ImageScrapper:

    def delete_existing_image(self, list_of_images):
        for self.image in list_of_images:
            try:
                os.remove("./static/" + self.image)
                print("Removed everything")
            except Exception as e:
                print('error in deleting:  ', e)
        return 0

    def list_only_jpg_files(self, folder_name):
        self.list_of_jpg_files = []
        self.list_of_files = os.listdir(folder_name)
        print('list of files == ')
        print(self.list_of_files)
        for self.file in self.list_of_files:
            self.name_array = self.file.split('.')
            if self.name_array[1] == 'jpg':
                self.list_of_jpg_files.append(self.file)
            else:
                print('filename does not end with "jpg"')
        return self.list_of_jpg_files

    def createURL(keyWord):
        keyWord = keyWord.split()
        keyWord = '+'.join(keyWord)
        url = "https://www.google.co.in/search?q=" + keyWord + "&source=lnms&tbm=isch"
        return url
        # print (url)
        # add the directory for your image here

    def get_RawHtml(url, header):
        # url = "https://acadgild.com/customers/reviews"
        # header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
        req = urllib.request.Request(url, headers=header)
        resp = urllib.request.urlopen(req)
        respData = resp.read()

        html = bs(respData, 'html.parser')
        # html = bs(respData, 'html.parser')
        return html

    # contains the link for Large original images, type of  image
    def getimageUrlList(rawHtml):
        imageUrlList = []
        for a in rawHtml.find_all("div", {"class": "rg_i Q4LuWd"}):
            link, imageExtension = json.loads(a.text)["ou"], json.loads(a.text)["ity"]
            imageUrlList.append((link, imageExtension))

        print("there are total", len(imageUrlList), "images")
        return imageUrlList

    def downloadImagesFromURL(folder_path, urls):

        for counter, url in enumerate(urls):

            try:
                image_content = requests.get(url).content

            except Exception as e:
                print(f"Error - Could not download {url} - {e}")

            try:
                f = open(os.path.join(folder_path, 'jpg' + "_" + str(counter) + ".jpg"), 'wb')
                f.write(image_content)
                f.close()

                print(f"Success-saved {url} -as {folder_path}")
            except Exception as e:
                print(f"ERROR- Could not save {url} - {e}")

        masterListOfImages = os.listdir('static')
        return masterListOfImages



    def fetch_image_urls(query, max_links_to_fetch, wd, sleep_between_interactions):

        def scroll_to_end(wd):
            wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(sleep_between_interactions)

        # build Google Query
        # {q} - The search element is passed as 'q'.

        search_url = "http://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&gs_I=img"

        # load the page
        wd.get(search_url.format(q=query))

        image_urls = []
        image_count = 0
        result_start = 0

        while image_count < max_links_to_fetch:

            scroll_to_end(wd)

            # get all images thumbnail

            thumbnail_results = wd.find_elements_by_css_selector('img.Q4LuWd')
            number_results = len(thumbnail_results)

            print(f"Found : {number_results} search results. Extracting links from {result_start}:{number_results}")

            for img in thumbnail_results[result_start:number_results]:

                # try to click on every thumbnail so that we can get the image behind it

                try:

                    img.click()
                    time.sleep(sleep_between_interactions)
                except Exception:
                    continue

                # Extract Image urls

                actual_images = wd.find_elements_by_css_selector('img.n3VNCb')
                for actual_image in actual_images:
                    if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):

                        image_urls.append(actual_image.get_attribute('src'))

                image_count = len(image_urls)

                if len(image_urls) >= max_links_to_fetch:
                    print(f"Found : {len(image_urls)} image links, done!")
                    break
            else:
                print(f"Found: ", len(image_urls), "image links, looking for more")
                time.sleep(30)
                return
                load_more_button = wd.find_elements_by_css_selector(".mye4qd")
                if load_more_button:
                    wd.execute_script("document.querySelector('.mye4qd').click();")

            # move the results startpoint further down

            results_starts = len(thumbnail_results)
        imageUrlList = image_urls
        return imageUrlList

    '''
        for i, (img, Type) in enumerate(imageUrlList):

            try:
                req = urllib.request.Request(img, headers=header)
                respData = urllib.request.urlopen(req)
                raw_img = respData.read()

                cntr = len([i for i in os.listdir(fileLoc) if image_type in i]) + 1
                print(cntr)
                if len(Type) == 0:
                    f = open(os.path.join(fileLoc, image_type + "_" + str(cntr) + ".jpg"), 'wb')
                else:
                    f = open(os.path.join(fileLoc, image_type + "_" + str(cntr) + "." + Type), 'wb')

                f.write(raw_img)
                f.close()
            except Exception as e:
                print("could not load : " + img)
                print(e)
         '''