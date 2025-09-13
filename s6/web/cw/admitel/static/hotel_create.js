let hotelNameInvalid = $('#hotel-name').hasClass('is-invalid')

$('#continue').on('click', (e) => {
    let hotelName = $('#hotel-name').val().trim()
    if (hotelName === '') {
        $('#hotel-name').addClass('is-invalid')
    } else if (!hotelNameInvalid) {
        $('#hotel-name').removeClass('is-invalid')
    }
})

function preventCollapse(e) {
    let hotelName = $('#hotel-name').val().trim()
    if (hotelName === '') {
        e.preventDefault()
    }
}

$('#multi-collapse-3').on('hide.bs.collapse', preventCollapse)
$('#multi-collapse-4').on('show.bs.collapse', preventCollapse)
$('#multi-collapse-5').on('show.bs.collapse', preventCollapse)

$('#register').on('click', (e) => {
    let inputs = $('.form-hotel')
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