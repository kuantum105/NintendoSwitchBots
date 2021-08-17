<h1>Nintendo Switch Bots</h1>

A hobby grade system for writing bots for the Nintendo Switch. The core of the bot uses [opencv](https://github.com/opencv/opencv) to process video capture input, [SwitchInputEmulator](https://github.com/wchill/SwitchInputEmulator) to send controller commands to the console, and Python for scripting bot logic. By "reading" game data through image recognition, and "writing" game data through controller input it is theoretically possible to write bots for most if not all Switch games. Also, this system does not directly modify game state in memory, so unless the game implements behavior based bot detection this bot is very difficult to detect.

Required software:
- [opencv](https://github.com/opencv/opencv)
- [SwitchInputEmulator](https://github.com/wchill/SwitchInputEmulator)
- [python](https://www.python.org/downloads/)
- [Gmail API](https://developers.google.com/gmail/api/guides/sending)

Required hardware:
- Nintendo Switch + Dock
- Video capture card
- Arduino UNO (or other device compatible SwitchInputEmulator)
- USB-to-UART adapter

<h2>Pokémon Sword/Shield Shiny Hatcher</h2>

Uses the Route 5 day care lady to hatch eggs until your PokéBox is full. Requires you to deposit a breeding pair of Pokémon first. Will email you whenever a shiny hatches, if the bot gets stuck, or if your PokéBox becomes full. Determines whether a Pokémon is shiny as it deposits them into the PokéBox by looking for the shiny stamp on the Pokémon's detail page. See successful hatches:
- [Litten](https://youtu.be/GRl-rYIsDsw)
- [Bulbasaur](https://youtu.be/_yu23dq0Rqs)
- [Mudkip](https://youtu.be/vp2THdn8IZM)

<h2>Legendary Shiny Finder</h2>

A oneoff bot that farms shiny Regieleki without soft resetting the game. Determines whether Regieleki is shiny by timing the slight hitch in the gameplay loop that occurs when the shiny sparkle animation plays. Note that while the following video does not show the capture of a shiny Regieleki, it does show the basic bot loop, and I was able to capture one off-screen after a couple of nights of running.
- [Regieleki](https://youtu.be/FjqbbE5pUqk)

<h2>Setup Instructions</h2>

1. Download all necessary software and ensure that associated Python libraries may initialize
2. Follow the setup instructions for [SwitchInputEmulator](https://github.com/wchill/SwitchInputEmulator)
3. Get yourself setup to use [Gmail API](https://developers.google.com/gmail/api/guides/sending)
4. Populate all the variables in Config.py (Windows users may determine their COM port by finding their USB-to-UART adapter in Device Manager)
5. If you have Pokémon Sword/Shield you can try running the egg hatching bot by navigating to SwordShieldShinyHatcher and calling `python .\SwordShieldShinyHatcher.py`, otherwise look to the existing bot scripts for examples and start writing your own!
