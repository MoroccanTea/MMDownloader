# MMDownloader
MMDownloader is a simple tool to download music from Youtube with metadata and a cover image.
Soon more sources will be added.

## Requirements
- Python 3.6 or higher
- FFmpeg

## Installation

```bash
git clone https://github.com/MoroccanTea/MMDownloader.git
cd MMDownloader
pip install -r requirements.txt
```

## Usage
Add the Youtube links to the `links.txt` file and run the following commands:

```bash
python download.py
python metadata.py
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
