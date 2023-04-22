# Final Project
This is the code repository for SI507 final project. The objective of this project is to create a movie recommendation list based on the user's perference. 

## API Keys;
To generate your own API key for the database, Please go to Open Movie Database, and follow its instruction on how to acquire an API key to use.

## API Calling Format:
There are two ways to call the api. For both apporaches, besure to use this format below.

https://www.omdbapi.com/?apikey=<Your API Key>
*when using multiple parameters, besure to use "&" to separate them in URL. 
For this project, we use the movie's id on IMDB to extract information of the movie from the database, which follows the format 'ttxxxxxxx'('x' for each digit)

## Package Required:
In order to run this projecct, we need the following packages: json, random, pandas, requests, and re(the regex package).

## Do it yourself:
You can also use your own file to load a separate list of movie data, currently, it only need a list of IMDB ids. Please see the sample files
movies.csv and movie_ID_generator.py for details. 
To load a new tree, please run Final_project.py with the name of your json file as the parameter. Then, you can use the recommendation system with your own list of movies.