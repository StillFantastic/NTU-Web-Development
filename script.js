// Unique symbols for private members
const _colors = Symbol('colors');
const _spaceCount = Symbol('spaceCount');
const _data = Symbol('data');

// UIComponent base class for UI related methods
function UIComponent() {
  this[_data] = {
    hiddenElements: new Set()
  };
}

// Defining methods on UIComponent's prototype for inheritance
UIComponent.prototype.showOrHideElement = function(elementId, isVisible) {
  const element = document.getElementById(elementId);
  if (isVisible) {
    element.style.display = "block";
    this[_data].hiddenElements.delete(elementId);
  } else {
    element.style.display = "none";
    this[_data].hiddenElements.add(elementId);
  }
};

UIComponent.prototype.setEasterEggBackground = function() {
  document.getElementsByClassName('container')[0].style.backgroundImage = "url(./img/rick-roll.jpeg)";
  document.body.style.backgroundSize = 'cover';
};

// App object encapsulates the entire application logic
const App = (function() {
  const privateMembers = {
    [_colors]: ["red", "orange", "yellow", "green", "blue", "indigo", "purple"],
    [_spaceCount]: 0
  };

  const uiComponent = new UIComponent();

  function changeColor() {
    const randomIndex = Math.floor(Math.random() * privateMembers[_colors].length);
    document.body.style.backgroundColor = privateMembers[_colors][randomIndex];
  }

  function displayGreeting() {
    const hours = new Date().getHours();
    const greeting = hours < 12 ? "Good Morning!" : hours < 18 ? "Good Afternoon!" : "Good Evening!";
    document.getElementById("greeting").innerText = greeting;
  }

  function displayTime() {
    document.getElementById('time').textContent = new Date().toLocaleTimeString();
    setTimeout(displayTime, 1000);
  }

  function validateEmail(event) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    uiComponent.showOrHideElement('invalidEmail', !emailRegex.test(event.target.value));
  }

  function checkEasterEgg(event) {
    if (event.code === 'Space') {
      privateMembers[_spaceCount]++;
      if (privateMembers[_spaceCount] === 5) {
        uiComponent.setEasterEggBackground();
        privateMembers[_spaceCount] = 0;
      }
    }
  }

  function handleFormSubmit(event) {
    event.preventDefault();
    const fname = document.getElementById('fname').value;
    const email = document.getElementById('email').value;
    const bday = document.getElementById('bday').value;

    Swal.fire({
      icon: 'success',
      title: 'Your form has been submitted',
      text: `Name: ${fname}, Email: ${email}, Birthday: ${bday}`,
    });
  }

  function bindEvents() {
    document.getElementById('changeColorButton').addEventListener('click', changeColor);
    document.getElementById('showButton').addEventListener('click', () => uiComponent.showOrHideElement('hiddenP', true));
    document.getElementById('hideButton').addEventListener('click', () => uiComponent.showOrHideElement('hiddenP', false));
    document.getElementById('email').addEventListener('input', validateEmail);
    window.addEventListener('keydown', checkEasterEgg);
    document.querySelector('form').addEventListener('submit', handleFormSubmit);
  }

  return {
    init: function() {
      displayGreeting();
      displayTime();
      bindEvents();
    }
  };
})();

document.addEventListener('DOMContentLoaded', App.init);
