# MMDownloader
MMDownloader is a simple tool to download music from Youtube with metadata and a cover image.
Soon more sources will be added.

## Requirements
- Python 3.6 or higher
- A recent version of FFmpeg

## Setup

For windows users, you can install FFmpeg using winget:

```sh
winget install ffmpeg
```

For linux users, you can install FFmpeg using apt:
```bash
sudo apt install ffmpeg
```

Then you can install the required python packages using pip:

```bash
git clone https://github.com/MoroccanTea/MMDownloader.git
cd MMDownloader
pip install -r requirements.txt
```

Copy and fill in the environment variables in the `.env` file:

```sh
cp .env.template .env
```

## Usage
Add the Youtube links to the `links.txt` file and run the following commands:

```bash
python MMDownloader.py
```

## License
[MIT](https://github.com/MoroccanTea/MMDownloader/blob/main/LICENSE)


## Upcoming Features
- [ ] Fix known issues
- [ ] Improve UI/UX
- [ ] Add more sources
- [ ] Add a GUI
- [ ] Add a download history
- [ ] Add a download scheduler
- [ ] Add a download speed limiter

## Known Issues
- The metadata is not always correct
- The cover image is not always correct
- File names on windows that contain some special characters crash the program
