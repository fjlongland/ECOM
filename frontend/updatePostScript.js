document.addEventListener("DOMContentLoaded", async function(){
    
    const list = document.getElementById("lstUPosts");
    const post_id = getCookie("post_id")


    try{
        const post = await fetch("http://127.0.0.1:8000/posts/"+post_id, {
            method: "GET",
        });

        if(!post.ok){
            alert("could not retrieve posts for user: "+ user_id)
            return;
        }

        const data = await post.json();

        document.getElementById("txtUpdateTitle").value=data.post_title;
        document.getElementById("txtUpdateContent").value=data.post_content;
    }

    catch(error){
        console.error("Error loading posts", error);
    }

    fetchImages(post_id)

    async function fetchImages(post_id) {
        const imageContainer = document.getElementById('images');

        try{
            const imageresponse = await fetch('http://127.0.0.1:8000/images/'+post_id, {
                method: "GET",
            });

            if(!imageresponse.ok){
                alert("could not return images");
                return;
            }

            const images = await imageresponse.json();

            for(const image of images){
                const img = document.createElement("img");
                img.src = "http://127.0.0.1:8000/"+image.image_loc;
                img.alt = "";

                img.style.width = "200px";
                img.style.height = "200px";
                img.style.objectFit = "cover";

                img.id = image.image_id;

                img.addEventListener("click", async function() {

                    const isShure = confirm("Are you shure you want to remove this image?");
                    if(isShure){
                        removeImage(image.image_id);
                    }
                    else{
                        return;
                    }

                    
                })

                imageContainer.appendChild(img);

            }

            const btn = document.createElement("button");
            btn.textContent = "new";
            btn.style.width = "200px";
            btn.style.height = "200px";
            btn.style.verticalAlign = "top";
            btn.id = "newImage";
            imageContainer.appendChild(btn);

            const inp = document.createElement("input");
            inp.type = "file";
            inp.accept = "image/png, image/jpeg, image/jpg";
            inp.style.display = "none";
            inp.id = "inpImage";
            document.body.appendChild(inp);

        }
        catch(error){
            console.error("there was an error loading images: ", error);
        }

        document.getElementById("newImage").addEventListener("click", async function(){
            const inp = document.getElementById("inpImage")
            inp.click();

        })

        const inp = document.getElementById("inpImage")

        inp.addEventListener("change", async function(){

            const post_id = getCookie("post_id");
        
            if (inp.files.length > 0){
                const file = inp.files[0];
        
                const formdata = new FormData();
        
                formdata.append("image", file);
                formdata.append("post_id", post_id);
        
                try{
                    const response = await fetch("http://127.0.0.1:8000/images/", {
                        method: "POST",
                        body: formdata,
                    });
        
                    if(!response.ok){
                        alert("Network error while trying to add image");
                    }
        
                    const data = await response.json();
        
                    if(data.image_id){
                        alert("Image added: ", data.image_id);
                        location.reload();
                    }
                }
                catch(error){
                    console.error("there was an error while trying to add inade: ", error);
                }
            }
        })
        
    }
})

document.getElementById("btnSubmit").addEventListener("click", async function() {
    const updateTitle = document.getElementById("txtUpdateTitle").value;
    const updateContent = document.getElementById("txtUpdateContent").value;
    const post_id = getCookie("post_id");
    console.log(post_id);
    try{
        const formdata = new URLSearchParams();

        formdata.append("title", updateTitle);
        formdata.append("content", updateContent);

        console.log("tile: "+updateTitle+"  contetn: "+updateContent)

        const response = await fetch("http://127.0.0.1:8000/posts/"+post_id, {
            method: "PUT",
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: formdata,
        })

        if(!response.ok){
            alert("could not update post!");
            return;
        }

        const data = await response.json();

        console.log(data)

        if(data.post_id){
            alert("post: "+data.post_id+" was updated successfuly!");
            window.location.href = "userPosts.html"
        }

    }
    catch(error){
        console.error("there was a network error while trying to update post: ", error);
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

document.getElementById("btnDelete").addEventListener("click", async function () {

    const post_id = getCookie("post_id");

    try{
        const response = await fetch('http://127.0.0.1:8000/posts/'+post_id, {
            method: "DELETE"
        });

        if(response.status !== 204){
            alert("could not delete post");
            return;
        }

        alert("post: ("+post_id+") was deleted successfully.");
    }
    catch(error){
        console.error("there was an error while trying to delete post:", error);
    }
    
});


async function removeImage(id){
    try{
        const response = await fetch("http://127.0.0.1:8000/images/"+id, {
            method: "DELETE",
        })
        
        if(response.status !== 204){
            alert("could not felete image ")
            return;
        }   

        //const data = await response.json();



        alert("image ("+id+") was deleted successfully!")
        location.reload()
        
    }
    catch(error){
        console.error("Error while trying to delete image: ", error);
    }
};