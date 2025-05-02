
# Reconstructing Han Dynasty Western Regions Using MDS  
*A High School Research Project by Lin Yun-Han*

## Project Overview

This project aims to reconstruct the geographical distribution of countries in the Western Regions during the Han Dynasty using textual spatial data from historical Chinese texts (primarily the *Book of Han*, 漢書). Due to limited archaeological evidence and incomplete geographic records, traditional methods fail to restore such maps accurately. This research uses **Multidimensional Scaling (MDS)** and **directional stress optimization** to algorithmically reconstruct the map.

This is a high school Grade 11 (Senior Year 2) research project under the supervision of Prof. Tsung-Han Tsai (Academia Sinica) and Mr. Wei-Li Pan (Jianguo High School).

## Key Features

- **Data Preprocessing**: Cleans and classifies directional and distance data from historical records.
- **Graph Construction**: Builds a directed weighted graph based on country relations in the *Book of Han*.
- **MDS Approaches (4 types)**:
  1. **Scikit-Learn MDS** using Floyd–Warshall shortest path.
  2. **Stress Majorization** with iterative optimization.
  3. **Unit-Based Distance from Historical Hypotheses.**
  4. **Directional MDS** with constraints on vector directions.
- **Visualization Tools**: Uses matplotlib and networkx for plotting node positions and stress reduction.

## Folder Structure

```
.
├── main.py                      # Entry point of the project
├── read_csvfile.py              # Read multiple CSV sources
├── data_processing.py           # Clean and classify raw data
├── data_to_graph.py             # Convert data into graph structures
├── Chen_Shih_Liang_method_data.py # Historical hypothesis import method
├── directed_mds.py              # Core directional MDS implementation
├── mds_sklearn.py               # Scikit-learn MDS implementation
├── mds_stress_majorization.py  # Custom stress majorization method
├── plotting.py                  # Graph and stress curve visualization
└── 07林昀翰專題研究報告書.pdf      # Full research paper (Traditional Chinese)
```

## How to Run

### Requirements

- Python 3.8+
- numpy
- scipy
- matplotlib
- networkx
- scikit-learn

### Execution

To run the full directional MDS reconstruction:

```bash
python main.py
```

This will load data from processed CSV files and perform reconstruction based on directional constraints extracted from historical texts.

Final output includes:

- Node coordinates of Han-era countries  
- Graph layout visualization (if `plotting()` is enabled)  
- Stress reduction log over iterations  

## Research Result Summary

| Method                        | Stress(X) Value |
|------------------------------|-----------------|
| Method 1: Scikit-MDS         | 1.7 × 10⁹       |
| Method 2: Stress Majorization| 5.0 × 10⁸       |
| Method 3: Unit Model         | 5.5 × 10⁴       |
| Method 4: Directional MDS    | **3.1 × 10⁴**   |

The fourth method, combining directional and distance constraints, yielded the most accurate and lowest stress reconstruction.

## Acknowledgements

- Prof. Tsung-Han Tsai, Academia Sinica  
- Mr. Wei-Li Pan, Jianguo High School  
- Chen Shih-Liang’s historical metric hypothesis  
- Gansner et al., 2004; Wang et al., 2018 for MDS theory  
