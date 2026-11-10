# Name: Grant Tanski
# Date: 2026-11-10
# Program: Program Help Screen
# Description: Using print statements to simulate a help screen for a tool called "gradebook"

# Output: Title
print("=" * 44)
print("  GRADEBOOK  version 1.0")
print("  A tool for tracking class scores")
print("=" * 44)

# Output: Usage
print("USAGE:")
print("  gradebook [option] [file]")
print()

# Output: Options
print("OPTIONS:")
print("  -a    Add a new score\n  -l    List all scores\n  -r    Print a report\n  -h    Show this help screen")
print()

# Output: Examples
print("EXAMPLES:")
print("  gradebook -1 C:\\BPA\\scores.txt\n  gradebook -a \"Quiz 3\"")
print()

# Output: Footer
print("-" * 44)
print("Tip: options are case sensitive.")
print("-A is not the same as -a.")
print("=" * 44)

print("Debug mode is on.")
