$(function () {
    let $titles = $('#list_movies')
    $.ajax({
        type: 'GET',
        url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
        success: function (titles) {
            var i = 0
            $.each(titles, function (idx, title) {
                $titles.append('<li> title :' + titles.results[i].title + '.</li>');
                i += 1;
            });
        }
    });
});