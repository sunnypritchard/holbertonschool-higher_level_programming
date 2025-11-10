/*
This script updates the text of the header element to "New Header!!!"
when user clicks on the element with id 'update_header'.
*/

function updateHeaderText (element, newText) {
    element.textContent = newText;
}

const headerText = document.querySelector('#update_header');
const header = document.querySelector('header');

headerText.addEventListener('click', function () {
    updateHeaderText(header, 'New Header!!!');
});

console.log('Script loaded: updateHeaderText on click');