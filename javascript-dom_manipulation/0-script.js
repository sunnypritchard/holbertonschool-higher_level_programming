// This script updates the text color of the header element to red.

function updateColor (element, color) {
  element.style.color = color;
}

const header = document.querySelector('header');
updateColor(header, '#FF0000');
console.log('Header color updated to red.');
