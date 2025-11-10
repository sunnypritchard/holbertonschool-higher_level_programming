/*
This script add the class 'red' to the header element
when user clicks on the element with id 'red_header'.
*/

function addClass (element, className) {
  element.classList.add(className);
}

const redHeader = document.querySelector('#red_header');
const header = document.querySelector('header');

redHeader.addEventListener('click', function () {
  addClass(header, 'red');
});

console.log('Script loaded: addClass to header on click');
