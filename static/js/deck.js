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

function showHideLoop (loopedOverElement) {
  loopedOverElement.addEventListener('click', function (event) {
    loopedOverElement.parentElement.classList.add('dn')
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
            newDiv.classList.add('darkshadowbox')
            newDiv.id = `card${card.id}`

            const title = document.createElement('p')
            title.innerText = card.title
            title.classList.add('card-title')
            newDiv.appendChild(title)

            if (card.figure_raw != null) {
              const figure = document.createElement('img')
              figure.src = card.figure_raw
              figure.classList.add('card-fig')
              newDiv.appendChild(figure)
            }

            const question = document.createElement('p')
            question.innerText = card.question
            question.classList.add('card-text')
            newDiv.appendChild(question)

            if (card.figure_raw != null) {
              question.classList.add('no-figure')
            }

            const answerbutton = document.createElement('button')
            answerbutton.innerText = 'SHOW ANSWER'
            answerbutton.id = `showbutt${card.id}`
            answerbutton.classList.add('form-butt')
            answerbutton.classList.add('card-butt')
            answerbutton.dataset.showhide = `answer${card.id}`
            newDiv.appendChild(answerbutton)
            // -------------------answer card ---------------------------------
            const answerDiv = document.createElement('div')
            answerDiv.id = `answer${card.id}`
            answerDiv.classList.add('card')
            answerDiv.classList.add('answer')
            answerDiv.classList.add('dn')
            answerDiv.classList.add('darkshadowbox')

            const title2 = document.createElement('p')
            title2.innerText = card.title
            title2.classList.add('card-title')
            title2.classList.add('textglow')
            answerDiv.appendChild(title2)

            const answer = document.createElement('p')
            answer.innerText = card.answer
            answer.classList.add('card-text')
            answer.classList.add('textglow')
            answer.dataset.showhide = `answer${card.id}`
            answer.id = `answer${card.id}`
            answerDiv.appendChild(answer)

            const showcardbutton = document.createElement('button')
            showcardbutton.innerText = 'BACK TO CARD'
            showcardbutton.id = `showcard${card.id}`
            showcardbutton.classList.add('form-butt')
            showcardbutton.classList.add('card-butt')
            showcardbutton.classList.add('answer-butt')
            showcardbutton.dataset.showhide = `card${card.id}`
            answerDiv.appendChild(showcardbutton)

            display.appendChild(newDiv)
            display.appendChild(answerDiv)
          }
          setupCardButtons()
        })
    })
  }
}

function setupCardButtons () {
  const buttons = dqsA('.card-butt')
  for (const button of buttons) {
    showHideLoop(button)
  }
}

setupDeckButtons()
showHide('#newdeckformSH')
newDeckForm()

// const data = {
//  id: 1,
//   cards: [{
//  id: 2,
//  title: 'Danger',
//  answer: 'Killer Rabbit',
//  subject: 'Lethal Lethalities',
//  created_at: '2020-03-15T17:05:26.788092Z',
//  decks: [1]},{
//  id: 9,
//  title: 'French Sayings',
//  answer: 'hamster, elderberries',
//  subject: 'Oooo that smell',
//  created_at: '2020-03-15T17:05:26.788092Z',
//  decks: [1] }, {
//  id: 5,
//  title: 'Old man on the bridge',
//  answer: 'African or European?',
//  subject: 'Swallows',
//  created_at: '2020-03-15T17:05:26.788092Z',
//  decks: [1] }, {
//  id: 3,
//  title: 'Old man on the bridge',
//  answer: 'Blue, no yeeeellllloooooowwwwww',
//  subject: 'Philosophy',
//  created_at: '2020-03-15T17:05:26.788092Z',
//  decks: [1] }],
//  name: 'Monty Python Quiz',
//  created_at: '2020-03-15T17:05:26.799462Z'
//  }
