function deleteClientes(){
    var id_cliente = window.location.search.substring(1);
    console.log("id_cliente: " +id_cliente);
    var id_cliente = document.getElementById("id_cliente");

   
    var payload ={
        "id_cliente": id_cliente.value,
  
    }
    
    var request = new XMLHttpRequest();
    request.open("DELETE","https://8000-pachecomejia-backend-0lv4cfaix24.ws-us53.gitpod.io/delete/"+ id_cliente,true);
    request.setRequestHeader("Content-Type","application/json");
    request.setRequestHeader("Accept","application/json");
    request.setRequestHeader("Authorization","Basic " + btoa("user" + ":" + "user"));
    

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