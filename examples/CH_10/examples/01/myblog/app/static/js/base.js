var option = {
    animation: true,
    delay: 3000
}
var toastElements = [].slice.call(document.querySelectorAll('.toast'))
var toasts = toastElements.map(function (toastElement) {
    return new bootstrap.Toast(toastElement, option)
})
toasts.forEach(toast => toast.show())
