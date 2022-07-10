function putClientes(){
    var id_cliente = window.location.search.substring(1);
    console.log("id_cliente: " +id_cliente);
    var id_cliente = document.getElementById("id_cliente");
    var nombre = document.getElementById("nombre");
    var email = document.getElementById("email");
    var numero = document.getElementById("numero");
    var payload ={
        "id_cliente": id_cliente.value,
        "nombre": nombre.value,
        "email": email.value,
        "numero": numero.value 

    }
    
    var request = new XMLHttpRequest();
    request.open("PUT","https://8000-pachecomejia-backend-0lv4cfaix24.ws-us53.gitpod.io/clientes/",true);
    request.setRequestHeader("Content-Type","application/json");
    request.setRequestHeader("Accept","application/json");
    request.setRequestHeader("Authorization","Basic " +btoa("user" + ":" + "user"));
    

    request.onload = () =>{
        const response = request.responseText;
        const json = JSON.parse(response);
        const status = request.status;


        console.log("Response: " + response);
        console.log("JSON: " + json);
        console.log("Status: " + status);

        if(status == 200){
            alert(json.message);
            window.location.replace("/get_clientes.html");
        }
    

    };
    
    request.send(JSON.stringify(payload));

};