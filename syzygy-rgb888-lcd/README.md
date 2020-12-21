# SYZYGY breakout

SYZYGY is an FPGA expansion standard for medium to high speed interfaces. Learn more and check out the specifications here: [https://syzygyfpga.io/](https://syzygyfpga.io/)

---

## What is it

Connection to the 5" LCD paired with the Sipeed Tang Nano. Which is a 800x480 LCD with RGB888 connections. All 8bits per channel are connected through to the SYZYGY connector.


## Folder structure

```
kicad-src: KiCad v6 source files
production:
 - Gerbers:      [project]_gerbers.zip
 - Schematic:    [project].pdf
 - Board render: [project].png
```

## Render

![Render](production/syzygy-rgb888-lcd.png "Render")