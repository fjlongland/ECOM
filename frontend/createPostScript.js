document.getElementById("btnUpload").addEventListener("click", async function(){
    const newTitle = document.getElementById("txtTitle").value;
    const newContent = document.getElementById("txtContent").value;

    const feedback = "Title: "+newTitle+"\tContent: "+newContent

    console.log(feedback)

    try{
        const formdata = new URLSearchParams();
        formdata.append("title", newTitle);
        formdata.append("content", newContent);

        const response = await fetch('http://127.0.0.1:8000/posts', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
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