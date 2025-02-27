const audio = document.getElementById('audioPlayer');
const transcript = document.getElementById('transcript');
const timestampLines = document.getElementsByTagName("h5");

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