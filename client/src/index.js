function pressButton() {
    window.alert("Apretaste el boton!");
    const url = "https://www.google.com/";
    fetch(url).then((response) => {
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
    })
}