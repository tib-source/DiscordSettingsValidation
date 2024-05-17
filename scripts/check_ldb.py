import plyvel
import csv
import base64

# Open the LevelDB database folder
origin = "C:\\Users\\tibebe.demissie_thed\\AppData\\Roaming\\discord\\Local Storage\\leveldb"
db = plyvel.DB(origin, create_if_missing=False)


# Prepare the CSV file to dump the contents of the LDB file to read
output = open("./output.txt", "w")

# Optionally write headers

# The key and value are bytes so we need to construct them with the b prefix.
# The keys are all prefixed with _https://discord.com\x00\x01 or _https://discordapp.com\x00\x01 where \x00\x01 are the first two bytes of the key.
# The values also need to have the \x01 byte prefixed.

# Data types as far as I can tell:
# If the value should be a string then it needs to be wrapped in quotes after the \x01 byte.
# e.g. b'\x01"test value"'
# If the value is a boolean or number it doesn't need quotes.
# e.g. b'\x01true' or b'\x01888433399'
# If the value is a JSON object I don't think it needs to be wrapped in quotes,
# but the JSON needs to be stringified first (in Javascript: JSON.stringify(value)).
# e.g. b'\x01{"_state":{"pendingUsages":[]},"_version":0}'

# The following line will write a key and value to the original database.
# This will either add a new entry or overwrite an existing one if the key already exists.
# db.put(b'_https://discord.com\x00\x01testKey', b'\x01"test value"')

# Iterate over the database and write to CSV
# Some keys and values can't be decoded so we need to catch those errors and skip them.

for key, value in db:
    # key_to_write = 'testKey'
    # if f'\x00\x01{key_to_write}' in key.decode('utf-8'):
    #     print(value.decode('utf-8'))

    try:
        key_str = key
        value_str = value

    except UnicodeDecodeError:
        continue  # Skip this entrycl

    output.write(f"{key_str} ---->  {value_str}")
# Clean up
db.close()
output.close()
