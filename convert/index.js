function convertToMmol() {
    const mgdl = document.getElementById('mgdl').value;
    if (mgdl === "") {
        document.getElementById('result').textContent = "Please enter a value in mg/dL.";
        return;
    }
    const mmol = (mgdl / 18).toFixed(2);
    document.getElementById('result').textContent = `${mgdl} mg/dL is equal to ${mmol} mmol/L`;
}

function convertToMgdl() {
    const mmol = document.getElementById('mmol').value;
    if (mmol === "") {
        document.getElementById('result').textContent = "Please enter a value in mmol/L.";
        return;
    }
    const mgdl = (mmol * 18).toFixed(2);
    document.getElementById('result').textContent = `${mmol} mmol/L is equal to ${mgdl} mg/dL`;
}