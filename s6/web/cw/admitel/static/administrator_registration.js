$('#register').on('click', (e) => {
    let inputs = $('.form-admin')
    let valid = true;
    inputs.each(function (i) {
        if ($(this).val() === '') {
            $(this).addClass('is-invalid')
            valid = false
        } else {
            $(this).removeClass('is-invalid')
        }
    })
    if (!valid) {
        e.preventDefault()
    }
})