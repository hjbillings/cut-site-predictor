# Hannah Billings

sequence = "ACACACACACACACA"
cut_site = "ACAC"
cut_amt = 0
  
for i in range(0, len(sequence)):
    if sequence[i:(len(cut_site)+i)] == cut_site:
        cut_amt += 1
print(cut_amt)

