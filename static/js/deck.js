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

function setupDeckButtons () {
  const buttons = dqsA('.shwcards')
  for (const button of buttons) {
    button.addEventListener('click', function (event) {
      const url = event.target.dataset.url
      const display = dqs('#card-display')
      fetch(url)
        .then(res => res.json())
        .then(json => {
          display.innerHTML = ''
          for (const card of json.cards) {
            const newDiv = document.createElement('div')
            newDiv.classList.add('card')
            newDiv.id = card.id

            const title = document.createElement('p')
            title.innerText = card.title
            title.classList.add('card-title')

            newDiv.appendChild(title)
            display.appendChild(newDiv)
          }
        })
    })
  }
}

// function showDeckCards (cardset) {
// }

setupDeckButtons()
showHide('#newdeckformSH')
newDeckForm()

// const data = {
//  id: 1,
//   cards: [{
//  id: 2,
//     title: 'Danger',
//     answer: 'Killer Rabbit',
//     subject: 'Lethal Lethalities',
//     created_at: '2020-03-15T17:05:26.788092Z',
// decks: [1]
//  }, { id: 9, title: 'French Sayings', answer: 'hamster, elderberries', subject: 'Oooo that smell', created_at: '2020-03-15T17:05:26.788092Z', decks: [1] }, { id: 5, title: 'Old man on the bridge', answer: 'African or European?', subject: 'Swallows', created_at: '2020-03-15T17:05:26.788092Z', decks: [1] }, { id: 3, title: 'Old man on the bridge', answer: 'Blue, no yeeeellllloooooowwwwww', subject: 'Philosophy', created_at: '2020-03-15T17:05:26.788092Z', decks: [1] }],
// name: 'Monty Python Quiz',
// created_at: '2020-03-15T17:05:26.799462Z'
//  }
