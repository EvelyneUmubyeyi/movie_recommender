# Movie Recommender System
[Video Demo](https://drive.google.com/file/d/13ZMgwy5vQPj6rEUnAJz9vxdJsDKtpPGm/view?usp=sharing)
[Google Colab Notebook](https://colab.research.google.com/drive/1O6l_4SltxjwRAPYO1QyQp4_lTfgPpH-h#scrollTo=UAXdtgomAotQ)

## Description

The Movie Recommender System is a web application that suggests movies to users based on the content of movies they have previously liked or watched. It utilizes a content-based recommendation approach, analyzing the characteristics of movies such as title, genre, and movie overview to recommend similar movies. The system aims to provide similar movie recommendations to users, enhancing their movie-watching experience.

## Features

- **Content-Based Recommendation:** The system recommends movies to users based on the similarity of their content to movies the user has liked or watched. The system will return the top 12 recommended movies.
- **Search functionality:**  The search functionality is powered by FuzzyWuzzy, which allows uses to search for a movie even when they might have misspelled the movie title. This fuzzy matching algorithm enhances user experience by offering flexibility and accuracy in retrieving movie results.

## Packages Used

This project has used some packages which have to be installed to run this web app locally present in `requirements.txt` file. 

## Installation

To run the project locally, there is a need to have Visual Studio Code (vs code) installed on your PC:

- **[vs code](https://code.visualstudio.com/download)**: It is a source-code editor made by Microsoft with the Electron Framework, for Windows, Linux, and macOS.

## Usage

1. Clone the project 

``` bash
git clone https://github.com/EvelyneUmubyeyi/movie_recommender.git

```

2. Open the project with vs code

``` bash
cd movie_recommender_system
code .
```

3. Install the required dependencies

``` bash
pip install -r requirements.txt
```


4. Run the project

``` bash
streamlit run app.py
```

5. Use the link printed in the terminal to visualise the app. (Usually `http://localhost:8501`)

## Important Notes
- The system provides recommendations based only on the content of movies already available in the dataset.

## Authors and Acknowledgment

- Evelyne UMUBYEYI
- Yvan SAMUNANI
- Gabin ISHIMWE
- Adrine UWERA 

## License
[MIT](https://choosealicense.com/licenses/mit/)
