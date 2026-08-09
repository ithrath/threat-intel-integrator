import requests

print("Fetching REAL IPs...")
print("="*40)

# This URL ALWAYS returns real IPs
url = "https://check.torproject.org/torbulkexitlist"

response = requests.get(url)
ips = response.text.strip().split('\n')

print(f"\n✅ Found {len(ips)} Tor exit node IPs!")
print("\n🔴 Here are the first 10 IPs:\n")

for i, ip in enumerate(ips[:10], 1):
    print(f"   {i}. {ip}")

# Save to file
with open('real_ips.txt', 'w') as f:
    f.write('\n'.join(ips))

print("\n" + "="*40)
print(f"✅ All {len(ips)} IPs saved to real_ips.txt")