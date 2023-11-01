$(function () {
    let $names = $('#character')
    $.ajax({
        type: 'GET',
        url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
        success: function (names) {
            $names.append('<p>name :' + names.name + '.</p>');
        }
    });
});