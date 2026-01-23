const jokeElement = document.getElementById("pyjoke").getElementsByTagName("code")[0];

function displayRandomJoke() {
  const randomIndex = Math.floor(Math.random() * jokes.length);
  jokeElement.textContent = jokes[randomIndex];
};

displayRandomJoke();

setInterval(displayRandomJoke, 10000);