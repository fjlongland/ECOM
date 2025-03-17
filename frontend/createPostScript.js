document.getElementById("btnUpload").addEventListener("click", async function(){
    const newTitle = document.getElementById("txtTitle").value;
    const newContent = document.getElementById("txtContent").value;
    const newImages =document.getElementById("inpImage").files;

    const feedback = "Title: "+newTitle+"\tContent: "+newContent

    console.log(feedback)

    try{
        const formdata = new FormData();
        formdata.append("title", newTitle);
        formdata.append("content", newContent);
        
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
        }
    }
    catch (error){
        console.error("network error: ", error)
    }
})