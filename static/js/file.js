async function projects() {
    let response = await fetch('/projectList');
    let data = await response.json();
    let projectList = data.project;
    text = `<button onclick="document.getElementById('open-project').style.display='none';">X</button>
    <table><tr>
    <th style='width: auto'>Project Title</th>
    <th style='width: 200px;'>Date Created</th>
    <th style='width: 200px;'>Last Accessed</th>
    <th style='width: 20px;'></th></tr>`; 
    for (const project of projectList) {
        text = text + `<tr>
        <td><button onclick='openProject("${project[0]}");'>${project[1]["title"]}</button></td>
        <td>${project[1]["date-created"]}</td>
        <td>${project[1]["last-accessed"]}</td>
        <td><button onclick='deleteProject("${project[0]}");'><img src='/static/assets/delete.png' alt='Delete' style='width:15px;' /></button></td>
        </tr>`;
    }
    text = text + "</table>";

    document.getElementById("open-project-content").innerHTML = text;
    document.getElementById("open-project").style.display = "flex";
    document.getElementById("project").style.display = "none";
    document.getElementById("center").style.display = "none";
    document.getElementById("right").style.display = "none";
}

async function deleteProject(projectId) {
    await fetch('/delete?projectId=' + projectId);
    projects();
}
