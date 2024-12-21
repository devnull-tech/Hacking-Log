const searchInput = document.getElementById('searchInput');
const searchResults = document.getElementById('searchResults');

searchInput.addEventListener('input', (event) => {
    const searchTerm = event.target.value.toLowerCase();
    const elements = searchResults.querySelectorAll('a');

    elements.forEach(element => {
        const elementText = element.textContent.toLowerCase();
        if (elementText.includes(searchTerm)) {
            element.style.display = 'block';
        } else {
            element.style.display = 'none';
        }
    });
});