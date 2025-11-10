/*
This script fetches the character data from the Star Wars API
and displayed the name of the character in the HTML element with id 'character'.
*/

function fetchCharacterData (characterId) {
  const url = `https://swapi-api.hbtn.io/api/people/${characterId}/?format=json`;

  fetch(url)
    .then(Response => Response.json())
    .then(data => {
      const characterName = data.name;
      const characterElement = document.getElementById('character');
      characterElement.textContent = characterName;
    })
    .catch(error => {
      console.error('Error fetching character data:', error);
    });
}

fetchCharacterData(5);
