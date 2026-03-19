// TOGGLE PROFILE DROPDOWN
function toggleProfile(){
    const menu = document.getElementById("profileDropdown");
    menu.style.display = menu.style.display === "flex" ? "none" : "flex";
}

// CLOSE WHEN CLICKING OUTSIDE
window.addEventListener("click", function(e){
    const menu = document.getElementById("profileDropdown");
    const icon = document.querySelector(".profile-icon");

    if (icon && menu && !icon.contains(e.target) && !menu.contains(e.target)){
        menu.style.display = "none";
    }
});

// PROFILE IMAGE UPLOAD (AJAX)
document.addEventListener("DOMContentLoaded", function(){

    const input = document.getElementById("profileInput");

    if(input){
        input.addEventListener("change", function(){

            let form = document.getElementById("profileForm");
            let formData = new FormData(form);

            fetch("/accounts/profile/", {   // ⚠️ IMPORTANT (no Django template here)
                method: "POST",
                headers: {
                    "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value
                },
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if(data.image_url){
                    document.querySelector(".profile-icon img").src = data.image_url;
                }
            });

        });
    }

});