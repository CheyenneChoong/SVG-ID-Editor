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
            if (fileList[file]["id-mode"] == "Manual") {
                document.getElementById("automatic-button").disabled = true;
                document.getElementById("manual-button").disabled = false;
                document.getElementById("manual-button").style.backgroundColor = "#131898";
            } else if(fileList[file]["id-mode"] == "Automatic") {
                document.getElementById("manual-button").disabled = true;
                document.getElementById("automatic-button").disabled = false;
                document.getElementById("automatic-button").style.backgroundColor = "#131898";
            }
        } else {
            color = "#D2FFFD";
        }
        fileListText = fileListText + `
        <div class='file-row' onclick='' style='background-color: ${color}'>
        <input type='text' id='name-${file}' value='${fileList[file]['name']}' />
        <button onclick=''><img src='/static/assets/delete.png' alt='Delete' style='width:15px;' /></button>
        </div>
        `;
    }
    document.getElementById("project-files").innerHTML = fileListText;

    document.getElementById("project").style.display = "flex";
    document.getElementById("open-project").style.display = "none";
}

async function openFile(fileId) {
    return
}

async function uploadFile() {
    input = document.getElementById("file-upload");
    formData = new FormData();
    formData.append("upload-svg", input.files[0]);

    let response = await fetch('/upload-file', {
        method: 'POST',
        body: formData
    });
    let data = await response.json();

    current = document.getElementById("project-files").innerHTML;
    updated = current.replace("#C4E3FF", "#D2FFFD");
    updated = updated + `
    <div class='file-row' onclick='' style='background-color: #C4E3FF'>
    <input type='text' id='name-${data.fileId}' value='${data.name}' />
    <button onclick=''><img src='/static/assets/delete.png' alt='Delete' style='width:15px;' /></button>
    </div>
    `;
    document.getElementById("project-files").innerHTML = updated;
}

