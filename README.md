# i2DX

i2DX is a web-based IIDX controller for mobile devices.

Because it is **web based**, you just need to run the server application on your computer,
and then point your device's web browser to the server.

--------------

It uses the following technologies:

* [WebSocket](http://websocket.org/)
* Python __3.9+__
	* [Tornado Web Server](http://www.tornadoweb.org/)
    * [keyboard](https://pypi.org/project/keyboard/)



## How it works

The server serves the file to the device's web browser, which connects back to
the server via WebSocket and send the press / release events.
The WebSocket server then uses the keyboard library to press the keys.

## Controllers

* IIDX 1P
* IIDX 2P
* IIDX Turntable
* Jubeat
* Pop'n Music
* Taiko

Setup
-----

* A computer with beatmania IIDX
* An iPad or an Android tablet device with a web browser
* An additional mobile device (optional, used as a dedicated scratch controller)
* A working WiFi connection (not required if using [adb reverse](#adb-reverse))

## Server Instructions

Download **Python** from [python.org](http://python.org/download/).

Then open command prompt and run

    pip install keyboard
    pip install tornado

And then go to the `server` directory and run `start.bat` **as an administrator** (or the keys won't be registered by your tools).

Now navigate your client to the the server (see **Client Instructions** below).
Try pressing some keys, it should type something on your keyboard.

With that set, open your tools and map the pressed key to the corresponding input!


## Client Instructions

Use your device's web browser to navigate to

    http://[your ip]:9876/

You will see a launcher. Set the settings and click Launch i2DX.

You can bring another device to use it as a dedicated scratch controller.

On the mobile device, the dedicated scratch controller supports rotational movements, so if you
can borrow another mobile device, then you can use it as a scratch controller! On other devices, it
only supports up / down movement, but it can be used to make the buttons and the turntable farther.

Now that if you have a scratch controller, you may not want it on the main controller anymore,
you can move the scratch area of the main controller to the right.


## Hard Mode

In normal mode, you can slide between buttons.
On real machines / controllers, you might not be able to do that, so in hard
mode, you cannot slide between buttons.

## adb reverse

You can improve latency by running i2DX with your Android device tethered to
your computer. However, this requires a little extra setup:

- Connect your Android device to your computer with a USB cable.
- If you haven't enabled Developer options on your device, do it by navigating to
the "About" page in your phone's settings, then tap "Build number" seven times.
This varies by device, so if unsure, look up the instructions for your specific
one.
- Navigate to Developer options and enable USB debugging.
- On your computer, download and extract [Android SDK Platform Tools](https://dl.google.com/android/repository/platform-tools-latest-windows.zip)
to your `i2DX\server\` folder.
- Navigate to the `i2DX\server\platform-tools` folder in File Explorer, click on the
address bar, type `cmd`, and hit Enter to open a command prompt.
- In the command prompt, type the following command: (change the port if required)

```
adb reverse tcp:9876 tcp:9876
```

- Start i2DX as normal.
- On your Android device, open your web browser, and change the address to `0.0.0.0:9876` (or the port you set it to).
- That's it!

The next time you want to use the controller, you only need to run the `adb reverse ...` command
again. To do this automatically when the game starts, add a line to the `start.bat`
script **before** the `python server-windows.py` line:

```
cd /d "%~dp0"
platform-tools\adb reverse tcp:9876 tcp:9876
python server-windows.py
pause
```

## Keyboard mapping

* `m`: Key 1
* `k`: Key 2
* `,`: Key 3
* `l`: Key 4
* `.`: Key 5
* `;`: Key 6
* `/`: Key 7
* `[`: Scratch Up
* `]`: Scratch Down
* `o`: Start
* `p`: Select

You can change key mappings in `server\config.ini`.

### Video Demos (Outdated)

* [1 iPad + 1 iPod Touch + StepMania](http://www.youtube.com/watch?v=C3cZsZYK4Jo) / Ristaccia
* [2 iPads + StepMania](http://www.youtube.com/watch?v=f7GBGOO5DRw&feature=channel) / garden
* [2 iPads v.s. Home Controller + Lunatic Rave 2](http://www.youtube.com/watch?v=RfJ5FoVZiBs) / being torn the sky
* [1 iPad](http://www.youtube.com/watch?v=tiuCW311GEA) / Elisha