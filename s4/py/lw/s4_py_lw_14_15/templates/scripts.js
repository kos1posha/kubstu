function showHide(field) {
    let isSlice = field === 'View slice' || field === 'Delete slice'
    let isId = field === 'View id' || field === 'Delete id' || field === 'Update'

    document.getElementById('id_block').style.display = isId ? 'block' : 'none'
    document.getElementById('start_block').style.display = isSlice ? 'block' : 'none'
    document.getElementById('end_block').style.display = isSlice ? 'block' : 'none'

    document.getElementById('id').required = isId
    document.getElementById('start').required = isSlice
    document.getElementById('end').required = isSlice
}
