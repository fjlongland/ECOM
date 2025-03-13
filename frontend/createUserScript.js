document.getElementById("btnSubmit").addEventListener('click', async function(event){
    event.preventDefault();

    const new_username = document.getElementById("txtUsername").value;
    const new_password = document.getElementById("txtPassword").value;

    console.log("Username: "+new_username+"\tPassword: "+new_password);

    const feedback = "Username: "+new_username+"\nPassword: "+new_password;

    document.getElementById("txtFeedback").textContent = feedback;

    try{
        const formdata = new URLSearchParams()
        formdata.append("user_name", new_username);
        formdata.append("user_password", new_password);

        const response = await fetch("http://127.0.0.1:8000/users", {
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
            console.log(data.user_id)
            alert("user ("+data.user_id+") was created successfuly!")
        }
    }
    catch(error){
        console.error("there was an error creating user: ", error);
        alert("an error occured while trying to create user :(");
        return null;
    }


});