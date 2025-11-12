#!/usr/bin/env python3
"""
Generate formatted measurement tables for 200mV, 20mA, and 10mA
Based on reference data, excluding the MSC column.
"""

import numpy as np
import pandas as pd

# Data for 200mV table
data_200mv = {
    'Freq(Hz)': [50, 150, 250, 350, 450, 550, 650, 750, 850, 950, 1050, 1150, 1250, 
                 1350, 1450, 1550, 1650, 1750, 1850, 1950, 2050, 2150, 2250, 2350, 
                 2450, 2550, 2650, 2750, 2850, 2950, 3050],
    'V': [np.nan, 0.2036, 0.2013, 0.2000, 0.1993, 0.1989, 0.1982, 0.1981, 0.1981, 
          0.1984, 0.1987, 0.1989, 0.1991, 0.1992, 0.1992, 0.1989, 0.1988, 0.1985, 
          0.1982, 0.1981, 0.1979, 0.1983, 0.1990, 0.1993, 0.1995, 0.2007, 0.2031, 
          0.2053, 0.2078, 0.2200, np.nan],
    'I': [np.nan, 0.0028, 0.0047, 0.0066, 0.0084, 0.0103, 0.0122, 0.0140, 0.0159, 
          0.0178, 0.0197, 0.0216, 0.0235, 0.0254, 0.0273, 0.0291, 0.0310, 0.0328, 
          0.0347, 0.0365, 0.0384, 0.0403, 0.0424, 0.0444, 0.0463, 0.0485, 0.0510, 
          0.0535, 0.0559, 0.0604, np.nan],
    'P(V*I)': [np.nan, 5.7555e-04, 9.4747e-04, 0.0013, 0.0017, 0.0021, 0.0024, 0.0028, 
               0.0031, 0.0035, 0.0039, 0.0043, 0.0047, 0.0051, 0.0054, 0.0058, 0.0062, 
               0.0065, 0.0069, 0.0072, 0.0076, 0.0080, 0.0084, 0.0088, 0.0092, 0.0097, 
               0.0104, 0.0110, 0.0116, 0.0133, np.nan],
    'V^2': [np.nan, 0.0415, 0.0405, 0.0400, 0.0397, 0.0395, 0.0393, 0.0392, 0.0393, 
            0.0394, 0.0395, 0.0395, 0.0396, 0.0397, 0.0397, 0.0396, 0.0395, 0.0394, 
            0.0393, 0.0392, 0.0392, 0.0393, 0.0396, 0.0397, 0.0398, 0.0403, 0.0412, 
            0.0421, 0.0432, 0.0484, np.nan],
    'I^2': [np.nan, 7.9895e-06, 2.2163e-05, 4.3352e-05, 7.1400e-05, 1.0639e-04, 
            1.4780e-04, 1.9650e-04, 2.5262e-04, 3.1611e-04, 3.8731e-04, 4.6601e-04, 
            5.5184e-04, 6.4467e-04, 7.4366e-04, 8.4851e-04, 9.6009e-04, 0.0011, 
            0.0012, 0.0013, 0.0015, 0.0016, 0.0018, 0.0020, 0.0021, 0.0024, 0.0026, 
            0.0029, 0.0031, 0.0036, np.nan],
    '% Error to analytical': [np.nan, 2.6569, 1.5343, 1.0165, 0.8215, 0.7372, 0.6961, 
                              0.6794, 0.6568, 0.6977, 0.7019, 0.6419, 0.6273, 0.6229, 
                              0.6001, 0.5410, 0.5550, 0.5309, 0.4578, 0.4639, 0.4482, 
                              0.4529, 0.4289, 0.3171, 0.2206, 0.2075, 0.1770, 0.2470, 
                              0.7282, 2.0851, np.nan],
    'Est % spread': [np.nan, 0.6358, 0.4435, 0.3375, 0.3055, 0.2709, 0.2687, 0.2406, 
                     0.2431, 0.2536, 0.2520, 0.2429, 0.2384, 0.2333, 0.2402, 0.2229, 
                     0.2235, 0.2262, 0.2417, 0.2320, 0.1985, 0.2185, 0.2219, 0.2051, 
                     0.1948, 0.1968, 0.2012, 0.1986, 0.1998, 0.1710, np.nan],
    'Est SNR dB': [np.nan, 43.9333, 47.0618, 49.4340, 50.2987, 51.3423, 51.4140, 
                   52.3733, 52.2847, 51.9164, 51.9735, 52.2912, 52.4531, 52.6432, 
                   52.3873, 53.0394, 53.0145, 52.9111, 52.3338, 52.6909, 54.0432, 
                   53.2112, 53.0774, 53.7589, 54.2061, 54.1208, 53.9256, 54.0412, 
                   53.9902, 55.3397, np.nan]
}

