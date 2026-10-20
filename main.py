from js import document, window

club_members = [
    "Pauline Chu Tan",
    "Kortneigh Maglaqui",
    "Riona Narciso",
    "Elisha Genove"
]

def check_membership(event=None):
    first = document.getElementById("first_name").value.strip()
    last = document.getElementById("last_name").value.strip()

    full_name = first + " " + last

    is_member = full_name in club_members
    messages = {
        True: f"Congratulations {full_name}! You are part of the Volleyball Varsity!",
        False: f"Sorry {full_name}, your name is not on the list"
    }

    result_box = document.getElementById("result")
    result_box.innerText = messages[is_member]
    result_box.classList.remove("d-none")

window.check_membership = check_membership