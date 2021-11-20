# import external libraries
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

# Download a single file
#Signature: dataset_download_file(dataset, file_name, path=None, force=False, quiet=True)
PATH = '../../datasets/'
api.dataset_download_file('grouplens/movielens-20m-dataset','link.csv', path=PATH)

