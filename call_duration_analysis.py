import os
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

def analyze_call_durations(call_data, target_duration=None):
    """ Analyzes call duration distributions and checks SLA compliance."""
    # Ensure data is a numpy array for vectorized operations
    call_data = np.asarray(call_data)
    mean_dur, std_dur = np.mean(call_data), np.std(call_data)
    
    # Setup visualizations: Histogram (left) and Q-Q plot (right)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
    
    # Plot histogram with an overlaid normal distribution curve
    ax1.hist(call_data, bins=30, density=True, alpha=0.7)
    x = np.linspace(*ax1.get_xlim(), 100)
    ax1.plot(x, stats.norm.pdf(x, mean_dur, std_dur), 'k', linewidth=2)
    ax1.set(title='Distribution of Call Durations', xlabel='Duration (minutes)', ylabel='Frequency')
    
    # Plot Q-Q plot to visually verify normality
    stats.probplot(call_data, dist="norm", plot=ax2)
    ax2.set_title('Q-Q Plot of Call Durations')
    
    # Calculate percentage of data within 1, 2, and 3 standard deviations
    abs_dev = np.abs(call_data - mean_dur)
    results = {
        'mean': mean_dur,
        'std': std_dur,
        'within_1_std': np.mean(abs_dev <= std_dur),
        'within_2_std': np.mean(abs_dev <= 2 * std_dur),
        'within_3_std': np.mean(abs_dev <= 3 * std_dur)
    }
    
    # Calculate probability of exceeding the SLA target using the survival function (sf)
    if target_duration is not None:
        results['probability_exceed_target'] = stats.norm.sf((target_duration - mean_dur) / std_dur)
    
    return results

def calculate_staffing_needs(mean_dur, calls_per_hour, target_occupancy=0.85):
    """Calculates minimum agents required using a simplified Erlang C model."""
    return int(np.ceil(calls_per_hour / ((60 / mean_dur) * target_occupancy)))

# Generate mock normally distributed call data (mean=8m, std=2m)
np.random.seed(42)  
call_durations = np.random.normal(loc=8, scale=2, size=1000)  

# Run analysis with a 10-minute Service Level Agreement (SLA) target
results = analyze_call_durations(call_durations, target_duration=10)
staff_needed = calculate_staffing_needs(results['mean'], calls_per_hour=30)

# Output numerical results
for k, v in results.items():
    print(f"{k.replace('_', ' ').title()}: {v:.4f}")
print(f"Agents Needed: {staff_needed}")

# Create output directory, save the plots, and display them
os.makedirs('presentations', exist_ok=True)
plt.tight_layout()
plt.savefig('presentations/call_durations_analysis.png', dpi=300)
plt.show()
