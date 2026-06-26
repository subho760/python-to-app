const button = document.getElementById('colorBtn');
const colors = ['#121212', '#1a237e', '#004d40', '#3e2723', '#4a148c'];
let currentIndex = 0;

button.addEventListener('click', () => {
    currentIndex = (currentIndex + 1) % colors.length;
    document.body.style.backgroundColor = colors[currentIndex];
});
