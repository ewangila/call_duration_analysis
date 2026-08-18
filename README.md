# Call Duration Analysis – Normal Distribution & Staffing

Analyzes call-center call durations assuming a normal distribution, checks Service Level Agreement (SLA) compliance, and estimates the minimum number of agents required using a simplified Erlang-C model.

## Overview

This project generates mock call duration data (mean = 8 minutes, σ = 2 minutes) and performs the following:

- Visual inspection of the distribution (histogram + normal PDF overlay)
- Q-Q plot to assess normality
- Calculation of the percentage of calls within 1σ, 2σ, and 3σ
- Probability of exceeding a 10-minute SLA target
- Simple staffing calculation based on call volume and target occupancy

## Features

- Histogram with overlaid normal distribution curve
- Quantile-Quantile (Q-Q) plot for normality check
- Empirical coverage within 1, 2, and 3 standard deviations
- SLA breach probability using the survival function
- Agent staffing estimate using a simplified Erlang-C formula

## Tech Stack

- Python 3
- NumPy
- SciPy
- Matplotlib

## Installation

```bash
pip install -r requirements.txt
