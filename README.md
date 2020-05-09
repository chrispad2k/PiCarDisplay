# PiCarDisplay

## General

PiCarDisplay is an application with which you can display (primarily) text sent from an app on a RGB-Matrix controlled by a Raspberry Pi.

## Setup the Pi

In this application a 64x32 matrix is used. The matrix is controlled and supplied by the "Adafruit RGB Matrix HAT" which is plugged in to the GPIO pins of the Raspberry Pi.

In order to run the application, clone this repository onto your Raspberry Pi.

The Adafruit HAT needs to be connected to a power supply with 5V and at least 6-8A of power. The Raspberry Pi itself **should not** be attached to power over Micro-USB.

## Running the Demo

The demo can be run with the provided demo script
```
./demo.sh -D 0
```

The `-D` parameter specifies the demo to be run. The available demos are listed in `./rpi-rgb-led-matrix/examples-api-use/README.md`.

## Products

* Raspberry Pi 2 Model B (https://www.amazon.de/Raspberry-Model-ARM-Cortex-A53-1-2GHz-Bluetooth/dp/B01CD5VC92/ref=sr_1_3?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1VJ5I66B5BOHA&dchild=1&keywords=raspberry+pi+2+model+b&qid=1589055157&sprefix=raspberry+pi+2+model%2Caps%2C179&sr=8-3)
* Adafruit HAT (https://www.adafruit.com/product/2345)
* RGB Matrix (https://www.amazon.de/gp/product/B06XNJZN89/ref=ppx_yo_dt_b_asin_title_o05_s00?ie=UTF8&psc=1)
