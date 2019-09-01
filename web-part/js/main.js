const drawBorder = function (errorField, inputTag) {
	if (errorField.innerText == '') {
		inputTag.style.borderBottom = '3px solid #87C540';
	}	else {
		inputTag.style.borderBottom = '3px solid #d9534f';
	}
}

const validateEmail = function (email) {
	return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)
}



const isNumberIn = function (userInputTag, errorField, message) {
	numberCounter = 0;

	for (let i = 0; i < userInputTag.length; i++) {
		if (userInputTag[i] >= '0' && userInputTag[i] <= '9') {
			numberCounter++;
   			errorField.innerText = message;
		}
	}

	if (numberCounter >= 1) {
		return true
	}	else if (numberCounter == userInputTag.length) {
		return 'This is a number'
	}

	return false
}


const validators = {
	name: function (nameTag) {
		let msg = 'Name length must contain 4 chars | Name can not contain any number';

		let errorNameField = document.getElementById('error-name');

		nameTag.oninput = function () {
			if (nameTag.value.length < 4 || isNumberIn(nameTag.value, errorNameField, msg)) {
				errorNameField.innerText = msg;
			}	else {
				errorNameField.innerText = '';
			}			

		};

		nameTag.onchange = function () {
			// checks error after unfocusing of input field and draws related border
			drawBorder(errorNameField, nameTag)
		}	

	},

	username: function (usernameTag) {
		let msg = 'User name length must contain at least 4 chars';

		let errorUserNameField = document.getElementById('error-username');

		usernameTag.oninput = function () {
			if (usernameTag.value.length < 4) {
				errorUserNameField.innerText = msg;
			}	else {
				errorUserNameField.innerText = '';
			}			

		};

		usernameTag.onchange = function () {
			// checks error after unfocusing of input field and draws related border
			drawBorder(errorUserNameField, usernameTag)
		}
	},

	email: function (emailTag) {
		let msg = 'Incorrect email';

		let errorEmailField = document.getElementById('error-email');

		emailTag.oninput = function () {
			if (validateEmail(emailTag.value)) {
				errorEmailField.innerText = '';
			}	else {
				errorEmailField.innerText = msg;
			}

		};

		emailTag.onchange = function () {
			// checks error after unfocusing of input field and draws related border
			drawBorder(errorEmailField, emailTag)
		}	

	},

	password: function (passwordTag, confirmTag) {
		let msg = 'Password must contain at least 6 chars and at least 1 number';

		let errorPasswordField = document.getElementById('error-password');
		let errorConfirmField  = document.getElementById('error-confirm');

		passwordTag.oninput = function () {
			if (passwordTag.value.length >= 6 && isNumberIn(passwordTag.value, errorPasswordField, msg)) {
				errorPasswordField.innerText = '';
				areFieldsEqual(passwordTag, confirmTag, errorConfirmField)
			}	else {
				errorPasswordField.innerText = msg;
			}

		};

		passwordTag.onchange = function () {
			// checks error after unfocusing of input field and draws related border
			drawBorder(errorPasswordField, passwordTag)
		}
	},

	confirm: function (passwordTag, confirmTag) {
		let msg = 'Passwords do not match';

		let errorConfirmField = document.getElementById('error-confirm');
		

		confirmTag.oninput = function () {
			if (passwordTag.value == confirmTag.value) {
				errorConfirmField.innerText = '';
				drawBorder(errorConfirmField, confirmTag)
			}	else {
				errorConfirmField.innerText = 'Fields are not equal';
				drawBorder(errorConfirmField, confirmTag)
			}
		}


		//confirmTag.onchange = function () {
			// checks error after unfocusing of input field and draws related border
			//drawBorder(errorConfirmField, confirmTag)
		//}

	}

};

const areFieldsEqual = function (firstTag, secondTag, errorField) {
	if (firstTag.value == secondTag.value) {
		errorField.innerText = '';
	}	else {
		errorField.innerText = 'Fields are not equal';
	}
}

const checkRightInput = function () {
	let correctNotes   = 0;
	let nonEmptyFields = 0;

	let errorFields = document.getElementsByClassName('error-msg');
	let inputFields = document.getElementsByClassName('input');



	Array.from(errorFields).forEach(function (note) {
		if (note.innerText == '') {
			correctNotes++;
			console.log('Correct notes: ' + correctNotes);
		}
	})

	Array.from(inputFields).forEach(function (input) {
    	if (input.value != '') {
           	nonEmptyFields++;
        	console.log(nonEmptyFields)
    	}
    })

	if (correctNotes == 5 && correctNotes == nonEmptyFields) {
    	document.getElementById('register').disabled = false;
    }	else {
    	correctNotes = 0;
    	nonEmptyFields = 0;
    	document.getElementById('register').disabled = true;
    }	


}


window.addEventListener('input', function () {
	checkRightInput()
	validators.name(document.getElementById('input-name'))
	validators.username(document.getElementById('input-username'))
	validators.email(document.getElementById('input-email'))
	validators.password(document.getElementById('input-password'), document.getElementById('input-confirm'))
	validators.confirm(document.getElementById('input-password'), document.getElementById('input-confirm'))
}, false);



