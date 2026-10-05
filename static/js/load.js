document.addEventListener("DOMContentLoaded", () => {
    let titleInput = document.getElementById("project-title");
    titleInput.addEventListener("dblclick", () => {
        titleInput.readOnly = false;
    });
    let typingTimer;
    titleInput.addEventListener("input", () => {
        clearTimeout(typingTimer);
        typingTimer = setTimeout(() => {
            renameProject(document.getElementById("project-id").innerText);
        }, 500);
    });

    document.addEventListener("click", (event) => {
        if (event.target != titleInput) {
            titleInput.readOnly = true;
        }
    });
});