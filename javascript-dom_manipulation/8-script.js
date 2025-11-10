/*
This script fetches data from the Hello API and displays the greeting message
in the HTML element with id 'hello'.
*/

function fetchHelloMessage () {
  const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';

  fetch(url)
    .then(response => response.json())
    .then(data => {
      const helloMessage = data.hello;
      const helloElement = document.getElementById('hello');
      helloElement.textContent = helloMessage;
    });
}

fetchHelloMessage();
