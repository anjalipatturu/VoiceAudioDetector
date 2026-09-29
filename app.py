import streamlit as st
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Voice Activity Detector",
    page_icon="🎙️",
    layout="wide"
)


# ============================================================
# TITLE
# ============================================================

st.title("🎙️ Voice Activity Detector")

st.write(
    "Detect speech and silence regions in an audio file "
    "using RMS energy."
)


# ============================================================
# 1. UPLOAD AUDIO
# ============================================================

st.header("📁 Upload Audio")

uploaded_file = st.file_uploader(
    "Choose an audio file",
    type=["wav", "mp3", "ogg"]
)


# ============================================================
# PROCESS AUDIO
# ============================================================

if uploaded_file is not None:

    # --------------------------------------------------------
    # 2. AUDIO PLAYER
    # --------------------------------------------------------

    st.header("🔊 Audio Player")

    st.audio(
        uploaded_file,
        format=uploaded_file.type
    )


    # --------------------------------------------------------
    # LOAD AUDIO
    # --------------------------------------------------------

    audio, sr = librosa.load(
        uploaded_file,
        sr=16000,
        mono=True
    )


    # Check empty audio

    if len(audio) == 0:

        st.error("The audio file is empty.")

        st.stop()


    # Duration

    duration = len(audio) / sr


    # --------------------------------------------------------
    # FRAME SETTINGS
    # --------------------------------------------------------

    frame_length = 512
    hop_length = 256


    # --------------------------------------------------------
    # RMS ENERGY
    # --------------------------------------------------------

    rms = librosa.feature.rms(
        y=audio,
        frame_length=frame_length,
        hop_length=hop_length
    )[0]


    # Convert RMS to decibels

    rms_db = librosa.amplitude_to_db(
        rms,
        ref=np.max
    )


    # --------------------------------------------------------
    # SPEECH THRESHOLD
    # --------------------------------------------------------

    threshold_db = -35


    # --------------------------------------------------------
    # SPEECH DETECTION
    # --------------------------------------------------------

    speech_frames = rms_db > threshold_db


    # --------------------------------------------------------
    # SPEECH / SILENCE PERCENTAGE
    # --------------------------------------------------------

    speech_percentage = (
        np.mean(speech_frames) * 100
    )

    silence_percentage = (
        100 - speech_percentage
    )


    # ========================================================
    # 3. DETECTION SUMMARY
    # ========================================================

    st.header("📊 Detection Summary")


    col1, col2, col3, col4 = st.columns(4)


    col1.metric(
        "🗣️ Speech",
        f"{speech_percentage:.1f}%"
    )


    col2.metric(
        "🔇 Silence",
        f"{silence_percentage:.1f}%"
    )


    col3.metric(
        "⏱️ Duration",
        f"{duration:.2f} sec"
    )


    col4.metric(
        "🎚️ Sample Rate",
        f"{sr} Hz"
    )


    # ========================================================
    # FRAME TIMES
    # ========================================================

    frame_times = librosa.frames_to_time(
        np.arange(len(speech_frames)),
        sr=sr,
        hop_length=hop_length
    )


    # ========================================================
    # 4. SPEECH ACTIVITY TIMELINE
    # ========================================================

    st.header("🗣️ Speech Activity Timeline")


    fig1, ax1 = plt.subplots(
        figsize=(12, 2.5)
    )


    # Convert False/True → 0/1

    activity = speech_frames.astype(int)


    ax1.step(
        frame_times,
        activity,
        where="post"
    )


    ax1.set_yticks([0, 1])

    ax1.set_yticklabels(
        ["Silence", "Speech"]
    )


    ax1.set_xlabel(
        "Time (seconds)"
    )


    ax1.set_title(
        "Speech / Silence Detection"
    )


    ax1.set_ylim(
        -0.2,
        1.2
    )


    ax1.grid(
        alpha=0.3
    )


    fig1.tight_layout()


    st.pyplot(
        fig1,
        use_container_width=True
    )


    plt.close(fig1)


    # ========================================================
    # 5. WAVEFORM WITH SPEECH REGIONS
    # ========================================================

    st.header("〰️ Waveform with Speech Regions")


    fig2, ax2 = plt.subplots(
        figsize=(12, 4)
    )


    # Draw waveform

    librosa.display.waveshow(
        audio,
        sr=sr,
        ax=ax2
    )


    # Highlight speech regions

    for i in range(len(speech_frames)):

        if speech_frames[i]:

            start_time = frame_times[i]


            if i + 1 < len(frame_times):

                end_time = frame_times[i + 1]

            else:

                end_time = duration


            ax2.axvspan(
                start_time,
                end_time,
                alpha=0.25
            )


    ax2.set_title(
        "Detected Speech Regions"
    )


    ax2.set_xlabel(
        "Time (seconds)"
    )


    ax2.set_ylabel(
        "Amplitude"
    )


    ax2.grid(
        alpha=0.3
    )


    fig2.tight_layout()


    st.pyplot(
        fig2,
        use_container_width=True
    )


    plt.close(fig2)


    # ========================================================
    # 6. RMS ENERGY
    # ========================================================

    st.header("📈 RMS Energy")


    rms_times = librosa.frames_to_time(
        np.arange(len(rms_db)),
        sr=sr,
        hop_length=hop_length
    )


    fig3, ax3 = plt.subplots(
        figsize=(12, 4)
    )


    # RMS energy

    ax3.plot(
        rms_times,
        rms_db,
        label="RMS Energy"
    )


    # Threshold line

    ax3.axhline(
        threshold_db,
        linestyle="--",
        label=f"Threshold ({threshold_db} dB)"
    )


    ax3.set_title(
        "RMS Energy Over Time"
    )


    ax3.set_xlabel(
        "Time (seconds)"
    )


    ax3.set_ylabel(
        "Energy (dB)"
    )


    ax3.legend()


    ax3.grid(
        alpha=0.3
    )


    fig3.tight_layout()


    st.pyplot(
        fig3,
        use_container_width=True
    )


    plt.close(fig3)


    # ========================================================
    # 7. DETECT SPEECH SEGMENTS
    # ========================================================

    st.header("🗣️ Detected Speech Segments")


    segments = []


    start_time = None


    for i, is_speech in enumerate(speech_frames):


        current_time = frame_times[i]


        # Speech starts

        if is_speech and start_time is None:

            start_time = current_time


        # Speech ends

        elif not is_speech and start_time is not None:

            end_time = current_time


            segments.append(
                (start_time, end_time)
            )


            start_time = None


    # Speech continues until end

    if start_time is not None:

        segments.append(
            (start_time, duration)
        )


    # --------------------------------------------------------
    # DISPLAY SEGMENTS
    # --------------------------------------------------------

    if len(segments) > 0:

        for i, (start, end) in enumerate(
            segments,
            start=1
        ):

            st.write(
                f"**Segment {i}** → "
                f"{start:.2f}s - {end:.2f}s"
            )

    else:

        st.warning(
            "No speech segments detected."
        )


    # ========================================================
    # 8. TECHNICAL INFORMATION
    # ========================================================

    st.header("🔍 Technical Information")


    col1, col2 = st.columns(2)


    with col1:

        st.write(
            f"**Sample Rate:** {sr} Hz"
        )

        st.write(
            f"**Frame Length:** {frame_length} samples"
        )

        st.write(
            f"**Hop Length:** {hop_length} samples"
        )


    with col2:

        st.write(
            f"**Number of Frames:** {len(rms)}"
        )

        st.write(
            f"**RMS Threshold:** {threshold_db} dB"
        )

        st.write(
            f"**Audio Duration:** {duration:.2f} seconds"
        )


    # ========================================================
    # 9. RESULT
    # ========================================================

    st.header("🧠 Result")


    if speech_percentage > 5:

        st.success(
            "Speech activity detected."
        )

    else:

        st.warning(
            "Very little speech detected."
        )


   