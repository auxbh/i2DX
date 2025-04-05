* __Scroll Down__ for installation instructions (Windows).
* Clone the repo to download latest version of i2DX.


__Video Demos__

* [1 iPad + 1 iPod Touch + StepMania](http://www.youtube.com/watch?v=C3cZsZYK4Jo) / Ristaccia
* [2 iPads + StepMania](http://www.youtube.com/watch?v=f7GBGOO5DRw&feature=channel) / garden
* [2 iPads v.s. Home Controller + Lunatic Rave 2](http://www.youtube.com/watch?v=RfJ5FoVZiBs) / being torn the sky
* [1 iPad](http://www.youtube.com/watch?v=tiuCW311GEA) / Elisha

i2DX
=======

i2DX is a web-based IIDX controller for mobile devices.

You can use it with [StepMania 5](http://www.stepmania.com/), especially with the
[beatmaniaIIDX15 theme](http://www.stepmania.com/forums/showthread.php?28308-SM5-beatmaniaIIDX15-theme-and-noteskin&p=195991#post195991).
You can also use it with Lunatic Rave 2, or other sims as well.

Because it is __web based__, you just need to run the server application on your computer,
and then point your device's web browser to the server (they must be on the same wireless network!).
__No application installation needed on the device.__

--------------

It uses the following technologies:

* [WebSocket](http://websocket.org/)
* Python __3.9+__
	* [Tornado Web Server](http://www.tornadoweb.org/)
* [keyboard](https://pypi.org/project/keyboard/)



How it works
------------

The server serves the file to the device's web browser, which connects back to
the server via WebSocket and send the press / release events.

__On Windows__: The WebSocket server then uses the keyboard library to press the keys.

Controllers
---------------

* IIDX 1P
* IIDX 2P
* IIDX Turntable
* Jubeat
* Pop'n Music
* Taiko

Setup
-----

* A computer with beatmaniaIIDX simulator (recommended: LR2, Beatoraja or [Bemuse](https://bemuse.ninja))
* An iPad or an Android tablet device with a web browser
* An additional mobile device (optional, used as a dedicated scratch controller)
* A working WiFi connection (may or may not have internet access. In my opinion, ad-hoc is the best)

Server Instructions (Windows + autopy)
-------------------------------------------------

Download __Python__ from [python.org](http://python.org/download/).

Then open command prompt and run

    pip install keyboard
    pip install tornado

And then go to the `server` directory and run `start.bat` **as an administrator** (or the keys won't be registered by your tools).

Now navigate your client to the the server (see __Client Instructions__ below).
Try pressing some keys, it should type something on your keyboard.

With that set, open your tools and map the pressed key to the corresponding input!


<span id="client-instructions">Client Instructions</span>
-------------------
Use your device's web browser to navigate to

    http://[your ip]:9876/

You will see a launcher. Set the settings and click Launch i2DX.

You can bring another device to use it as a dedicated scratch controller.

On the mobile device, the dedicated scratch controller supports rotational movements, so if you
can borrow another mobile device, then you can use it as a scratch controller! On other devices, it
only supports up / down movement, but it can be used to make the buttons and the turntable farther.

Now that if you have a scratch controller, you may not want it on the main controller anymore,
you can move the scratch area of the main controller to the right.


Hard Mode
---------

In normal mode, you can slide between buttons.
On real machines / controllers, you might not be able to do that, so in hard
mode, you cannot slide between buttons.

Keyboard maps (Windows)
-----------------------

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
