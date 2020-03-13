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

function pageRun () {
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

pageRun()
