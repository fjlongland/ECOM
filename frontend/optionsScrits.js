document.getElementById("btnDeleteAccount").addEventListener("click", async function () {

    const user_id = getCookie("user_id");

    console.log(user_id)

    try{
        const response = await fetch('http://127.0.0.1:8000/users/'+user_id, {
            method: "DELETE"
        });
        

        if(response.status !== 204){
            alert("could not delete user");
            return;
        }

        alert("user: ("+user_id+") was deleted successfully.");
    }
    catch(error){
        console.error("there was an error while trying to delete user:", error);
    }
    
})

function getCookie(name){
    const cookies = document.cookie.split("; ");
    for (const cookie of cookies){
        const [key, value] = cookie.split("=");
        if (key === name){
            return decodeURI(value);
        }
    }
    return null;
}