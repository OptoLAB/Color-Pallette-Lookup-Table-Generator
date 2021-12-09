# Color Pallette Lookup Table Generator
 Simple Python script for thermal camera color pallette generation 
## About
Script is written for use with [thermal camera project](https://github.com/OptoLAB/MLX90640-Thermal-Camera-STM32-STemWin). It generates lookup table containing 256 24bit color values based on selected color pallette (map). User can choose predefined color map from matplotlib or define custom using LinearSegmentedColormap.   

pallette.h contains generated lookup tables for several pallettes ilustrated bellow:
<p align="center">
 <br> Plasma <br> <img src="https://github.com/OptoLAB/Color-Pallette-Lookup-Table-Generator/blob/main/demo/img/plasma.jpg" width="400"/>
 <br> Rainbow <br> <img src="https://github.com/OptoLAB/Color-Pallette-Lookup-Table-Generator/blob/main/demo/img/rainbow.jpg" width="400"/>
 <br> Seismic <br> <img src="https://github.com/OptoLAB/Color-Pallette-Lookup-Table-Generator/blob/main/demo/img/seismic.jpg" width="400"/>
 <br> Hot <br> <img src="https://github.com/OptoLAB/Color-Pallette-Lookup-Table-Generator/blob/main/demo/img/hot.jpg" width="400"/>
 <br> Grayscale <br> <img src="https://github.com/OptoLAB/Color-Pallette-Lookup-Table-Generator/blob/main/demo/img/grayscale.jpg" width="400"/>
 <br> Viridis <br> <img src="https://github.com/OptoLAB/Color-Pallette-Lookup-Table-Generator/blob/main/demo/img/viridis.jpg" width="400"/>
 <br> Hot&Cold <br> <img src="https://github.com/OptoLAB/Color-Pallette-Lookup-Table-Generator/blob/main/demo/img/Hot%26Cold.jpg" width="400"/>
 <br> HotSpot <br> <img src="https://github.com/OptoLAB/Color-Pallette-Lookup-Table-Generator/blob/main/demo/img/hotspot.jpg" width="400"/>
 <br> ColdSpot <br> <img src="https://github.com/OptoLAB/Color-Pallette-Lookup-Table-Generator/blob/main/demo/img/coldspot.jpg" width="400"/>
</p>

Video demosntration: [youtube](https://youtu.be/KOCp_KNmq_Y) 
