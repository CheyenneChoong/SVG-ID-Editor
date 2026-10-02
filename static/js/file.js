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
    for (const project in projectList) {
        text = text + `<tr>
        <td><button onclick='openProject(${project});'>${projectList[project]["title"]}</button></td>
        <td>${projectList[project]["date-created"]}</td>
        <td>${projectList[project]["last-accessed"]}</td>
        <td><button onclick='deleteProject("${project}");'><img src='/static/assets/delete.png' alt='Delete' style='width:15px;' /></button></td>
        </tr>`;
    }
    text = text + "</table>";
    document.getElementById("open-project-content").innerHTML = text;
    document.getElementById("open-project").style.display = "flex";
}

async function openProject(projectId) {
    let response = await fetch('/open?projectId=' + projectId);
    let data = await response.json();
    document.getElementById("project-title").innerText = data.title;

    document.getElementById("project").style.display = "flex";
}

async function deleteProject(projectId) {
    await fetch('/delete?projectId=' + projectId);
    projects();
}