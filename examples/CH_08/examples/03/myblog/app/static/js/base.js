$(document).ready(function () {
    let localStorage = window.localStorage;

    // get the href of the menu navbar link clicked
    $('.navbar-nav a.nav-link').click(function () {
        localStorage.setItem('active_navbar_link', $(this).get(0).href);
    });
    // clear the current active menu item
    $('.navbar-nav li.active').removeClass('active');

    // make the active navbar item active
    $('.navbar-nav a.nav-link').each(function () {
        if (this.href == localStorage.getItem('active_navbar_link')) {
            $(this).addClass('active');
            return false;
        }
    });
});