document.getElementById("btnLogin").addEventListener("click", async function(){
    const username = document.getElementById("txtUsername").value;
    const password = document.getElementById("txtPassword").value;

    alert("loging in user "+username+" with password "+password);
})