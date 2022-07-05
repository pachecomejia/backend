function get_clientes(){
    var query = window.location.search.substring(1);
    

    console.log("Query: " + query)
    //conectar el bakent
    var request = new XMLHttpRequest();
    

    request.open("GET","https://8000-pachecomejia-backend-0lv4cfaix24.ws-us51.gitpod.io/user/",true);
    request.setRequestHeader("Accept","application/json");
    
    request.setRequestHeader("Authorization","Basic " +btoa("user" + ":" + "user"));
    request.setRequestHeader("Content-Type", "application/json");

    const  tabla   = document.getElementById("tabla_clientes");
    const  thead   = document.getElementById("thead_clientes");

    request.onload = () =>{
        const response = request.responseText;
        const json = JSON.parse(response);

        console.log("Response: "+response);
        console.log("JSON: "+typeof json);
        var tbody = document.getElementById("tbody_clientes");


        
        for(let row=0; row<json.length; row++){
            var tr = document.createElement("tr");
            var tr_id_cliente       = document.createElement("td");
            var tr_nombre           = document.createElement("td");
            var tr_email            = document.createElement("td");
            var tr_numero           = document.createElement("td");


            tr_id_cliente.innerHTML     = json[row].id_cliente;
            tr_nombre.innerHTML         = json[row].nombre;
            tr_email.innerHTML          = json[row].email;
            tr_numero.innerHTML         = json[row].numero;
           
            tr.appendChild(tr_id_cliente);
            tr.appendChild(tr_nombre);
            tr.appendChild(tr_email);
            tr.appendChild(tr_numero);

            tbody.appendChild(tr);


        }
        tabla.appendChild(tbody);
    };
    request.send();

};