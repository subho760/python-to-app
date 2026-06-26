const btn = document.getElementById('colorBtn');
const colors = ['#1abc9c', '#3498db', '#9b59b6', '#f1c40f', '#e67e22', '#2ecc71'];

btn.addEventListener('click', () => {
    const randomColor = colors[Math.floor(Math.random() * colors.length)];
    document.body.style.backgroundColor = randomColor;
});
