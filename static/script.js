console.log('script is running...');
// make sure that your javascript code is between the <script> tags

// select the element with the id="time"
const paragraphElement = document.querySelector('#time');

// crerate a function that assigns the "new Date()" (the date and time) as the innerHTML of the paragraph element
const showTheTime = () => {
    paragraphElement.innerHTML = new Date();
};

// set so every 1000 ms (so every one second), the function showtheTime executes
setInterval(showTheTime, 1000);
