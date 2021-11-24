# movies_rating_model challenge

The objective of this challenge is to assess you ability to:

> perform basic data manipulation and data pre-processing
> demonstrate awareness of the computations involved
● perform feature engineering
● train and tune ML models
● asses performance of the ML models
● obtaining clear, useful, and business driven insights from data and models

## Repository structure
URL: https://github.com/FranckEnriquez/movies_rating_model
<rootDir>
└── ml
    └── analysis
        ├── final_results
        │   ├── threshold_iteration_logreg_hyper_tuning.csv
        │   └── threshold_iteration_logreg_standard.csv
        │   └── threshold_iteration_randforest_standard.csv
        │   └── threshold_iteration_randoforest_hyper_tuning.csv     
        └── analysis.ipynb
    └── data
        ├── APIEngine
        │    ├── AWSConnector (almost done)
        │    │   └── Config.py
        │    │   └── S3.py
        │    ├── kaggleAPI (done)
        │    │    └── kaggleAPI
  └── kpis
        ├── predictions
        │   ├── df_predictions_logreg_hyper_tuning.csv
        │   └── df_predictions_logreg_standard.csv
        │   └── df_predictions_randoforest_hyper_tuning.csv
        │   └── df_predictions_randoforest_standard.csv    
        ├── utils
        │   ├── KPIs.py
        │   └── visualizations.py
  └── models
        ├── logreg
        │   ├── hyper_tuning.ipynb
        │   └── standard.ipynb 
        ├── random-forest
        │   ├── hyper_tuning.ipynb
        │   └── standard.ipynb 
   └── preprocess
        ├── utils
        │   ├── exploratory_analysis.py
        │   └── preprocess.py 
        │   └── visualizations.py 
        └── EDA.ipynb
        └── Feature_Engineering.ipynb
 └── .gitattributes
 └── .gitignore
 └── Pipfile
 └── Pipfile.loc
 └── README.md

## Initial Setup

Clone this repository and install the virtual environment of this repository.

You can create a install via  commandline.
* Using the terminal: `pipenv install`

If you don't have pipenv install yet, follow the next steps there:
https://pipenv-es.readthedocs.io/es/latest/

Activate the Pipfile:
* Windows / MacOS / Unix: `pipenv shell`

Once you activate the pipenv, there's a kaggleAPI that 
acquire the data from its web site, to use the funcion,
you need to install **unzip**:

* Linux: https://linuxize.com/post/how-to-unzip-files-in-linux/


## Contact Info

Please feel free to ask me any outstanding question or concern:

* Phone: 3331856793
* Email: franckenriquezz@iteso.mx
