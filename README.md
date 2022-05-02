# meshTopologyVisualer

This is a functional code of meshtopologyVisualizer from yoppy-tjhin.

This code is functional as of May 2020 with all updated libraries for both Python and Arduino.

![alt text](https://github.com/jorgelvv/meshTopologyVisualizer/blob/master/Main_Window.png?raw=true)


A simple Python program running on PC to visualize ESP8266 painlessMesh topology.
This app captures the MeshTopology sent by ESP8266 on serial port.  The app processes the MeshTopology and visualize it. The graph is interactive. A click on a node will pop up a dialog box. Through the dialog box we can set and read parameters on a ESP8266 node.
The ESP8266 Arduino codes are available at:
https://github.com/yoppy-tjhin/espMesh

The app is started from main_window.py. It then loads a window from top.py. The top.py orchestrates all other functions, such as 
