document.addEventListener('DOMContentLoaded', () => {
    displayGreeting();
    displayTime();
    bindEvents();
  });
  
  function bindEvents() {
    document.getElementById('changeColorButton').addEventListener('click', changeColor);
    document.getElementById('showButton').addEventListener('click', () => showOrHideElement('hiddenP', true));
    document.getElementById('hideButton').addEventListener('click', () => showOrHideElement('hiddenP', false));
    document.getElementById('email').addEventListener('input', validateEmail);
    window.addEventListener('keydown', checkEasterEgg);
  }
  
  const colors = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"];
  let spaceCount = 0;
  
  function changeColor() {
    const randomColor = colors[Math.floor(Math.random() * colors.length)];
    document.body.style.backgroundColor = randomColor;
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
  
  function showOrHideElement(elementId, isVisible) {
    document.getElementById(elementId).style.display = isVisible ? "block" : "none";
  }
  
  function validateEmail(event) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    showOrHideElement('invalidEmail', !emailRegex.test(event.target.value));
  }
  
  function checkEasterEgg(event) {
    if (event.code === 'Space') {
      spaceCount++;
      if (spaceCount === 5) {
        document.body.style.backgroundImage = "url(./img/rick-roll.jpeg)";
        document.body.style.backgroundSize = 'cover';
        spaceCount = 0;
      }
    }
  }
  