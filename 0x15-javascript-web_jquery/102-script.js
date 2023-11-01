$(document).ready(function () {
    const url = 'https://www.fourtonfish.com/hellosalut/hello/'
    $('#btn_translate').click(function () {
        const lan = $('#language_code').val();
        $.get(url + $.param({ lan }), function (data) {
            $('#hello').html(data.hello);
        });
    });
});