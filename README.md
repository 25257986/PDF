# Measurement Tables Generator

This repository contains a Python script that generates formatted measurement tables for electrical measurements at different current/voltage levels.

## Overview

The script generates three tables based on reference data:
1. **200mV Measurements** - Voltage measurements at 200 millivolts
2. **20mA Measurements** - Current measurements at 20 milliamps
3. **10mA Measurements** - Current measurements at 10 milliamps

Each table contains the following columns (MSC column excluded):
- `Freq(Hz)` - Frequency in Hertz
- `V` - Voltage measurement
- `I` - Current measurement
- `P(V*I)` - Power (Voltage × Current)
- `V^2` - Voltage squared
- `I^2` - Current squared
- `% Error to analytical` - Percentage error compared to analytical values
- `Est % spread` - Estimated percentage spread
- `Est SNR dB` - Estimated Signal-to-Noise Ratio in decibels

## Requirements

- Python 3.x
- NumPy
- Pandas

## Installation

Install the required dependencies:

```bash
pip install numpy pandas
```

## Usage

Run the script to generate and display all three tables:

```bash
python3 generate_tables.py
```

The script will output:
- Formatted tables with proper column alignment
- Scientific notation for very small numbers (< 0.001)
- NaN values for missing data at 50Hz and 3050Hz frequencies
- No column overflow or viewing errors

## Output Format

The tables are formatted with:
- 140 character width for optimal viewing
- Centered column headers
- Consistent spacing and alignment
- Clear separation between tables

## Example Output

```
============================================================================================================================================
Table 1: 200mV Measurements
============================================================================================================================================
  Freq(Hz)       V           I          P(V*I)        V^2          I^2       % Error to analytical    Est % spread    Est SNR dB  
--------------------------------------------------------------------------------------------------------------------------------------------
     50         NaN         NaN          NaN          NaN          NaN                NaN                 NaN            NaN      
    150        0.2036      0.0028     5.7555e-04     0.0415     7.9895e-06           2.6569              0.6358        43.9333    
    ...
```

## Notes

- Data points at 50Hz and 3050Hz are marked as NaN (Not a Number) indicating missing or invalid measurements
- Very small numbers are displayed in scientific notation (e.g., 5.7555e-04) for better readability
- All measurements are precisely formatted to 4 decimal places for consistency
