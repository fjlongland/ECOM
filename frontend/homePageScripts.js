document.addEventListener("DOMContentLoaded", async function(){
    const postList = document.getElementById("lstPosts");

    try{
        const response = await fetch("http://127.0.0.1:8000/posts", {
            method: 'GET'
        });

        if(!response.ok){
            alert("failed to retrieve posts");
            return;
        }

        const posts = await response.json();

        for (const post of posts){
            const postDiv = document.createElement("div");
            postDiv.classList.add("post");

            postDiv.innerHTML = "<h2>"+post.post_title+"</h2>"+
                                "<p>"+post.post_content+"</p>"+
                                "<div class='images' id='images-"+post.post_id+"'></div>"+
                                "<hr>";


            postDiv.addEventListener("click", function(){
                console.log(post.post_id);
                document.cookie = "post_id="+post.post_id;
                window.location = "viewPost.html"
            })

            postList.appendChild(postDiv);

            fetchImages(post.post_id);
        }

    }

    catch(error){
        console.error("Error loading posts", error);
    }


    async function fetchImages(post_id) {
        const imageContainer = document.getElementById('images-'+post_id);
        
        try{
            const imageresponse = await fetch('http://127.0.0.1:8000/images/'+post_id, {
                method: 'GET'
            });

            if (!imageresponse.ok){
                alert("cant load images");
                return;
            }

            const images = await imageresponse.json();

            for(const image of images){
                const img = document.createElement("img");
                console.log(image.image_loc)
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

});