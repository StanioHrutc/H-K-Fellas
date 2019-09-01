document.querySelector('#main-form').addEventListener('submit', function (e) {
	e.preventDefault()
	console.log(e.target.elements.firstName.value)
	e.target.elements.firstName.value = ''
})