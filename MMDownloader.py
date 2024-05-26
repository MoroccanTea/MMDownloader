import os
from pytube import YouTube
import metadata

def download_audio(video_url, output_path, video_number, total_videos):
    try:
        video = YouTube(video_url)
        audio_stream = video.streams.filter(only_audio=True).order_by('abr').last()
        
        if audio_stream is None:
            print(f"No audio stream found for video: {video_url}")
            return
        
        print(f"Downloading {video_number}/{total_videos}: {video_url}")
        output_file = audio_stream.download(output_path=output_path)
        
        base, ext = os.path.splitext(output_file)
        new_file = base + '.m4a'
        os.rename(output_file, new_file)
        
        print(f"Download complete - saved in {new_file}")
    except Exception as e:
        print(f"Error downloading audio for video: {video_url}")
        print(f"Error message: {str(e)}")

def print_banner():
    print("""
    __  __ __  __ _____                      _                 _           
    |  \/  |  \/  |  __ \                    | |               | |          
    | \  / | \  / | |  | | _____      ___ __ | | ___   __ _  __| | ___ _ __ 
    | |\/| | |\/| | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
    | |  | | |  | | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   
    |_|  |_|_|  |_|_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_| V1.0
                                                                 
                                                       by MoroccanTea
    """)

def main():
    print_banner()
    
    links_file = "links.txt"
    downloads_folder = "downloaded_music"
    output_folder = "finalized_music"

    # Create the output folder if it doesn't exist
    if not os.path.exists(downloads_folder):
        os.makedirs(downloads_folder)
    
    if not os.path.exists(links_file):
        print("No links file found. Skipping download.")
        metadata.add_metadata(downloads_folder, output_folder)
        return

    with open(links_file, "r") as file:
        video_links = file.readlines()
    
    total_videos = len(video_links)
    
    for index, link in enumerate(video_links, start=1):
        link = link.strip()
        if link:
            download_audio(link, downloads_folder, index, total_videos)
    
    print("Finished downloading audio files.")

    # Add metadata to the downloaded audio files
    print("Adding metadata to downloaded audio files...")
    metadata.add_metadata(downloads_folder, output_folder)
    
    print("Finished.")

if __name__ == "__main__":
    main()