
clickpreregistrados = (a) => {
let ver = document.getElementById(a)
let elementos = ver.getElementsByTagName("td")
console.log(elementos)
// document.getElementById("id_username").value = elementos[0].innerHTML
document.getElementById("id_first_name").value = elementos[1].innerHTML
document.getElementById("id_last_name").value = elementos[2].innerHTML
document.getElementById("id_email").value = elementos[4].innerHTML
if( elementos[3].innerHTML = "Fonoaudiólogo"){
    document.getElementById("id_id_tipo_user").value = 1


}



}
