$(function () {
    let $lang = $('#hello')
    $.ajax({
        type: 'GET',
        url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
        success: function (lang) {
            $lang.append('<p>' + lang.hello + '.</p>');
        }
    });
});