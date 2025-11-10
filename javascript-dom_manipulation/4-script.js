/*
This script adds a li element with text 'Item' to the ul element
when user clicks on the element with id 'add_item'.
*/

function addListItem (ulElement, itemText) {
  const li = document.createElement('li');
  li.textContent = itemText;
  ulElement.appendChild(li);
}

const addItem = document.querySelector('#add_item');
const ul = document.querySelector('ul');

addItem.addEventListener('click', function () {
  addListItem(ul, 'Item');
});

console.log('Script loaded: addListItem to ul on click');
