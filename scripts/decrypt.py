import os 


def decrypt(path, current): 
    with open(path, "rb") as file: 
        binary_data = file.read()
        encodings_to_try = [
            'utf-8',
            'utf-16',
            'utf-32',
            'iso-8859-1',  # Latin-1
            'windows-1252',  # Windows Latin-1
            'ascii',
            'cp1251',  # Cyrillic
            'shift_jis',  # Japanese
            'euc-jp',
            'iso-2022-jp',
            'gb2312',  # Simplified Chinese
            'big5',  # Traditional Chinese
            'koi8-r',  # Russian
            'utf-16-le',  # UTF-16 Little Endian
            'utf-16-be',  # UTF-16 Big Endian
            'latin-2',    # ISO-8859-2
            'windows-1250',  # Windows Central European
            'windows-1251',  # Windows Cyrillic
            'windows-1253',  # Windows Greek
            'windows-1254',  # Windows Turkish
            'windows-1255',  # Windows Hebrew
            'windows-1256',  # Windows Arabic
            'windows-1257',  # Windows Baltic
            'windows-1258',  # Windows Vietnamese
            'macroman',    # Mac Roman
            'mac-roman',   # Another form of Mac Roman
            'us-ascii',    # ASCII
            'iso-8859-3',  # Latin-3
            'iso-8859-4',  # Latin-4
            'iso-8859-5',  # Latin/Cyrillic
            'iso-8859-6',  # Latin/Arabic
            'iso-8859-7',  # Latin/Greek
            'iso-8859-8',  # Latin/Hebrew
            'iso-8859-9',  # Latin-5
            'iso-8859-10',  # Latin-6
            'iso-8859-13',  # Latin-7
            'iso-8859-14',  # Latin-8
            'iso-8859-15',  # Latin-9
            'iso-8859-16',  # Latin-10
            'cp437',  # IBM PC graphics
            'cp850',  # IBM PC multilingual
            'cp852',  # Latin-2 (Eastern European)
            'cp855',  # Cyrillic
            'cp857',  # Turkish
            'cp858',  # Latin-1 with Euro
            'cp860',  # Portuguese
            'cp861',  # Icelandic
            'cp862',  # Hebrew
            'cp863',  # French Canadian
            'cp864',  # Arabic
            'cp865',  # Nordic
            'cp866',  # Cyrillic (Russian)
            'cp869',  # Greek
        ]

        for encoding in encodings_to_try:
            try:
                text_data = binary_data.decode(encoding)
                with open(f"scripts/output/{current}_output_{encoding}.txt", "w", encoding="utf-8") as text_file:
                    text_file.write(text_data)
            except UnicodeDecodeError: 
                print(file)
            except Exception: 
                pass

def main():
    origin = "C:\\Users\\tibebe.demissie_thed\\AppData\\Roaming\\discord\\Local Storage\\leveldb"
    for subdir, dirs, files in os.walk(origin):
        for file in files: 
            if file.endswith('.ldb'):
                decrypt(os.path.join(origin, file), file )


if __name__ == "__main__": 
    main()