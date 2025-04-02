const audio = document.getElementById('audioPlayer');
const transcript = document.getElementById('transcript');
const timestampLines = document.getElementsByTagName("h5");

let anchor = document.createElement("a");
anchor.innerText = "Sermon index";
anchor.setAttribute("href", "../hollensen_idx.html");
let body = document.getElementsByTagName("body")[0];
body.insertBefore(anchor, body.firstChild);


function iconLinks(size) {
    const head = document.getElementsByTagName("head")[0];
    const icoLink = document.createElement("link");
    icoLink.setAttribute("rel", "icon");
    icoLink.setAttribute("type", "image/ico");
    icoLink.setAttribute("sizes", size);
    icoLink.setAttribute("href", "favicon-" + size + ".ico");
    head.appendChild(icoLink);
}
iconLinks("16x16");
iconLinks("32x32");
iconLinks("180x180");

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