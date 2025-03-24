document.getElementById("btnLogin").addEventListener('click', async function(event){
    event.preventDefault();

    const new_username = document.getElementById("txtUsername").value;
    const new_password = document.getElementById("txtPassword").value;

    try{

        //api call to log in a user
        //NOTE: the endpoint will possibly change if i add proper authentication.

        const formdata = new URLSearchParams()
        formdata.append("username", new_username);
        formdata.append("password", new_password);

        const response = await fetch("http://127.0.0.1:8000/users/login", {
            method: "POST",
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: formdata
        });

        if(!response.ok){
            const errorData = await response.json();
            console.error("Error response: ", errorData);
            throw new Error("Network response was not ok: "+ response.status);
        }

        const data = await response.json();

        if(data.user_id){
            console.log(data.user_id);
            alert("user ("+data.user_id+") was found");
            document.cookie = "user_id="+data.user_id;
            window.location.href = "homePage.html";
        }
    }
    catch(error){
        console.error("there was an error creating user: ", error);
        alert("an error occured while trying to login");
        return null;
    }
});