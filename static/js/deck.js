/* globals fetch */

function dqs (elementID) {
  return document.querySelector(elementID)
}

function dqsA (elementClass) {
  return document.querySelectorAll(elementClass)
}

function hide (element) {
  element.classList.add('dn')
}

function show (element) {
  element.classList.remove('dn')
}

function newDeckForm () {
  const form = dqs('#deckcreate')
  form.addEventListener('submit', function (event) {
    // event.preventDefault()
    fetch('/view_decks/new/', {
      method: 'POST',
      body: JSON.stringify({ name: dqs('#name').value })
    })
      // .then(res => res.text())
      // .then(text => console.log(text))
      .then(res => res.json())
      .then(json => {
        if (json.status === 'ok') {
          console.log('NEW DECK CREATED')
        }
      })
  })
}

function showHide (buttonID) {
  const button = dqs(buttonID)
  button.addEventListener('click', function (event) {
    const query = document.getElementById(event.target.dataset.showhide)
    console.log(query)
    if (query.classList.contains('dn')) {
      show(query)
    } else {
      hide(query)
    }
  })
}

showHide('#newdeckformSH')
newDeckForm()
