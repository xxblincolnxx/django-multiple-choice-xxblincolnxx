/* globals fetch, location */
// -----------------------HELPER FUNCTIONS---------------------
function dQS (elementID) {
  return document.querySelector(elementID)
}

function dQSA (elementClass) {
  return document.querySelectorAll(elementClass)
}

function hide (element) {
  element.classList.add('dn')
}

function show (element) {
  element.classList.remove('dn')
}

// -------------------BASIC HIDE AND SHOW--------------------

function pageFormButtons () {
  const buttons = dQSA('.col-butt')
  for (const button of buttons) {
    button.addEventListener('click', function (event) {
      const formQuery = event.target.dataset.form
      const forms = dQSA('.col-form')
      for (const form of forms) {
        if (form.id === formQuery && form.classList.contains('dn')) {
          show(form)
        } else {
          hide(form)
        }
      }
    })
  }
}

function showColumn () {
  const headers = dQSA('.col-heading')
  for (const header of headers) {
    header.addEventListener('click', function (event) {
      console.log(`you clicked ${event.target.dataset.stuff}`)
      const contentQuery = event.target.dataset.stuff
      const containers = dQSA('.col-container')
      for (const container of containers) {
        if (container.id === contentQuery && container.classList.contains('dn')) {
          show(container)
        } else {
          hide(container)
        }
      }
    })
  }
}
// ---------------------FORM SUBMITTERS------------------
function formListener (form) {
  form.addEventListener('submit', function (event) {
    console.log(event.target.id)
    event.preventDefault()
    if (form.id === 'text-card-create') {
      fetch('http://localhost:8000/api/text-card/', {
        method: 'POST',
        headers: {
          contentType: 'application/json'
        },
        body: JSON.stringify({
          title: event.target.id_title.value,
          subject: event.target.id_subject.value,
          question: event.target.id_question.value,
          answer: event.target.id_answer.value
        })
      })
        .then(res => res.json())
        .then(json => {
          location.reload()
        })
    }
    if (form.id === 'figure-card-create') {
      fetch('http://localhost:8000/api/figure-card/', {
        method: 'POST',
        headers: {
          contentType: 'application/json'
        },
        body: JSON.stringify({
          title: event.target.id_title.value,
          subject: event.target.id_subject.value,
          raw_image: event.target.id_raw_image.value,
          answer: event.target.id_answer.value
        })
      })
        .then(res => res.json())
        .then(json => {
          location.reload()
        })
    }
  })
}

// ----------------------RUN PAGE---------------------
function pageRun () {
  const textCardForm = dQS('#text-card-create')
  const figureCardForm = dQS('#figure-card-create')
  pageFormButtons()
  showColumn()
  formListener(textCardForm)
  formListener(figureCardForm)
}

pageRun()
