document.addEventListener("DOMContentLoaded", async function(){
    const post_id = getCookie("post_id"); 
    
    try{
        const response = await fetch('http://127.0.0.1:8000/posts/'+post_id, {
            method: "GET",
        })

        if(!response.ok){
            alert("Network error occured while trying to retrieve post.");
            return;
        }

        const data = await response.json();

        if(data.post_id){
            console.log("post retrieved: ", data.post_id);

            document.getElementById("postTitle").textContent = data.post_title;
            document.getElementById("postContent").textContent = data.post_content;
            fetchImages(data.post_id);
        }
    }
    catch(error){
        console.error("an error occured while trying to fetch post: ",error);
    }
        
})


async function fetchImages(post){

    console.log("fetching images for post: ", post);

    const imageContainer = document.getElementById("images");

    try{
        const imageResponse = await fetch('http://127.0.0.1:8000/images/'+post, {
            method: "GET"
        });

        if(!imageResponse.ok){
            alert("Networ error occured");
            return;
        }
        
        const images = await imageResponse.json();

        for (const image of images){
            const img = document.createElement("img");
            img.src = "http://127.0.0.1:8000/"+image.image_loc;

            img.style.width = "200px";
            img.style.height = "200px";
            img.style.objectFit = "cover";

            imageContainer.appendChild(img);
        }

    }
    catch(error){
        console.error("there was an error while trying to fetch images: ", error);
    }
}

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
