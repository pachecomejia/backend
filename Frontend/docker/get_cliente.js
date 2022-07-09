function getClientes(){
    var id_cliente = window.location.search.substring(1);
    console.log("id_cliente: " +id_cliente);
    var request = new XMLHttpRequest();



    request.open("GET","https://8000-pachecomejia-backend-0lv4cfaix24.ws-us53.gitpod.io/cliente/"+id_cliente,true);
    request.setRequestHeader("Accept","application/json");

    request.onload = () =>{
        const response = request.responseText;
        const json = JSON.parse(response);

        console.log("Response: " + response);
        console.log("JSON: " + json);

        let nombre  = document.getElementById("nombre");
        let email   = document.getElementById("email");
        let numero = document.getElementById("numero");
        

        nombre.value = json.nombre;
        email.value = json.email;
        numero.value = json.numero;
       

    };


    request.send();

};