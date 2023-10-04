def permute (a, idx):
    hi = len(a)
    if idx == hi:
        print(a)
    else: 
        for i in range(idx, hi):
            a[idx], a[i] = a[i], a[idx]
            permute(a, idx+1)
            a[idx], a[i] = a[i], a[idx]


def main():
    a = ['A', 'B', 'C']
    permute (a, 0)