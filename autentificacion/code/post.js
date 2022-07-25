function add_user(){
   var email = document.getElementById("email").value;
   var password = document.getElementById("password").value;

    var  datos ={
        "email": email,
        "password": password,
    }
    var request = new XMLHttpRequest();


    request.open("POST","https://8000-pachecomejia-backend-0lv4cfaix24.ws-us54.gitpod.io/users/",true); 
  //request.setRequestHeader("Authorization", "Basic " + btoa(email.value,password.value));
    request.setRequestHeader("Accept", "application/json");
    request.setRequestHeader("Content-Type", "application/json");


    request.onload = ()=>{
       const status = request.status


        if (status == 202){
            alert("Usuario agregado correctamnete");
            window.location.replace("/inicio.html");

        }
        if (status == 401){
            alert("Dirreccion de correo o contraseña invalidos vuelve a intentarlo");
        }
       
        else if(status == 422){
            
            alert("Error");
        
            
        }
    };
    request.send(JSON.stringify(datos));
};