# ezdxf-donut

A simple Python module to draw donuts (filled circles with a hole) in DXF format using [ezdxf](https://ezdxf.mozman.at/), mimicking the behavior of the `DONUT` command in AutoCAD.

---

## 📌 Overview

This module allows you to easily create **donut shapes** (circles with an inner hole) in DXF files. It uses `LWPolyline` with `const_width` and `bulge` values to simulate the appearance of a donut as done by the `DONUT` command in AutoCAD.

> ⚠️ Note: This is a simplified simulation that works well in most CAD viewers like AutoCAD, but may not be fully compatible with all DXF readers.

---

## 🧩 Features

- Draw donuts with outer and inner diameters.
- Mimics the behavior of AutoCAD's `DONUT` command.
- Easy integration with `ezdxf`.

---

## 📦 Installation

Make sure you have `ezdxf` installed:

```bash
pip install ezdxf