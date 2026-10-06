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
        <div class='file-row' id='${file}' onclick='selectFile("${file}");' style='background-color: ${color}'>
        <input type='text' class='file-name' id='name-${file}' value='${fileList[file]['name']}' readonly />
        <button onclick='deleteFile("${file}");'><img src='/static/assets/delete.png' alt='Delete' style='width:15px;' /></button>
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
    let response = await fetch('/getSvg');
    let data = await response.json();
    file = data.active;
    if (file == "None") {
        document.getElementById("center").style.display = "none";
        document.getElementById("right").style.display = "none";
        return;
    }

    fileList = data.data;
    if (fileList["id-mode"] == "Manual") {
        document.getElementById("automatic-button").disabled = true;
        document.getElementById("manual-button").disabled = false;
        document.getElementById("manual-button").style.backgroundColor = "#131898";
    } else if(fileList["id-mode"] == "Automatic") {
        document.getElementById("manual-button").disabled = true;
        document.getElementById("automatic-button").disabled = false;
        document.getElementById("automatic-button").style.backgroundColor = "#131898";
    }

    document.getElementById("preview").innerHTML = data.svg;
    document.getElementById("center").style.display = "block";
    document.getElementById("right").style.display = "flex";
}

async function uploadFile() {
    input = document.getElementById("file-upload");
    check = input.files[0];
    if (!check.name.includes(".svg")) {
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
    <div class='file-row' id='${data.fileId}' onclick='selectFile("${data.fileId}");' style='background-color: #C4E3FF'>
    <input type='text' input='file-name' id='name-${data.fileId}' value='${data.name}' readonly />
    <button onclick='deleteFile("${data.fileId}");'><img src='/static/assets/delete.png' alt='Delete' style='width:15px;' /></button>
    </div>
    `;
    openProject(document.getElementById("project-id").innerText);
}

async function deleteFile(fileId) {
    response = await fetch(`/deleteFile?fileId=${fileId}`);
    openProject(document.getElementById("project-id").innerText);
}

async function selectFile(fileId) {
    await fetch(`/selectFile?fileId=${fileId}`);
    openProject(document.getElementById("project-id").innerText);
}

async function renameFile(fileId) {
    await fetch(`/renameFile?fileId=${fileId}`);
    document.getElementById(`name-${fileId}`).readOnly = true;
}