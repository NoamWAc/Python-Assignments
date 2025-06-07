import sys, codecs, os

if len(sys.argv) < 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

# Better version of the code that I got from ChatGPT that uses codecs to handle the ROT13 encoding. Includes the encode function with inherent error handling.
def get_unique_filename(base):
    if not os.path.exists(base):
        return base
    name, ext = os.path.splitext(base)
    i = 1
    while True:
        new_name = f"{name}({i}){ext}"
        if not os.path.exists(new_name):
            return new_name
        i += 1

src = sys.argv[1]

# Determine output file name
name, ext = os.path.splitext(src)
if name.endswith('.rot13'):
    # remove '.rot13' before the extension
    target = name[:-6] + ext
else:
    # add '.rot13' before the extension
    target = name + '.rot13' + ext

# Make sure we don't overwrite an existing file
target = get_unique_filename(target)

# Try to read original. If not binary, transform and write to new file
try:
    with open(src, 'r', encoding='utf-8') as f:
        content = f.read()
except UnicodeDecodeError:
    sys.exit(1)

with open(target, 'w', encoding='utf-8') as f:
    f.write(codecs.encode(content, 'rot_13'))

#Thiscould be improved also by first creating a string file, then adding into the get_unique_filename function the ability to compare your string to the similarly named file, and if it's identical then say it already exists.





# def main():
#     if len(sys.argv) != 2:
#         exit(f"Usage: {sys.argv[0]} FILENAME")
#     filename = sys.argv[1]
#     with open(filename) as fh:
#         for line in fh:
#             # This code was suggested by Copilot. It reads a file line by line and applies the ROT13 cipher to each character in the line.
#             # It handles both uppercase and lowercase letters, leaving other characters unchanged.
#             line = line.strip()
#             if not line:
#                 continue
#             rot13_line = []
#             for char in line:
#                 if 'a' <= char <= 'z':
#                     rot13_char = chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
#                 elif 'A' <= char <= 'Z':
#                     rot13_char = chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
#                 else:
#                     rot13_char = char
#                 rot13_line.append(rot13_char)
    

# try: #code I got from ChatGPT
#     with open(sys.argv[1], 'r+', encoding='utf-8') as f:
#         content = f.read()
#         f.seek(0)
#         f.write(codecs.encode(content, 'rot_13'))
#         f.truncate()
# except UnicodeDecodeError:
#     pass  # silently skip binary or non-UTF-8 files

# main()