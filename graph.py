import pandas as pd
import matplotlib.pyplot as plt

# Load results
df = pd.read_csv("results.csv")

# Build pairing label
df["pairing"] = df["styleA"] + "-" + df["styleB"]

# Make x positions for grouped bars
x = range(len(df))

# Breakup probabilities: A vs B vs no one
plt.figure()
width = 0.25

plt.bar([i - width for i in x], df["pALeaves"], width, label="P(A leaves)")
plt.bar(x,                           df["pBLeaves"], width, label="P(B leaves)")
plt.bar([i + width for i in x], df["pNoOneLeaves"], width, label="P(no one leaves)")

plt.xticks(x, df["pairing"], rotation=45, ha="right")
plt.ylabel("Probability")
plt.title("Breakup outcomes by attachment pairing")
plt.legend()
plt.tight_layout()
plt.savefig("breakup_probabilities.png")

# False breakup vs staying in bad relationship
plt.figure()

width = 0.35
plt.bar([i - width/2 for i in x], df["pFalseBreakup"], width, label="P(false breakup)")
plt.bar([i + width/2 for i in x], df["pStayBad"],      width, label="P(stay in bad relationship)")

plt.xticks(x, df["pairing"], rotation=45, ha="right")
plt.ylabel("Probability")
plt.title("Misaligned outcomes by attachment pairing")
plt.legend()
plt.tight_layout()
plt.savefig("misaligned_outcomes.png")

# Belief accuracy (MSE vs true C)
plt.figure()

width = 0.25
plt.bar([i - width/2 for i in x], df["mseA"], width, label="MSE A")
plt.bar([i + width/2 for i in x], df["mseB"], width, label="MSE B")

plt.xticks(x, df["pairing"], rotation=45, ha="right")
plt.ylabel("Mean squared error")
plt.title("Belief accuracy by attachment pairing")
plt.legend()
plt.tight_layout()
plt.savefig("belief_accuracy_mse.png")

# Leave timing
plt.figure()

width = 0.25
plt.bar([i - width/2 for i in x], df["avgLeaveRoundA"], width, label="A leave round")
plt.bar([i + width/2 for i in x], df["avgLeaveRoundB"], width, label="B leave round")

plt.xticks(x, df["pairing"], rotation=45, ha="right")
plt.ylabel("Round (1–20)")
plt.title("Average leave timing by attachment pairing")
plt.legend()
plt.tight_layout()
plt.savefig("leave_timing.png")

# Average experienced signal
plt.figure()

width = 0.25
plt.bar([i - width/2 for i in x], df["avgSignalA"], width, label="Avg signal to A")
plt.bar([i + width/2 for i in x], df["avgSignalB"], width, label="Avg signal to B")

plt.xticks(x, df["pairing"], rotation=45, ha="right")
plt.ylabel("Average signal")
plt.title("Average experienced signal by attachment pairing")
plt.legend()
plt.tight_layout()
plt.savefig("avg_signals.png")

print("Saved figures:")
print("  breakup_probabilities.png")
print("  misaligned_outcomes.png")
print("  belief_accuracy_mse.png")
print("  leave_timing.png")
print("  avg_signals.png")