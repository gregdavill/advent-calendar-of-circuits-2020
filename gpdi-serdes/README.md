# SYZYGY-SGMII breakout

SYZYGY is an FPGA expansion standard for medium to high speed interfaces. Learn more and check out the specifications here: [https://syzygyfpga.io/](https://syzygyfpga.io/)

---

## What is it

A breakout to output video to common digital displays, also supports inputs from digital displays

This is connected to the SERDES via a SYZYGY-TXR connector. Hopefully will enable testing the 5Gbps output for high resolution GPDI.


## Folder structure

```
kicad-src: KiCad v6 source files
production:
 - Gerbers:      [project]_gerbers.zip
 - Schematic:    [project].pdf
 - Board render: [project].png
```

## Render

![Render](production/gpdi-serdes.png "Render")