#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd

# Read the data from file
data = pd.read_csv('per-release-china-percent.txt',
                   sep='\\s+', skiprows=1,
                   names=['date', 'numeric-release', 'total-contributor-number',
                          'china-contributor-number', 'china-contributor-percent',
                          'total-patch-number', 'china-patch-number', 'china-patch-percent'])

# Treat kernel versions as categorical text and sort reverse-chronologically by date
data = data.sort_values('date', ascending=False)
labels = data['numeric-release'].astype(str).tolist()
positions = list(range(len(labels)))

# Create the figure with white background for better readability
plt.figure(figsize=(16, 12), facecolor='white')
ax = plt.gca()
ax.set_facecolor('white')

# Create horizontal bar chart with improved styling
plt.barh(positions, data['china-contributor-number'], color='#e74c3c', height=0.8, edgecolor='black', linewidth=0.5)

# Add title and labels
plt.title('Chinese Developers by Kernel Version', fontsize=20, fontweight='bold', pad=20)
plt.xlabel('Number of Chinese Developers', fontsize=16, labelpad=15)
plt.ylabel('Kernel Version', fontsize=16, labelpad=15)

# Show 1 of every 2 y labels for better readability
plt.yticks(positions[::2], labels[::2], fontsize=12)
plt.xticks(fontsize=14)

# Add grid for better readability
plt.grid(axis='x', alpha=0.4, linestyle='--', linewidth=0.8)
plt.gca().set_axisbelow(True)  # Place grid below bars

# Ensure time direction is from bottom to top (earliest at bottom)
plt.gca().invert_yaxis()

# Add data labels for key values
for i, value in enumerate(data['china-contributor-number']):
    if i % 2 == 0:  # Only show labels for visible yticks
        plt.text(value + 5, i, f'{value}', fontsize=10, va='center', fontweight='bold', color='#2c3e50')

# Beautify axes
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)

# Adjust layout
plt.tight_layout(pad=2.0)

# Save with white background
img_path = 'chinese_developers.png'
plt.savefig(img_path, dpi=300, bbox_inches='tight')
print(f"Figure saved as {img_path}")

# Second figure: patches per release with improved styling
plt.figure(figsize=(16, 12), facecolor='white')
ax = plt.gca()
ax.set_facecolor('white')

# Create horizontal bar chart with improved styling
plt.barh(positions, data['china-patch-number'], color='#3498db', height=0.8, edgecolor='black', linewidth=0.5)

# Add title and labels
plt.title('Chinese Developers Patches by Kernel Version', fontsize=20, fontweight='bold', pad=20)
plt.xlabel('Number of Patches from Chinese Developers', fontsize=16, labelpad=15)
plt.ylabel('Kernel Version', fontsize=16, labelpad=15)

# Show 1 of every 2 y labels for better readability
plt.yticks(positions[::2], labels[::2], fontsize=12)
plt.xticks(fontsize=14)

# Add grid for better readability
plt.grid(axis='x', alpha=0.4, linestyle='--', linewidth=0.8)
plt.gca().set_axisbelow(True)  # Place grid below bars

# Ensure time direction is from bottom to top (earliest at bottom)
plt.gca().invert_yaxis()

# Add data labels for key values
for i, value in enumerate(data['china-patch-number']):
    if i % 2 == 0:  # Only show labels for visible yticks
        plt.text(value + 5, i, f'{value}', fontsize=10, va='center', fontweight='bold', color='#2c3e50')

# Beautify axes
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)

# Adjust layout
plt.tight_layout(pad=2.0)

# Save with white background
img_path = 'chinese_patches.png'
plt.savefig(img_path, dpi=300, bbox_inches='tight')
print(f"Figure saved as {img_path}")

