function CambiarMayusculas(objeto_input)
{
    
    objeto_input.value = objeto_input.value.toUpperCase();
    
}


//validar registro
$(function() 
{
  $("#registro").validate({
       rules: {
            nombre: "required",
     
            apellido: "required",
            correo: {
                required: true,
                email: true
            },
            contrasena: "required",
            fono: "required",
            contrasena2: {
                required: true,
                equalTo: "#contrasena"
            }   
              
        }, 
      messages: {
          nombre: {
              required: 'Ingresa un nombre valido'
          },
          apellido: {
              required: 'Ingresa un apellido valido'
          },
          correo: {
              required: 'Ingresa tu correo electrónico',
              email: 'Formato de correo no válido'
          },
          contrasena: {
              required: 'Ingresa una contraseña',
              minlength: 'Caracteres insuficientes'
          },
          fono:{
              required: 'Ingrese un número de celular',
              minlength: 'Cantidad de digitos insuficiente'
          },
        
          contrasena2: {
              required: 'Reingresa la contraseña',
              equalTo: 'Las contraseñas ingresadas no coinciden',
              minlength: 'Caracteres insuficientes'

          }
      }
  }); 
}); 
//validar login