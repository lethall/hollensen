const audio = document.getElementById('audioPlayer');
const transcript = document.getElementById('transcript');
const timestampLines = document.getElementsByTagName("h5");

let anchor = document.createElement("a");
anchor.innerText = "Sermon index";
anchor.setAttribute("href", "../hollensen_idx.html");
let body = document.getElementsByTagName("body")[0];
body.insertBefore(anchor, body.firstChild);

for (let ii = 0; ii < timestampLines.length; ++ii) {
    const line = timestampLines[ii];
    line.addEventListener("click", e => {
        const tStamp = line.getHTML().split(":");
        audio.currentTime = parseInt(tStamp[0]) * 60 + parseInt(tStamp[1]);
    });
}

audio.addEventListener('timeupdate', () => {
    const currentTime = parseInt(audio.currentTime);

    for (let ii = 0; ii < timestampLines.length; ++ii) {
        const line = timestampLines[ii];
        const tStamp = line.getHTML().split(":");
        if (currentTime == (parseInt(tStamp[0]) * 60 + parseInt(tStamp[1]))) line.scrollIntoView(true);
    }
});