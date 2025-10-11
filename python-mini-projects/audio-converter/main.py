import os, sys
from pydub import AudioSegment

if len(sys.argv) != 3:
    print(f"{sys.argv[0]} <audio file> <format>")
    sys.exit(1)

file_name = sys.argv[1]
frm = sys.argv[2]

file_path = os.path.abspath(file_name)
file_base = os.path.basename(file_name)
file_ext = file_name.split(".")[-1]

print(f"Converting from {file_ext} to {frm}")

# only run if converting to a different format
if not(file_name.endswith(str("." + frm))):
    track = AudioSegment.from_file(file_name, file_ext)
    new_name = file_base.replace(file_ext, frm)

    # save to the same folder as original file
    new_path = file_path.replace(file_base, new_name)
    track.export(new_path, format=frm)
    print(f"File saved to {new_path}")