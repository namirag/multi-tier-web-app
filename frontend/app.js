async function loadData() {
    let response = await fetch("http://18.222.87.246:5000/products");
    let data = await response.json();

    document.getElementById("cart").innerHTML =
        data.map(x => x.name).join("<br>");
}

async function addProduct() {
    let name = document.getElementById("productName").value;

    await fetch("http://18.222.87.246:5000/products", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ name: name })
    });

    loadData();
}

window.onload = loadData;


