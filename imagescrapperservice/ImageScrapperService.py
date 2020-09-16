from imagescrapper.ImageScrapper import ImageScrapper
from imagescrapperutils.ImageScapperUtils import ImageScrapperUtils
from selenium import webdriver
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("-headless")
chrome_options.add_argument("--disable-dev-shm-usages")
chrome_options.add_argument("--no-sandbox")
wd = webdriver.Chrome(executable_path = os.environ.get("CHROMEDRIVER PATH"), chrome_options = chrome_options)





#wd = webdriver.ChromeRemoteConnection(DRIVER_PATH)

target_folder = './static'

class ImageScrapperService:
    utils = ImageScrapperUtils
    imgScrapper = ImageScrapper
    keyWord = ""
    fileLoc = ""
    image_name = ""
    header = ""

    '''def __main__(keyWord, image_name, fileLoc, header):
    keyWord = keyWord
    fileLoc = fileLoc
    image_name = keyWord
    dao = DAO
    utils = ImageScrapperUtils
    imgScrapper = ImageScrapper'''

    # you can change the query for the image  here

    # pdb.set_trace()

    def downloadImages(keyWord, header):
        imgScrapper = ImageScrapper



        imageURLList = imgScrapper.fetch_image_urls(keyWord,10,wd,1)
        print("ImageURLList  ", imageURLList)
        masterListOfImages = imgScrapper.downloadImagesFromURL(target_folder, imageURLList)
        print("masterListOfImages  ",masterListOfImages)
        return masterListOfImages

    def get_image_urls(keyWord, header):
        imgScrapper = ImageScrapper
        imageURLList = imgScrapper.fetch_image_urls(keyWord,10,wd,1)
        print(imageURLList)
        return imageURLList
