document.addEventListener("DOMContentLoaded", async function(){
    
    const list = document.getElementById("lstUPosts");
    const user_id = getCookie("user_id")


    try{
        const posts = await fetch("http://127.0.0.1:8000/posts/user/"+user_id, {
            method: "GET",
        });

        if(!posts.ok){
            alert("could not retrieve posts for user: "+ user_id)
            return;
        }

        const postlist = await posts.json();

        for (const pst of postlist){
            const postDiv = document.createElement("div");
            postDiv.classList.add("pst");

            postDiv.innerHTML = "<h2>"+pst.post_title+"</h2>"+
                                "<p>"+pst.post_content+"</p>"+
                                "<div class='images' id='images-"+pst.post_id+"'></div>"+
                                "<button class='btnEdit' data-id='"+pst.post_id+"'>Edit</button>";
            
            list.appendChild(postDiv);

            fetchImages(pst.post_id);
        }
    }

    catch(error){
        console.error("Error loading posts", error);
    }

    async function fetchImages(post_id) {
        const imageContainer = document.getElementById('images-'+post_id);

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

                imageContainer.appendChild(img);

            }
        }
        catch(error){
            console.error("there was an error loading images: ", error);
        }
        
    }
})


document.addEventListener("click", function(event){
    if (event.target.classList.contains("btnEdit")){
        let postId = event.target.dataset.id;
        console.log("selecting post id: ", postId)

        document.cookie ="post_id="+encodeURIComponent(postId)+"; path=/";

        window.location.href = "updatePost.html";
    }

    console.log(document.cookie)
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

