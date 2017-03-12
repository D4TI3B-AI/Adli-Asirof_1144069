import time
start_time = time.time()
print("menghitung nilai rumus matematika menggunakan bahasa jepang")
a = input("Masukan Nilai 1 : ")
d = input("Masukan Nilai 2 : ")
l = input("Masukan Nilai 3 : ")
i = input("Masukan Nilai 4 : ")

if a =='ichi':
	a=1
if a =='ni':
	a=2
if a =='san':
	a=3
if a =='shi':
	a=4
if a =='go':
	a=5
if a =='roku':
	a=6
if a =='nana':
	a=7
if a =='hachi':
	a=8
if a =='kyuu':
	a=9
if a =='zero':
	a=0

if d =='ichi':
	d=1
if d =='ni':
	d=2
if d =='san':
	d=3
if d =='shi':
	d=4
if d =='go':
	d=5
if d =='roku':
	d=6
if d =='nana':
	d=7
if d =='hachi':
	d=8
if d =='kyuu':
	d=9
if d =='zero':
	d=0

if l =='ichi':
	l=1
if l =='ni':
	l=2
if l =='san':
	l=3
if l =='shi':
	l=4
if l =='go':
	l=5
if l =='roku':
	l=6
if l =='nana':
	l=7
if l =='hachi':
	l=8
if l =='kyuu':
	l=9
if l =='zero':
	l=0

if i =='ichi':
	i=1
if i =='ni':
	i=2
if i =='san':
	i=3
if i =='shi':
	i=4
if i =='go':
	i=5
if i =='roku':
	i=6
if i =='nana':
	i=7
if i =='hachi':
	i=8
if i =='kyuu':
	i=9
if i =='zero':
	i=0

perhitungan = (((a * d)/l) * ((l * i)/a)*a)
print('hasil perhitungan', perhitungan)
print("time : %s detik " % (time.time() - start_time))
