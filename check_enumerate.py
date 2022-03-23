#check_enumerate.py
vals = [10,23,44,55,66,77]
for i, val in enumerate(vals):
    print(f'index={i}->value={val}')

"""
out:
index=0->value=10
index=1->value=23
index=2->value=44
index=3->value=55
index=4->value=66
index=5->value=77
"""
print()
vals2 = [1,2,3,4,5,6]
for i, val in enumerate(vals2):
    print(f'index={i+1}->value={val}')
