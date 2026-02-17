# The Perfect Human - Frame Counter

A Python utility to calculate precise film frame ranges for the film *"The Perfect Human"*.

## Overview

This script translates physical documentation coordinates (Page, Column, Frame) into exact linear frame numbers or ranges. It is designed for a specific template where:
- Each **Page** has **11 Columns**
- Each **Column** has **34 Frames**

## Prerequisites

- Python 3.x installed on your system.

## Setup

1. Clone or download this repository.
2. Navigate to the directory in your terminal:
   ```bash
   cd /path/to/frame-counter
   ```

## Usage

Run the script using Python:

```bash
python3 frame_counter.py
```

### Input Format

The script accepts input in two formats:

1.  **Single Frame coordinate:** `page-column-frame`
    -   Example: `1-2-1`
    -   Calculates the absolute frame number.

2.  **Frame Range with Count:** `page-column-frame count`
    -   Example: `1-2-1 10`
    -   Calculates the start and end frame numbers for a sequence of 10 frames.

### Examples

| Input      | Description                                      | Output  |
| :---       | :---                                             | :---    |
| `1-1-1`    | First frame of the film                          | `1`     |
| `1-2-1`    | Page 1, Column 2, Frame 1                        | `35`    |
| `1-2-1 10` | sequence starting at P1-C2-F1 with length 10     | `35-44` |

To exit the script, type `exit`, `quit`, or press `Ctrl+C`.
