# E-Paper Display using ESP IDF

This directory implements the E-Paper Display code using Espressif's ESP-IDF (IoT Development Framework).

## WSL-2 ESP-IDF Setup

https://youtu.be/eQ0D8pnZTSY?si=sJwv8-8tlvZuBL6y

You can copy nad paste the commands from here to setup ESP-IDF on WSL-2.

> If you use zsh or other terminal profile, you will need to change the commands that reference `.profile` to `.zshrc` or other profile.

https://gist.github.com/abobija/2f11d1b2c7cb079bec4df6e2348d969f

You can also either add $HOME/bin to path, or move `$HOME/bin/idfx` to `/usr/bin/idfx`.

I also had to open the normal Windows terminal and install the `esptool` and `esp_idf_monitor` package. 

```bash
pip install esptool esp_idf_monitor
```

## VSCode Tasks

I like to use VSCode Tasks to automate certain command sequences. Here's the tasks I have right now. You can change the `"label"` field to any label you want.

You may want to replace COM3 with which ever port your ESP-32 is connected to. 

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "type": "shell",
      "group": "build",
      "label": "Pre-Commit (custom)",
      "command": "idf.py build && idfx flash COM3 monitor"
    },
    {
      "type": "shell",
      "group": "build",
      "label": "Build Utils (custom)",
      "command": "idf.py build"
    },
  ]
}
```