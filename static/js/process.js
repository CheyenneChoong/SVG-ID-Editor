async function automaticId() {
    response = await fetch('/automatic');
    data = await response.json()
    document.getElementById("preview").innerHTML = data.svg;
    document.getElementById("automatic-button").disabled = true;
    document.getElementById("manual-button").disabled = true;
    document.getElementById("automatic-button").style.backgroundColor = "#131898";
    document.getElementById("manual-button").style.backgroundColor = "#6F74F7";
    await fetch('/updateMode?key=id-mode&value=automatic');
    idList();
}

async function manualId() {
    fileUpload = document.getElementById("manual-upload").files[0];
    formData = new FormData();
    formData.append("manual-file", fileUpload);
    response = await fetch('/manual', {
        method: "POST",
        body: formData
    });
    data = await response.json();
    document.getElementById("preview").innerHTML = data.svg;
    document.getElementById("automatic-button").disabled = true;
    document.getElementById("manual-button").disabled = true;
    document.getElementById("manual-button").style.backgroundColor = "#131898";
    document.getElementById("automatic-button").style.backgroundColor = "#6F74F7";
    await fetch('updateMode?key=id-mode&value=manual');
    idList();
}

async function reset() {
    response = await fetch('/reset');
    data = await response.json();
    document.getElementById("preview").innerHTML = data.svg;
    document.getElementById("manual-button").disabled = false;
    document.getElementById("manual-button").style.backgroundColor = "#6F74F7";
    document.getElementById("automatic-button").disabled = false;
    document.getElementById("automatic-button").style.backgroundColor = "#6F74F7";
    await fetch('/updateMode?key=id-mode&value=None');
    idList();
}

async function download() {
    await fetch('/download', {method: "POST"})
        .then(response => response.blob())
        .then(blob => {
            const url = URL.createObjectURL(blob);
            const link = document.createElement("a");
            link.href = url;
            link.download = "output.svg";
            link.click();
            URL.revokeObjectURL(url);
        });
}

async function idList() {
    response = await fetch('/idList');
    data = await response.json();
    text = "";
    for (const idData of data.idList) {
        text = text + `
        <div class='id-card' id='card-${idData[0]}'>
            <input type='text' id='id-${idData[0]}' value='${idData[0]}' />
            <div class='colour-row'>
                <label>Fill</label>
                <input type='text' id='fill-${idData[0]}' value='${idData[1]}' />
            </div>
            <div class='colour-row'>
                <label>Stroke</label>
                <input type='text' id='stroke-${idData[0]}' value='${idData[2]}' />
            </div>
            <div class='id-button'>
                <button onclick='saveId("${idData[0]}");'><img src='/static/assets/save.png' alt='Save' /></button>
                <button onclick='deleteId("${idData[0]}");'><img src='/static/assets/delete.png' alt='Delete' /></button>
            </div>
        </div>
        `;
    }
    document.getElementById("id-list").innerHTML = text;
}

async function saveId(id) {
    newId = document.getElementById(`id-${id}`).value;
    fill = document.getElementById(`fill-${id}`).value;
    stroke = document.getElementById(`stroke-${id}`).value;
    response = await fetch(`/saveChange?newId=${encodeURIComponent(newId)}&id=${encodeURIComponent(id)}&fill=${encodeURIComponent(fill)}&stroke=${encodeURIComponent(stroke)}`);
    data = await response.json();
    document.getElementById("preview").innerHTML = data.svg;
    idList();
}

async function deleteId(id) {
    response = await fetch(`/deleteId?id=${encodeURIComponent(id)}`);
    data = await response.json();
    document.getElementById("preview").innerHTML = data.svg;
    idList();
}

async function testMode() {
    testButton = document.getElementById("test-button");
    await fetch('/updateTest');
    openFile();
}
