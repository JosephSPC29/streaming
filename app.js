const videoGrid = document.getElementById('video-grid');

// Función para renderizar videos sin usar innerHTML
async function loadVideos() {
    try {
        const response = await fetch('http://TU-IP-EC2:8000/videos');
        const videos = await response.json();

        videos.forEach(video => {
            const card = document.createElement('article');
            card.className = 'video-card';

            const img = document.createElement('img');
            img.src = video.thumbnail_url;
            img.alt = video.title;

            const title = document.createElement('h3');
            title.textContent = video.title; // Seguro contra XSS

            card.appendChild(img);
            card.appendChild(title);
            videoGrid.appendChild(card);
        });
    } catch (error) {
        console.error("Error cargando videos:", error);
    }
}

document.addEventListener('DOMContentLoaded', loadVideos);