# Data for 20mA table
data_20ma = {
    'Freq(Hz)': [50, 150, 250, 350, 450, 550, 650, 750, 850, 950, 1050, 1150, 1250, 
                 1350, 1450, 1550, 1650, 1750, 1850, 1950, 2050, 2150, 2250, 2350, 
                 2450, 2550, 2650, 2750, 2850, 2950, 3050],
    'V': [4.2614, 1.1432, 0.8514, 0.6092, 0.4742, 0.3880, 0.3283, 0.2848, 0.2519, 
          0.2259, 0.2051, 0.1879, 0.1735, 0.1612, 0.1505, 0.1414, 0.1333, 0.1261, 
          0.1198, 0.1142, 0.1094, 0.1054, 0.1021, 0.0994, 0.0969, 0.0943, 0.0917, 
          0.0904, 0.0899, 0.0927, np.nan],
    'I': [0.0201, 0.0161, 0.0201, 0.0201, 0.0201, 0.0201, 0.0201, 0.0201, 0.0202, 
          0.0203, 0.0203, 0.0204, 0.0205, 0.0205, 0.0206, 0.0207, 0.0208, 0.0209, 
          0.0209, 0.0211, 0.0212, 0.0214, 0.0217, 0.0221, 0.0225, 0.0228, 0.0231, 
          0.0235, 0.0242, 0.0260, np.nan],
    'P(V*I)': [0.0855, 0.0184, 0.0171, 0.0122, 0.0095, 0.0078, 0.0066, 0.0057, 0.0051, 
               0.0046, 0.0042, 0.0038, 0.0036, 0.0033, 0.0031, 0.0029, 0.0028, 0.0026, 
               0.0025, 0.0024, 0.0023, 0.0023, 0.0022, 0.0022, 0.0022, 0.0022, 0.0021, 
               0.0021, 0.0022, 0.0024, np.nan],
    'V^2': [18.1592, 1.3069, 0.7248, 0.3711, 0.2248, 0.1506, 0.1077, 0.0811, 0.0635, 
            0.0510, 0.0421, 0.0353, 0.0301, 0.0260, 0.0226, 0.0200, 0.0178, 0.0159, 
            0.0144, 0.0130, 0.0120, 0.0111, 0.0104, 0.0099, 0.0094, 0.0089, 0.0084, 
            0.0082, 0.0081, 0.0086, np.nan],
    'I^2': [4.0254e-04, 2.5818e-04, 4.0268e-04, 4.0310e-04, 4.0367e-04, 4.0467e-04, 
            4.0466e-04, 4.0580e-04, 4.0794e-04, 4.1014e-04, 4.1281e-04, 4.1556e-04, 
            4.1886e-04, 4.2161e-04, 4.2423e-04, 4.2807e-04, 4.3115e-04, 4.3515e-04, 
            4.3870e-04, 4.4363e-04, 4.5001e-04, 4.5940e-04, 4.7302e-04, 4.8969e-04, 
            5.0630e-04, 5.2106e-04, 5.3342e-04, 5.5394e-04, 5.8554e-04, 6.7780e-04, 
            np.nan],
    '% Error to analytical': [0.8894, 1.3874, 0.7651, 0.8847, 0.8935, 0.7900, 0.7648, 
                              0.7503, 0.7256, 0.6610, 0.7078, 0.7209, 0.6622, 0.7004, 
                              0.6391, 0.6296, 0.6374, 0.5326, 0.5593, 0.4686, 0.4006, 
                              0.4707, 0.3733, 0.2406, 0.2296, 0.1204, 0.0017, 0.3640, 
                              0.5416, 0.2089, np.nan],
    'Est % spread': [0.3260, 0.6113, 0.2432, 0.2924, 0.3384, 0.2919, 0.2404, 0.3026, 
                     0.3430, 0.3826, 0.3082, 0.3138, 0.4103, 0.4017, 0.3509, 0.3482, 
                     0.4042, 0.4808, 0.4411, 0.4371, 0.4461, 0.5242, 0.5306, 0.4571, 
                     0.4653, 0.5415, 0.5397, 0.5563, 0.4693, 0.5309, np.nan],
    'Est SNR dB': [49.7348, 44.2749, 52.2813, 50.6790, 49.4118, 50.6955, 52.3821, 
                   50.3832, 49.2940, 48.3443, 50.2247, 50.0658, 47.7372, 47.9219, 
                   49.0960, 49.1628, 47.8675, 46.3606, 47.1098, 47.1875, 47.0110, 
                   45.6093, 45.5050, 46.8001, 46.6449, 45.3274, 45.3564, 45.0934, 
                   46.5711, 45.4993, np.nan]
}

