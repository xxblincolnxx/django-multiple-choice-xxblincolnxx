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

// ----------------------RUN PAGE---------------------
function pageRun () {
  showColumn()
}

pageRun()
