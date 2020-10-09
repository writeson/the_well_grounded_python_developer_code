window.addEventListener('load', function (event) {
    let banner = document.querySelector("#header h1");
    let colors = [
        'darkcyan',
        'cyan',
        'aqua',
        'cadetblue',
        'red',
        'lightblue'
    ];

    window.addEventListener('click', function (event) {
        // is this the click even we're looking for?
        if (event.target.matches('.change-banner-color')) {
            let color = colors[Math.floor(Math.random() * colors.length)];
            banner.style.backgroundColor = color;
        }
    })
});
