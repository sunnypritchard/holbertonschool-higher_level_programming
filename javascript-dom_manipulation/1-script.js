/*
This script updates the text color of the header element to red
when user clicks on the element with id 'red_header'.
*/

function updateColor (element, color) {
  element.style.color = color;
}

const header = document.querySelector('#red_header');

header.addEventListener('click', function () {
  updateColor(header, '#FF0000');
});
