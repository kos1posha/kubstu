function usernameInvalidFeedback(me, feedbackTextId) {
    let feedback = document.getElementById(feedbackTextId)
    feedback.hidden = /^[a-zA-Zа-яА-Я0-9-_]*$/.test(me.value) || me.value.length === 0
}

function passwordInvalidFeedback(me, feedbackTextId) {
    let feedback = document.getElementById(feedbackTextId)
    feedback.hidden = (!/^[0-9]+$/.test(me.value) && me.value.length > 7) || me.value.length === 0
}

function password2InvalidFeedback(me, otherID, feedbackTextId) {
    let feedback = document.getElementById(feedbackTextId)
    let password = document.getElementById(otherID)
    feedback.hidden = me.value === password.value
}

function passwordShowHide(me, passwordID) {
    let password = document.getElementById(passwordID)

    if (password.type === "password") {
        password.type = "text"
        me.value = "👁️"
    } else {
        password.type = "password"
        me.value = "—"
    }

    password.focus()
}

function forgotPassword() {
    let alertContent = "Надо было записывать"
    let alertTitle = "Нам все равно"

    halfmoon.initStickyAlert({
        content: alertContent,
        title: alertTitle,
        alertType: "",
        fillType: "",
        hasDismissButton: true,
        timeShown: 4000
    })
}

function profileTabSwitch(activeTab) {
    let tabs = [
        document.getElementById("profile-info"),
        document.getElementById("profile-keys")
    ]
    let tabsContent = [
        document.getElementById("profile-info-content"),
        document.getElementById("profile-keys-content")
    ]

    for (let i = 0; i < tabs.length; i++) {
        let isActive = activeTab === i + 1
        tabsContent[i].hidden = !isActive
        if (isActive) {
            tabs[i].classList.add("hyperlink-underline")
            tabs[i].classList.remove("hyperlink")
            tabs[i].classList.remove("text-light-dm")
            tabs[i].classList.remove("text-dark-lm")
        } else {
            tabs[i].classList.add("hyperlink")
            tabs[i].classList.add("text-light-dm")
            tabs[i].classList.add("text-dark-lm")
            tabs[i].classList.remove("hyperlink-underline")
        }
    }
}

function profileEdit() {
    document.getElementById("edit").toggleAttribute("disabled")
    document.getElementById("cancel").toggleAttribute("disabled")
    document.getElementById("save").toggleAttribute("disabled")

    document.getElementById("first-name").toggleAttribute("readonly")
    document.getElementById("last-name").toggleAttribute("readonly")
    document.getElementById("group-code").toggleAttribute("readonly")
    document.getElementById("email").toggleAttribute("readonly")
}

function profileCancel(old_first_name, old_last_name, old_group_code, old_email) {
    profileEdit()

    document.getElementById("first-name").value = old_first_name
    document.getElementById("last-name").value = old_last_name
    document.getElementById("group-code").value = old_group_code
    document.getElementById("email").value = old_email
}

