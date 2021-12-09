# Color Pallette Lookup Table Generator
 Simple Python script for thermal camera color pallette generation 
## About
Script is written for use with [thermal camera project](https://github.com/OptoLAB/MLX90640-Thermal-Camera-STM32-STemWin). It generates lookup table containing 256 24bit color values based on selected color pallette (map). User can choose predefined color map from matplotlib or define custom using LinearSegmentedColormap.   

pallette.h contains generated lookup tables for several pallettes ilustrated bellow:

<p align="center">
 <br> Plasma&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/OptoLAB/Color-Pallette-Lookup-Table-Generator/blob/main/demo/img/plasma.jpg" width="400"/>
 <br> Rainbow&nbsp;&nbsp;&nbsp;<img src="https://github.com/OptoLAB/Color-Pallette-Lookup-Table-Generator/blob/main/demo/img/rainbow.jpg" width="400"/>
 <br> Seismic&nbsp;&nbsp;&nbsp;<img src="https://github.com/OptoLAB/Color-Pallette-Lookup-Table-Generator/blob/main/demo/img/seismic.jpg" width="400"/>
 <br> Hot       <img src="https://github.com/OptoLAB/Color-Pallette-Lookup-Table-Generator/blob/main/demo/img/hot.jpg" width="400"/>
 <br> Grayscale&nbsp;<img src="https://github.com/OptoLAB/Color-Pallette-Lookup-Table-Generator/blob/main/demo/img/grayscale.jpg" width="400"/>
 <br> Viridis   <img src="https://github.com/OptoLAB/Color-Pallette-Lookup-Table-Generator/blob/main/demo/img/viridis.jpg" width="400"/>
 <br> Hot&Cold  <img src="https://github.com/OptoLAB/Color-Pallette-Lookup-Table-Generator/blob/main/demo/img/Hot%26Cold.jpg" width="400"/>
 <br> HotSpot   <img src="https://github.com/OptoLAB/Color-Pallette-Lookup-Table-Generator/blob/main/demo/img/hotspot.jpg" width="400"/>
 <br> ColdSpot   <img src="https://github.com/OptoLAB/Color-Pallette-Lookup-Table-Generator/blob/main/demo/img/coldspot.jpg" width="400"/>
</p>
