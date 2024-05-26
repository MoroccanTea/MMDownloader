import os
import requests
import json
import subprocess

# Set the path to the downloaded_music folder
source_folder = "downloaded_music"
output_folder = "finalized_music"

# Create the output folder if it does not exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate over each file in the music folder
for filename in os.listdir(source_folder):
    if filename.endswith(".m4a"):
        # Get the file path
        file_path = os.path.join(source_folder, filename)
        track_title = os.path.splitext(filename)[0]
        print(f"[+] Processing file: {filename}")

        # Search for the track on iTunes
        search_url = f"https://itunes.apple.com/search?term={track_title}&entity=song&limit=1"
        response = requests.get(search_url)
        data = json.loads(response.text)

        if data["resultCount"] > 0:
            # Extract the metadata from the iTunes API response
            track_info = data["results"][0]
            title = track_info.get("trackName", "")
            artist = track_info.get("artistName", "")
            album = track_info.get("collectionName", "")
            genre = track_info.get("primaryGenreName", "")
            release_year = track_info.get("releaseDate", "")[:4]
            track_number = track_info.get("trackNumber", "")
            contributing_artists = track_info.get("artistName", "")
            publisher = track_info.get("copyright", "").split("©")[0].strip()
            #producer = ""  # Producer information is not available in the iTunes API need to find another source
            length = track_info.get("trackTimeMillis", "")
            cover_url = track_info.get("artworkUrl100", "").replace("100x100", "600x600")

            # Download the album/track cover image
            cover_path = os.path.join(source_folder, f"{track_title}_cover.jpg")
            response = requests.get(cover_url)
            with open(cover_path, "wb") as file:
                file.write(response.content)

            # Update the metadata using FFmpeg
            ffmpeg_command = [
                "ffmpeg",
                "-i",
                file_path,
                "-i",
                cover_path,
                "-map",
                "0",
                "-map",
                "1",
                "-c:a",
                "aac",
                "-b:a",
                "192k",
                "-c:v",
                "copy",
                "-metadata",
                f"title={title}",
                "-metadata",
                f"artist={artist}",
                "-metadata",
                f"album={album}",
                "-metadata",
                f"genre={genre}",
                "-metadata",
                f"date={release_year}",
                "-metadata",
                f"track={track_number}",
                "-metadata",
                f"publisher={publisher}",
                "-metadata",
                f"composer={contributing_artists}",
                "-metadata",
                f"genre={genre}",
                "-disposition:v:0",
                "attached_pic",
                f"{file_path}.temp.m4a",
            ]
            subprocess.run(ffmpeg_command, check=True)

            # Remove the original file and rename the temporary file
            os.remove(file_path)
            os.rename(f"{file_path}.temp.m4a", file_path)

            # Rename the file to include only the title
            new_filename = f"{title}.m4a"
            new_file_path = os.path.join(output_folder, new_filename)
            os.rename(file_path, new_file_path)
            os.remove(cover_path)

            print(f"Metadata added and file renamed: {new_filename}")
        else:
            print(f"[-] No metadata found for: {filename} :(")