# Data for 10mA table
data_10ma = {
    'Freq(Hz)': [50, 150, 250, 350, 450, 550, 650, 750, 850, 950, 1050, 1150, 1250, 
                 1350, 1450, 1550, 1650, 1750, 1850, 1950, 2050, 2150, 2250, 2350, 
                 2450, 2550, 2650, 2750, 2850, 2950, 3050],
    'V': [2.1326, 0.7100, 0.4265, 0.3050, 0.2376, 0.1947, 0.1649, 0.1434, 0.1268, 
          0.1141, 0.1038, 0.0952, 0.0880, 0.0818, 0.0765, 0.0719, 0.0678, 0.0643, 
          0.0614, 0.0588, 0.0568, 0.0547, 0.0527, 0.0509, 0.0491, 0.0478, 0.0465, 
          0.0462, 0.0465, 0.0499, np.nan],
    'I': [0.0101, 0.0101, 0.0101, 0.0101, 0.0101, 0.0101, 0.0101, 0.0101, 0.0102, 
          0.0102, 0.0103, 0.0103, 0.0104, 0.0104, 0.0104, 0.0105, 0.0105, 0.0106, 
          0.0107, 0.0108, 0.0110, 0.0111, 0.0112, 0.0113, 0.0114, 0.0115, 0.0117, 
          0.0120, 0.0126, 0.0140, np.nan],
    'P(V*I)': [0.0215, 0.0071, 0.0043, 0.0031, 0.0024, 0.0020, 0.0017, 0.0015, 0.0013, 
               0.0012, 0.0011, 9.8082e-04, 9.1038e-04, 8.5064e-04, 7.9906e-04, 7.5460e-04, 
               7.1373e-04, 6.8208e-04, 6.5718e-04, 6.3594e-04, 6.2230e-04, 6.0600e-04, 
               5.9015e-04, 5.7603e-04, 5.5893e-04, 5.5028e-04, 5.4398e-04, 5.5472e-04, 
               5.8566e-04, 6.9724e-04, np.nan],
    'V^2': [4.5480, 0.5041, 0.1819, 0.0930, 0.0565, 0.0379, 0.0272, 0.0206, 0.0161, 
            0.0130, 0.0108, 0.0091, 0.0077, 0.0067, 0.0059, 0.0052, 0.0046, 0.0041, 
            0.0038, 0.0035, 0.0032, 0.0030, 0.0028, 0.0026, 0.0024, 0.0023, 0.0022, 
            0.0021, 0.0022, 0.0025, np.nan],
    'I^2': [1.0149e-04, 1.0114e-04, 1.0126e-04, 1.0141e-04, 1.0167e-04, 1.0192e-04, 
            1.0205e-04, 1.0269e-04, 1.0318e-04, 1.0410e-04, 1.0526e-04, 1.0620e-04, 
            1.0714e-04, 1.0804e-04, 1.0903e-04, 1.1003e-04, 1.1093e-04, 1.1241e-04, 
            1.1457e-04, 1.1682e-04, 1.2021e-04, 1.2292e-04, 1.2535e-04, 1.2787e-04, 
            1.2944e-04, 1.3256e-04, 1.3662e-04, 1.4445e-04, 1.5835e-04, 1.9539e-04, 
            np.nan],
    '% Error to analytical': [0.5545, 0.6051, 0.6639, 0.7017, 0.7407, 0.7665, 0.8125, 
                              0.8273, 0.8348, 0.9485, 0.9268, 0.9030, 0.9092, 0.9802, 
                              0.9520, 0.9918, 0.8517, 0.8832, 0.8094, 0.8511, 0.8189, 
                              0.6946, 0.6384, 0.5717, 0.5064, 0.5669, 0.2432, 0.3291, 
                              0.1368, 0.0062, np.nan],
    'Est % spread': [0.2145, 0.2703, 0.2880, 0.2592, 0.2530, 0.3598, 0.3621, 0.3759, 
                     0.4101, 0.4974, 0.5325, 0.5008, 0.5585, 0.6339, 0.5957, 0.6435, 
                     0.7232, 0.6505, 0.7966, 0.7946, 0.8045, 0.8972, 0.8623, 0.9298, 
                     0.9079, 0.8989, 1.0048, 1.0282, 0.9425, 0.8693, np.nan],
    'Est SNR dB': [53.3696, 51.3633, 50.8110, 51.7285, 51.9368, 48.8798, 48.8226, 
                   48.4977, 47.7422, 46.0657, 45.4740, 46.0071, 45.0591, 43.9594, 
                   44.4997, 43.8292, 42.8143, 43.7343, 41.9754, 41.9971, 41.8887, 
                   40.9422, 41.2866, 40.6316, 40.8390, 40.9256, 39.9577, 39.7579, 
                   40.5138, 41.2161, np.nan]
}

