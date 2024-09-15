import random
from moviepy.editor import *
import moviepy.video.fx.all as vfx
import ffmpeg

# Function to apply random effects on the video clips
def apply_random_effects(clip):
    effects = [
        lambda clip: vfx.speedx(clip, random.uniform(0.5, 2.0)),  # Random speed
        lambda clip: vfx.mirror_x(clip),  # Mirror horizontally
        lambda clip: vfx.mirror_y(clip),  # Mirror vertically
        lambda clip: vfx.time_mirror(clip),  # Reverse video
        lambda clip: vfx.lum_contrast(clip, lum=random.uniform(0.5, 2), contrast=random.uniform(0.5, 2)),  # Luminosity/Contrast
        lambda clip: vfx.rotate(clip, angle=random.choice([0, 90, 180, 270])),  # Rotate randomly
        lambda clip: vfx.fadein(clip, duration=random.uniform(0.5, 2)),  # Fade in
        lambda clip: vfx.fadeout(clip, duration=random.uniform(0.5, 2)),  # Fade out
        lambda clip: vfx.colorx(clip, factor=random.uniform(0.5, 2)),  # Random color changes
        lambda clip: vfx.resize(clip, random.uniform(0.5, 1.5))  # Random resizing
    ]
    
    # Apply a random subset of effects
    for effect in random.sample(effects, k=random.randint(1, len(effects))):
        clip = effect(clip)
    
    return clip

# Main remix function
def remix_video(input_video_path, output_video_path, num_slices=5):
    # Load video file
    video = VideoFileClip(input_video_path)
    
    # Create random clips by slicing the video
    duration = video.duration
    slices = []
    
    for _ in range(num_slices):
        start_time = random.uniform(0, duration - 1)
        end_time = min(duration, start_time + random.uniform(0.5, 2.0))
        slice_clip = video.subclip(start_time, end_time)
        
        # Apply random effects to each slice
        slice_clip = apply_random_effects(slice_clip)
        
        slices.append(slice_clip)
    
    # Concatenate the modified slices
    final_clip = concatenate_videoclips(slices, method="compose")
    
    # Write the output video to file
    final_clip.write_videofile(output_video_path, codec="libx264", audio_codec="aac")

# Example usage
input_video = "input_video.mp4"  # Replace with your input video path
output_video = "crazy_remix.mp4"  # Output video file name
remix_video(input_video, output_video)
