function scrollDown() 
{
    document.getElementById('move_here').scrollIntoView({
        behavior: 'smooth'
    });
}

function reloadPage() 
{
    location.reload();
}

function goHome() 
{
    window.location.href = "/";
}

function clearSearchInput() 
{
    setTimeout(function() 
    {
        document.getElementById('searchInput').value = '';
    }, 0);
}

var searchInput = document.getElementById('searchInput');
var searchSuggestions = document.getElementById('searchSuggestions');


fetch('/api/movies')
    .then(response => response.json())
    .then(movieNamesArray => {
        searchInput.addEventListener('input', function () {
            var inputValue = this.value.trim().toLowerCase();
            var suggestions = [];
            if (inputValue.length > 0) {
                suggestions = movieNamesArray.filter(function (movie) {
                    return movie.toLowerCase().includes(inputValue);
                });
            }
            displaySuggestions(suggestions);
        });
    })
    .catch(error => console.error('Error fetching movie names:', error));

function displaySuggestions(suggestions) {
    searchSuggestions.innerHTML = '';
    suggestions.forEach(function (suggestion) {
        var li = document.createElement('li');
        li.textContent = suggestion;
        li.addEventListener('click', function () {
            searchInput.value = suggestion;
            searchSuggestions.style.display = 'none';
            document.getElementById('search').submit();
        });
        searchSuggestions.appendChild(li);
    });
    searchSuggestions.style.display = suggestions.length > 0 ? 'block' : 'none';
}

document.addEventListener('click', function (event) {
    if (!event.target.matches('#searchInput') && !event.target.matches('#searchSuggestions li')) {
        searchSuggestions.style.display = 'none';
    }
});

function showPreviousPage() 
{
    if (current_page > 1) 
    {
        current_page--;
        document.getElementById('currentPageInput').value = current_page;
        document.getElementById('paginationForm').submit();
    }
}

function showNextPage() 
{
    current_page++;
    document.getElementById('currentPageInput').value = current_page;
    document.getElementById('paginationForm').submit();
}

function submitPlayMovieForm(element) 
{
    var selectedMovie = element.textContent;
    window.location.href = '/play_movie.html?movie=' + encodeURIComponent(selectedMovie);
}

function PLAY_click_movie(element) 
{
    var selectedMovie = element.textContent;
    window.location.href = '/play_movie.html?movie=' + encodeURIComponent(selectedMovie);
}
