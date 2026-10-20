# Alvin Kim | Set A | ACIT1515
KB = 1024
MB = 1048576
GB = 1073741824

num_entries = int(input("Please enter the number of entries per second: "))
entry_size = int(input("Please enter the average number of bytes per entry: "))

kb_size = ((num_entries * entry_size) / KB) * 60
mb_size = ((num_entries * entry_size) / MB) * 60 * 60
gb_size = ((num_entries * entry_size) / GB) * 60 * 60 * 24

print("Storage Estimates")
print(f"Per minute: {kb_size}KB")
print(f"Per hour: {mb_size}MB")
print(f"Per day: {gb_size}GB")