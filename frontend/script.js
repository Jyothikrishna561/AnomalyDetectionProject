async function checkAnomaly() {
    
    let login_hour = document.getElementById("login_hour").value;
    let amount = document.getElementById("amount").value;
    let duration = document.getElementById("duration").value;

    let response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            login_hour: parseInt(login_hour),
            transaction_amount: parseFloat(amount),
            session_duration: parseFloat(duration)
        })
    });

    let data = await response.json();
    console.log(data);

    let result = document.getElementById("result");

    if (data.anomaly === -1) {
        result.innerHTML = "⚠️ Anomaly Detected!";
    } else {
        result.innerHTML = "✅ Normal Behavior";
    }
}
async function uploadCSV() {

    let fileInput = document.getElementById("fileInput");
    let file = fileInput.files[0];

    if (!file) {
        alert("Please select a file!");
        return;
    }

    let formData = new FormData();
    formData.append("file", file);

    let response = await fetch("http://127.0.0.1:8000/upload-csv", {
        method: "POST",
        body: formData
    });

    let data = await response.json();

    console.log(data);

    if (!data.results) {
        alert("Error: " + JSON.stringify(data));
        return;
    }

    let tableDiv = document.getElementById("tableResult");

    let html = "<table border='1'><tr><th>Login Hour</th><th>Amount</th><th>Duration</th><th>Anomaly</th></tr>";

    data.results.forEach(row => {
        html += `<tr>
                    <td>${row.login_hour}</td>
                    <td>${row.transaction_amount}</td>
                    <td>${row.session_duration}</td>
                    <td>${row.anomaly == -1 
? "<span style='color:red;'>⚠️ Anomaly</span>" 
: "<span style='color:green;'>✅ Normal</span>"}</td>
                 </tr>`;
    });

    html += "</table>";

    tableDiv.innerHTML = html;
}