def format_value_latex(value, col):
    """Format a value for LaTeX output."""
    if pd.isna(value):
        return "---"
    elif col == 'Freq(Hz)':
        return f"{int(value)}"
    elif isinstance(value, float):
        # Use scientific notation for very small numbers
        if abs(value) < 0.001 and value != 0:
            return f"{value:.4e}".replace('e-0', r'$\times 10^{-').replace('e-', r'$\times 10^{-') + '}$'
        else:
            return f"{value:.4f}"
    else:
        return str(value)

def generate_latex_table(data, title, label):
    """Generate LaTeX table code."""
    df = pd.DataFrame(data)
    
    latex_code = []
    latex_code.append(f"% {title}")
    latex_code.append(r"\begin{table}[htbp]")
    latex_code.append(r"  \centering")
    latex_code.append(f"  \\caption{{{title}}}")
    latex_code.append(f"  \\label{{tab:{label}}}")
    latex_code.append(r"  \small")
    latex_code.append(r"  \begin{tabular}{|c|c|c|c|c|c|c|c|c|}")
    latex_code.append(r"    \hline")
    
    # Header row
    headers = []
    for col in df.columns:
        if col == 'Freq(Hz)':
            headers.append(r"\textbf{Freq (Hz)}")
        elif col == 'V':
            headers.append(r"\textbf{V}")
        elif col == 'I':
            headers.append(r"\textbf{I}")
        elif col == 'P(V*I)':
            headers.append(r"\textbf{P (V$\times$I)}")
        elif col == 'V^2':
            headers.append(r"\textbf{$V^2$}")
        elif col == 'I^2':
            headers.append(r"\textbf{$I^2$}")
        elif col == '% Error to analytical':
            headers.append(r"\textbf{\% Error}")
        elif col == 'Est % spread':
            headers.append(r"\textbf{Est \% spread}")
        elif col == 'Est SNR dB':
            headers.append(r"\textbf{Est SNR (dB)}")
        else:
            headers.append(f"\\textbf{{{col}}}")
    
    latex_code.append("    " + " & ".join(headers) + r" \\")
    latex_code.append(r"    \hline")
    
    # Data rows
    for idx, row in df.iterrows():
        values = []
        for col in df.columns:
            values.append(format_value_latex(row[col], col))
        latex_code.append("    " + " & ".join(values) + r" \\")
        if idx % 5 == 4:  # Add horizontal line every 5 rows for readability
            latex_code.append(r"    \hline")
    
    if len(df) % 5 != 0:  # Add final hline if not already added
        latex_code.append(r"    \hline")
    
    latex_code.append(r"  \end{tabular}")
    latex_code.append(r"\end{table}")
    latex_code.append("")
    
    return "\n".join(latex_code)

