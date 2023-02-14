


clickRut = () => {

    
    const input1 = document.querySelector("#rut-input").value;

    if (!input1) {
        alert("Por favor, rellene todos los campos");
        return;
    }else{

    $.ajax({
       url: "/buscar_rut/",
       type: "POST",
       data:  { rut: input1 },
       success: function(response) {
        if (response.Nombre){
          alert("Hola Eres Fonoaudilogo") 
          $('#rutvalidate').hide();
          $('#formulario').show();
          let rut = document.querySelector("#id_rut");
          let nombre = document.querySelector("#id_nombre");
          let apellido = document.querySelector("#id_apellido")
          let tipo_user = document.querySelector("#id_tipo_user");

          
          let FullName = response.Nombre
          FullName = FullName.split(" ")
          rut.value = response.rut
          nombre.value = FullName[0]
          apellido.value = FullName[2]
          tipo_user.value = "FonoAudilogo"
          console.log(apellido)
        }else if (response.NO){
          alert("RUT ya fue registrado/Preregistrado")  
            
        }else if (response.SI){
          alert("No tenemos Informacion del Rut, Complete el formulario de PreRegistro") 
          $('#rutvalidate').hide();
          $('#formulario').show();

        }



       }
     });

}
}

//agrega . y - a el Rut
 const rutInput = document.querySelector("#rut-input");

  rutInput.addEventListener("input", function() {
    let rut = this.value;
    rut = rut.replace(/[^0-9kK]+/g, "");

    if (rut.length > 1) {
      rut = rut.slice(0, rut.length - 1) + "-" + rut.slice(rut.length - 1);
    }

    if (rut.length > 4) {
      rut = rut.slice(0, -5) + "." + rut.slice(-5);
    }

    if (rut.length > 8) {
      rut = rut.slice(0, -9) + "." + rut.slice(-9);
    }

    this.value = rut;
  });


