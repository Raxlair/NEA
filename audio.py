from process_audio_capture import ProcessAudioCapture
import time
import files

def captureSentenceAudio(game):
    processes = ProcessAudioCapture.enumerate_audio_processes()

    for window in processes: #gets the pid of the window thats passed in throught the parameter game
        if window.window_title == game:
            gamePID = window.pid

    audioFileNum = files.fileCouter("audio/audioCounter.txt") #gets the current audio file number

    with ProcessAudioCapture(
        output_path=f"audio/output{audioFileNum}.wav",
        pid = gamePID

    ) as capture:
        capture.start()
        time.sleep(8)  # Capture audio for 8 seconds
        capture.stop()

    return f"audio/output{audioFileNum}.wav"
