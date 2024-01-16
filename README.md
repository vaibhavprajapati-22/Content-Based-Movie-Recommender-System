# Content Based Movie Recommender System
This repository contains the code and resources for a Content-Based Movie Recommender System. The system recommends movies to users based on the similarity between the movies. This Content-Based Movie Recommender System is built using python.It takes into account the features of movies, such as genre and year of release to recommend similar movies to users.
## Instalation
To get started, follow these steps:
1. Clone the repository:
  ```sh
  git clone https://github.com/vaibhavprajapati-22/content-based-movie-recommender.git
  cd content-based-movie-recommender
  ```
2. Install the required dependencies:
  ```sh
  pip install -r requirements.txt
  ```
3. Run the Jupyter Notebook:
   <ul>
        <li>Open model.ipynb in Jupyter Notebook.</li>
        <li>Run each cell to generate the similarity_matrix.pkl file.</li>
    </ul>
4. Run the Flask App:
  ```sh
  python app.py
  ```
5. Access the Recommender System:
   <ul>
     <li>Open your web browser and go to the link provided in the terminal (e.g., http://127.0.0.1:5000).</li>
   </ul>
## Dataset
I am using the MovieLens dataset from https://grouplens.org/datasets/movielens/ . I have used MovieLens 10M Dataset.
## Algorithm
The algorithm employs a Content-Based Movie Recommender System using Count Vectorization and Cosine Similarity. It converts movie descriptions into a matrix of token counts, calculates cosine similarity between movies based on this matrix, and generates recommendations for a specified movie by sorting similar movies and returning the top 5 with their similarity scores.
## References
1. https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html
2. https://towardsdatascience.com/introduction-to-recommender-systems-6c66cf15ada
   
