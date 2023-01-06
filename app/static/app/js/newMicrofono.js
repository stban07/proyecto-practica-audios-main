console.log("poooooooooooooooop");


let recorder;
let audio = document.getElementById("audio");


function stopRecording() {
  recorder.stop();
}


function startRecording() {
  navigator.mediaDevices.getUserMedia({ audio: true })
    .then(stream => {
      recorder = new MediaRecorder(stream);
      recorder.start();

      let chunks = [];
      recorder.addEventListener("dataavailable", event => {
        chunks.push(event.data);
      });

      recorder.addEventListener("stop", () => {
        console.log(chunks);
        let blob = new Blob(chunks, { type: "audio/mp3" });

        console.log(blob);

        
        audio.src = URL.createObjectURL(blob);
        audio.controls = true;
        audio.autoplay = true;
        console.log(audio)
      });
    });
}





