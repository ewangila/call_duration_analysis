# Call Duration Analysis – Normal Distribution & Staffing

Analyzes call-center call durations under a normal distribution assumption, checks SLA compliance, and estimates required agents using a simplified Erlang-C model.

## Features
- Histogram + normal PDF overlay
- Q-Q plot for normality check
- % of calls within 1σ / 2σ / 3σ
- Probability of exceeding 10-minute SLA
- Simple staffing calculation

## Tech Stack
- Python 3, NumPy, SciPy, Matplotlib

## Installation
pip install -r requirements.txt (bash)

## Sample Output
Mean: 8.0066
Std: 1.9622
Within 1 Std: 0.6830
Within 2 Std: 0.9550
Within 3 Std: 0.9970
Probability Exceed Target: 0.1545
Agents Needed: 5

## Visualization
![Call Duration Analysis](presentations/call_durations_analysis.png)

## Project Structure
├── call_duration_analysis.py
├── presentations/call_durations_analysis.png
├── requirements.txt
├── LICENSE
└── README.md

## License
MIT License – see [LICENSE](LICENSE)