def format_table(data, title):
    """Format and display a table with proper alignment."""
    df = pd.DataFrame(data)
    
    print(f"\n{'='*140}")
    print(f"{title}")
    print(f"{'='*140}")
    
    # Define column widths for better formatting
    col_widths = {
        'Freq(Hz)': 12,
        'V': 12,
        'I': 12,
        'P(V*I)': 14,
        'V^2': 12,
        'I^2': 14,
        '% Error to analytical': 24,
        'Est % spread': 16,
        'Est SNR dB': 14
    }
    
    # Print header
    header = ""
    for col in df.columns:
        width = col_widths.get(col, 12)
        header += f"{col:^{width}}"
    print(header)
    print("-" * 140)
    
    # Print rows
    for idx, row in df.iterrows():
        line = ""
        for col in df.columns:
            width = col_widths.get(col, 12)
            value = row[col]
            
            if pd.isna(value):
                line += f"{'NaN':^{width}}"
            elif col == 'Freq(Hz)':
                line += f"{int(value):^{width}}"
            elif col in ['% Error to analytical', 'Est % spread', 'Est SNR dB']:
                line += f"{value:^{width}.4f}"
            elif isinstance(value, float):
                # Use scientific notation for very small numbers
                if abs(value) < 0.001 and value != 0:
                    line += f"{value:^{width}.4e}"
                else:
                    line += f"{value:^{width}.4f}"
            else:
                line += f"{str(value):^{width}}"
        print(line)
    
    print(f"{'='*140}\n")

def main():
    """Generate and display all three tables."""
    print("\n" + "="*140)
    print("MEASUREMENT TABLES - Without MSC Column")
    print("="*140)
    
    format_table(data_200mv, "Table 1: 200mV Measurements")
    format_table(data_20ma, "Table 2: 20mA Measurements")
    format_table(data_10ma, "Table 3: 10mA Measurements")
    
    print("\n" + "="*140)
    print("All tables generated successfully!")
    print("="*140)
    
    # Generate LaTeX output
    print("\nGenerating LaTeX code for Overleaf...")
    
    latex_output = []
    latex_output.append("% LaTeX tables for Overleaf")
    latex_output.append("% Copy the table code below into your Overleaf document")
    latex_output.append("% Note: Make sure to include \\usepackage{booktabs} in your preamble for better formatting")
    latex_output.append("")
    
    latex_output.append(generate_latex_table(data_200mv, "200mV Measurements", "200mv"))
    latex_output.append(generate_latex_table(data_20ma, "20mA Measurements", "20ma"))
    latex_output.append(generate_latex_table(data_10ma, "10mA Measurements", "10ma"))
    
    # Save LaTeX output to file
    with open('measurement_tables_latex.tex', 'w') as f:
        f.write("\n".join(latex_output))
    
    print("LaTeX code saved to 'measurement_tables_latex.tex'")
    print("You can copy this file content directly into your Overleaf document!")
    print("="*140)

if __name__ == "__main__":
    main()
