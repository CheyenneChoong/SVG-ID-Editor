async function automaticId() {
    response = await fetch('/automatic');
    data = await response.json()
    document.getElementById("preview").innerHTML = data.svg;
    document.getElementById("automatic-button").disabled = true;
    document.getElementById("manual-button").disabled = true;
    document.getElementById("automatic-button").style.backgroundColor = "#131898";
    await fetch('/updateMode?key=id-mode&value=automatic');
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