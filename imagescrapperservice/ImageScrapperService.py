from imagescrapper.ImageScrapper import ImageScrapper
from imagescrapperutils.ImageScapperUtils import ImageScrapperUtils
from selenium.webdriver.chrome import webdriver


DRIVER_PATH = r'C:\Users\pRoJyot\Downloads\Programs\chromedriver.exe'
#wd = webdriver.ChromeRemoteConnection(DRIVER_PATH)
wd = webdriver.WebDriver(executable_path = DRIVER_PATH)
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
