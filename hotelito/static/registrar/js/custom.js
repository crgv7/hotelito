const formulario=document.getElementById( 'signup-form');
const pass=document.getElementById('password')
const r_pass=document.getElementById('rpassword')


formulario.addEventListener('submit',(e) => {
    e.preventDefault();
    if (pass.value == r_pass.value){
        alert("se registro correctamente");



    }else{
        alert("las contraseñas no son igualesss");
    }




    });
