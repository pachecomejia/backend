function login_user(){
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;



    var request = new XMLHttpRequest();
    request.open("GET","https://8000-pachecomejia-backend-0lv4cfaix24.ws-us54.gitpod.io/users/token/",true);
    request.setRequestHeader("Authorization", "Basic " + btoa(email + ":" + password));
    request.setRequestHeader("Content-Type", "application/json");
    request.setRequestHeader("Accept","application/json");
    
    request.onload = () =>{
        const status = request.status
        JSON.parse(request.responseText);

        if (status == 202) {

            alert("Inicio Correcto");
            window.location.replace("/inicio.html");
       

            
        }
        if (status == 401){
            alert("Credenciales no validas vuelve a intentarlo");
        }
        
        if (status == 422){
            alert("ERROR de inicio desesion");
        }

    };
   request.send();
};