# Measurement Tables Generator

This repository contains a Python script that generates formatted measurement tables for electrical measurements at different current/voltage levels, **including LaTeX code for use in Overleaf**.

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

Run the script to generate both console output and LaTeX tables:

```bash
python3 generate_tables.py
```

The script will:
- Display formatted tables in the console with proper column alignment
- Generate a `measurement_tables_latex.tex` file containing LaTeX code ready for Overleaf
- Use scientific notation for very small numbers (< 0.001)
- Show NaN values for missing data at 50Hz and 3050Hz frequencies

## Output Files

1. **Console output** - Formatted tables displayed in the terminal
2. **measurement_tables_latex.tex** - LaTeX table code ready to copy into your Overleaf document

## Using in Overleaf

1. Run the script: `python3 generate_tables.py`
2. Open the generated `measurement_tables_latex.tex` file
3. Copy the LaTeX code for the tables you need
4. Paste into your Overleaf LaTeX document
5. The tables use standard LaTeX table environment with:
   - `\begin{table}[htbp]` for table positioning
   - `\caption{}` for table titles
   - `\label{}` for referencing (tab:200mv, tab:20ma, tab:10ma)
   - Proper formatting with `\hline` separators every 5 rows

## LaTeX Table Features

- Professional formatting with borders
- Centered columns
- Bold headers with proper mathematical notation ($V^2$, $I^2$, V×I)
- Scientific notation formatted as $\times 10^{-n}$
- Missing values shown as "---"
- Horizontal lines every 5 rows for readability

## Example LaTeX Output

```latex
\begin{table}[htbp]
  \centering
  \caption{200mV Measurements}
  \label{tab:200mv}
  \small
  \begin{tabular}{|c|c|c|c|c|c|c|c|c|}
    \hline
    \textbf{Freq (Hz)} & \textbf{V} & \textbf{I} & ... \\
    \hline
    150 & 0.2036 & 0.0028 & 5.7555$\times 10^{-4}$ & ... \\
    ...
  \end{tabular}
\end{table}
```

## Notes

- Data points at 50Hz and 3050Hz are marked as NaN (Not a Number) or "---" in LaTeX, indicating missing or invalid measurements
- Very small numbers are displayed in scientific notation for better readability
- All measurements are precisely formatted to 4 decimal places for consistency
- The LaTeX tables are ready to use without modification in Overleaf
