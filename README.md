# DriveRiff

DriveRiff is a real-time AI generated music mixing and improvisation tool designed to create dynamic soundtracks that adapt to simulated driving statuses. It combines various music genres, including Techno, Rock, Funk, and Reggae, to provide an immersive and interactive audio experience.

## Features

- **Real-Time Music Mixing**: Dynamically mixes and adjusts music tracks based on driving status.
- **AI Multi-Genre Support**: Includes multiple-style of AI-generated sound tracks from SoundRaw.io, e.g. Techno, Rock, Funk, and Reggae genres.
- **Customizable Tracks Intensity Control**: Adjusts the volume of individual music components based on driving simulation inputs.
- **Pygame Integration**: Utilizes the `pygame.mixer` module for sound playback and channel control.
- **Socket Communication**: Connects to a driving status simulator using the `socketio` library to cooperate in protopie.connect.

## Prerequisites

Before running DriveRiff, ensure you have the following installed:

- Python 3.x
- `pygame` library
- `python-socketio` library
- protopie.connect

You can install the required libraries using pip:

```bash
pip install pygame python-socketio
```

## Directory Structure

Ensure the following directory structure for the project:

```
DriveRiff/
├── main.py                  # Main script to run the application
├── Sound_Tracks/            # Directory containing all music tracks
│   ├── Techno_bass_decreased.MP3
│   ├── Rock_bass_decreased.MP3
│   ├── funk_bass_decreased.MP3
│   ├── Raggae_bass_1.MP3
│   └── ...                  # Additional sound files
```

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/DriveRiff.git
   cd DriveRiff
   ```

2. Place all required audio files in the `Sound_Tracks` directory.

3. Update the `address` variable in the script to match your driving simulator's address (default: `http://127.0.0.1:9981`).

4. Run the script:

   ```bash
   python main.py
   ```

## Code Overview

### Initialization

- Initializes the `pygame.mixer` module for handling audio playback.
- Sets up 40 audio channels for simultaneous playback of multiple tracks.

### Music Tracks

- **Techno**: Includes bass, melody, drum, and backing tracks.
- **Rock**: Includes bass, melody, drum, and backing tracks, with variations for intensity.
- **Funk**: Includes bass, melody, drum, and backing tracks, with soft and strong variations.
- **Reggae**: Includes bass, melody, drum, and backing tracks, with additional layers for improvisation.

### Channel Assignment

Each music component is assigned to a specific channel, allowing independent playback and volume control.

### Intensity Control

The `update_volume_reggae()` function demonstrates how to dynamically adjust the volume of Reggae tracks based on driving settings.

## Future Enhancements

- Add more genres and tracks for greater diversity.
- Implement a GUI for easier control and visualization.
- Improve driving status integration for smoother transitions.
- Add support for custom user-defined tracks.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Enjoy creating adaptive soundtracks with DriveRiff! 🎵
