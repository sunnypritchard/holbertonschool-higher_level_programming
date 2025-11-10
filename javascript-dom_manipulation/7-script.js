/*
This script fetches and list the titles of all Star Wars movies
from the Star Wars API and displays them in the HTML element with id 'list_movies'.
*/

function fetchAndListMovies () {
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

  fetch(url)
    .then(response => response.json())
    .then(data => {
      const movies = data.results;
      const listElement = document.getElementById('list_movies');

      movies.forEach(movie => {
        const listItem = document.createElement('li');
        listItem.textContent = movie.title;
        listElement.appendChild(listItem);
      });
    })
    .catch(error => {
      console.error('Error fetching movies:', error);
    });
}

fetchAndListMovies();

console.log('Script loaded: fetchAndListMovies');
