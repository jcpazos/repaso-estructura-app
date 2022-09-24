function pressButton() {
    window.alert("Apretaste el boton!");
    /*const url = "https://www.google.com/";
    
    fetch(url).then((response) => {
        console.log(response);
    });

    fetch(url).then(function(response) {
        console.log(response);
    });

    const body = {"prop1": "value1", "prop2": "value2"};
    
    fetch(url, {
        "method": "POST",
        "body": JSON.stringify(body),
        "headers": {
            "Content-Type": "application/json"
        }
    }).then((response) => {
        console.log(response);
    })*/

    const url = "http://localhost:5000/login/";

    const url2 = "http://localhost:5000/users/";

    const body = {"username": "lhidalgo"};

    fetch(url, {
        "method": "POST",
        "body": JSON.stringify(body),
        "headers": {
            "Content-Type": "application/json"
        }
    }).then((response) => response.json())
    .then((data) => console.log(data));

    fetch(url2).then((response) => response.json())
    .then((data) => {
        let resultado = "";
        data.forEach((item) => {
            resultado+= "Usuario: " + item.username + " Email: " + item.email + "<br>";
        });

        document.getElementById("divresultado").innerHTML = resultado;
    });

}

function miFuncion() {

}

let funcion = (param1) => {
    console.log(param1);
}