# import external libraries
from kaggle.api.kaggle_api_extended import KaggleApi

# constants
PATH = '../../datasets/'
KAGGLE_PATH = 'grouplens/movielens-20m-dataset'
FILES_NAMES = ['genome_tags.csv', 'genome_scores.csv',
              'link.csv', 'movie.csv', 'rating.csv', 'tag.csv']

# keys authetication
api = KaggleApi()
api.authenticate()

# download singular file
[api.dataset_download_file(
    dataset=KAGGLE_PATH, file_name=file, path=PATH) for file in FILES_NAMES]

print("All files are downloaded")
