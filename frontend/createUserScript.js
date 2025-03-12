document.getElementById("btnSubmit").addEventListener('click', function(){
    const new_username = document.getElementById("txtUsername").value;
    const new_password = document.getElementById("txtPasseord").value;

    console.log("Username: "+new_username+"\tPassword: "+new_password);
});