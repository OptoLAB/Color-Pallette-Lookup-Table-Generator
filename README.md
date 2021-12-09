# Color Pallette Lookup Table Generator
 Simple Python script for thermal camera color pallette generation 
## About
Script is written for use with [thermal camera project](https://github.com/OptoLAB/MLX90640-Thermal-Camera-STM32-STemWin). It generates lookup table containing 256 24bit color values based on selected color pallette (map). User can choose predefined color map from matplotlib or define custom using LinearSegmentedColormap.   

pallette.h contains generated lookup tables for several pallettes ilustrated bellow:

<p align="center">
 <p align="right">
  <br> Plasma &ensp; <img src="https://github.com/OptoLAB/Color-Pallette-Lookup-Table-Generator/blob/main/demo/img/plasma.jpg" width="400"/>
 </p>
 <p align="right"> 
  <br> Hot&Cold &ensp; <img src="https://github.com/OptoLAB/Color-Pallette-Lookup-Table-Generator/blob/main/demo/img/Hot%26Cold.jpg" width="400"/>
 </p>
</p>
