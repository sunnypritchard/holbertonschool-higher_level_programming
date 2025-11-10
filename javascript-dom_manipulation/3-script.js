/*
This script toggles ('red' || 'green') the class of the header element
when user clicks on the element with id 'toggle_header'.
*/

function toggleClass (element, className1, className2) {
  if (element.classList.contains(className1)) {
    element.classList.replace(className1, className2);
  } else {
    element.classList.replace(className2, className1);
  }
}

const toggleHeader = document.querySelector('#toggle_header');
const header = document.querySelector('header');

toggleHeader.addEventListener('click', function () {
  toggleClass(header, 'red', 'green');
});
