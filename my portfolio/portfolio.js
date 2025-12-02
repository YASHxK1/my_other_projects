// Create data visualization grid
const dataViz = document.getElementById('dataViz');
const rows = 36;
const cols = 36;

// Create grid
for (let i = 0; i < rows; i++) {
    const row = document.createElement('div');
    row.className = 'data-row';
    
    for (let j = 0; j < cols; j++) {
        const cell = document.createElement('div');
        cell.className = 'data-cell';
        row.appendChild(cell);
    }
    
    dataViz.appendChild(row);
}

// Animate grid
function animateGrid() {
    const cells = document.querySelectorAll('.data-cell');
    cells.forEach(cell => {
        if (Math.random() > 0.9) {
            cell.classList.add('active');
        } else {
            cell.classList.remove('active');
        }
    });
    
    setTimeout(animateGrid, 1000);
}

// Start animations when page loads
window.addEventListener('load', () => {
    animateGrid();
});

// Navigation bar visibility logic - only visible on home section
window.addEventListener('scroll', function() {
    const nav = document.querySelector('nav');
    const homeSection = document.getElementById('home');
    const homeSectionBottom = homeSection.offsetTop + homeSection.offsetHeight;
    
    if (window.pageYOffset > homeSectionBottom) {
        nav.style.display = 'none';
    } else {
        nav.style.display = 'block';
    }
});
//typying animation
        document.addEventListener('DOMContentLoaded', function() {
    const text = "> Hello world";
    const typedTextElement = document.getElementById('typed-text');
    let charIndex = 0;
    
    function typeText() {
        if (charIndex < text.length) {
            typedTextElement.textContent += text.charAt(charIndex);
            charIndex++;
            setTimeout(typeText, 100); // Adjust typing speed here (milliseconds)
        }
    }
    
    // Start typing animation
    typeText();
});
