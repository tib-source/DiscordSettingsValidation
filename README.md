# Ansible Discord Validation

##Ansible Playbook Repository
###Overview
This repository contains an Ansible playbook designed to check discord audio settings by extracting it from their leveldb folder. It fetches the leveldb folder, places it in the `files/db_container` then runs the `scrips/ldb.py`. This script extracts the `mediaEngine` json settings that discord uses to configure audio. This is generated and placed into `files/db_output`. 

Ansible then checks each of these output json files against a whatever critera is set on `utils/discord-audio-check.yml`

##Playbook Structure
The playbook is divided into three main sections:

Clear Old LevelDB Files: Removes outdated LevelDB and JSON files from designated directories.
Fetch Folders from Each Pod: Gathers specific folders from each immersion pod, closes Discord processes, and copies necessary files.
Configure Discord Settings: Executes scripts to manage LevelDB extraction and perform audio checks on Discord files.
