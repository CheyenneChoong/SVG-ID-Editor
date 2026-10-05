async function openProject(projectId) {
    let response = await fetch('/open?projectId=' + projectId);
    let data = await response.json();
    document.getElementById("project-title").value = data.title;

    active = data.active;
    fileList = data.files;

    fileListText = "";
    for (const file in fileList) {
        if (active == file) {
            color = "#C4E3FF";
        } else {
            color = "#D2FFFD";
        }
        fileListText = fileListText + `
        <div class='file-row' onclick='' style='background-color: ${color}'>
        <input type='text' id='name-${file}' value='${fileList[file]['name']}' readonly />
        <button onclick=''><img src='/static/assets/delete.png' alt='Delete' style='width:15px;' /></button>
        </div>
        `;
    }
    document.getElementById("project-files").innerHTML = fileListText;

    document.getElementById("project-id").innerText = projectId;
    document.getElementById("project").style.display = "flex";
    document.getElementById("open-project").style.display = "none";
    openFile();
}

async function openFile() {
    console.log(document.getElementById("project-id").innerText);
    let response = await fetch('/open?projectId=' + document.getElementById("project-id").innerText);
    let data = await response.json();
    file = data.active;
    fileList = data.files;
    if (fileList[file]["id-mode"] == "Manual") {
        document.getElementById("automatic-button").disabled = true;
        document.getElementById("manual-button").disabled = false;
        document.getElementById("manual-button").style.backgroundColor = "#131898";
    } else if(fileList[file]["id-mode"] == "Automatic") {
        document.getElementById("manual-button").disabled = true;
        document.getElementById("automatic-button").disabled = false;
        document.getElementById("automatic-button").style.backgroundColor = "#131898";
    }

    document.getElementById("center").style.display = "block";
    document.getElementById("right").style.display = "flex";
}

async function uploadFile() {
    input = document.getElementById("file-upload");
    if (input && input.type != "image/svg+xml") {
        return;
    }

    formData = new FormData();
    formData.append("upload-svg", input.files[0]);

    let response = await fetch('/uploadFile', {
        method: 'POST',
        body: formData
    });
    let data = await response.json();

    current = document.getElementById("project-files").innerHTML;
    updated = current.replace("#C4E3FF", "#D2FFFD");
    updated = updated + `
    <div class='file-row' onclick='' style='background-color: #C4E3FF'>
    <input type='text' id='name-${data.fileId}' value='${data.name}' readonly />
    <button onclick=''><img src='/static/assets/delete.png' alt='Delete' style='width:15px;' /></button>
    </div>
    `;
    document.getElementById("project-files").innerHTML = updated;
}

async function deleteFile(fileId) {
    response = await fetch(`/deleteFile?fileId=${fileId}`);
}