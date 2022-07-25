function add_use(){

    var nombre      = document.getElementById("nombre");
    var email       = document.getElementById("email");
    var numero      = document.getElementById("numero");

    var payload ={
       
        "nombre": nombre.value,
        "email": email.value,
        "numero": numero.value     
    }
  
    console.log("nombre: " + nombre.value);
    console.log("email: " + email.value);
    console.log("numero: " + numero.value);

    var request = new XMLHttpRequest();
    request.open("POST","https://8000-pachecomejia-backend-0lv4cfaix24.ws-us53.gitpod.io/cliente/",true);
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