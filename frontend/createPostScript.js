document.getElementById("btnUpload").addEventListener("click", async function(){
    const newTitle = document.getElementById("txtTitle").value;
    const newContent = document.getElementById("txtContent").value;
    const newImages =document.getElementById("inpImage").files;
    const userID = getCookie("user_id");

    //const feedback = "Title: "+newTitle+"\tContent: "+newContent+"\tid: "+userID
    //console.log(feedback)


    //API call to add a post to the database:
    try{
        const formdata = new FormData();
        formdata.append("title", newTitle);
        formdata.append("content", newContent);
        formdata.append("user_id", userID);
        
        for(let i=0; i< newImages.length; i++){
            formdata.append("images", newImages[i]);
        }

        const response = await fetch('http://127.0.0.1:8000/posts', {
            method: 'POST',
            body: formdata
        });

        if(!response.ok){
            alert("Network response was not OK");
        }

        console.log(response)

        const data = await response.json()

        if(data.post_id){
            console.log(data.post_id)
            alert("upload successful")
            window.location.href = "homePage.html"
        }
    }
    catch (error){
        console.error("network error: ", error)
    }
});


//to get the user id so that the foreign key of user id can be filled.
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