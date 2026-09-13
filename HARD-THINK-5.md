# HARD-THINK-5 (tu duy nhieu buoc co kiem chung; cham tay 0-4/cau)

## Quy tac chay
- Chat moi moi cau, temp 0.7, thinking ON.
- Khong paste dap an/keys vao de.
- Cham: dung ket luan + lap luan kiem tra duoc (xem check-points).

---

## T1 — Markov: cho doi mau HTH (xac suat)
Tung dong xu cong bang doc lap cho den khi lan dau xuat hien mau HTH lien tiep.
Tinh ky vong so lan tung. Lap trang thai + he phuong trinh ro rang.
(Khong dung gia dinh cac cua so 3-lan-tung doc lap.)

**Key:** E = 10 (DA SUA TU 8 NGAY 2026-09-14: model tu giai ra 10, verify 2 cach — Markov + Conway borders (HTH co border H dai 1 nen E=2^3+2^1=10); HHT moi la 8). Trang thai: {} (0 khop), {H} (1), {HT} (2), {HTH} (0, hut). E0 = 1 + 0.5*E1 + 0.5*E0; E1 = 1 + 0.5*E1 + 0.5*E2; E2 = 1 + 0.5*0 + 0.5*E0 (HTT ve 0). Giai: E0=10.
**Check:** co trang thai dung (dac biet tu HTT ve 0 chu khong ve 1) + he 3 phuong trinh + E=8. Bay window-independence phai noi ro.

## T2 — Lich tac vu (toi uu + chung minh)
1 may, khong ngat viec. 4 viec (san sang, xu ly): A(0,3) B(1,1) C(2,2) D(3,1).
Muc tieu: toi thieu tong thoi diem hoan thanh. Duoc de may ranh chu dong.
Tim 1 lich toi uu + chung minh toi uu (khong mac dinh may lam ngay khi co viec).

**Key:** Thu A(0-3): xong A=3. B san sang t=1 cho den 3. Chay B(3-4), C(4-6), D(6-7): tong = 3+4+6+7 = 20. Chung minh: A phai chay tu 0 (doi A chi tang tong); sau t=3 con B,C,D voi release<=3 het -> SPT: B(1),C(2),D(1) -> thu tu B,D,C? Tinh: B(3-4)=4, D(4-5)=5, C(5-7)=7: tong A+B+D+C = 3+4+5+7 = 19 < 20! Vay lich toi uu: A,B,D,C = 19. (De may ranh khong giup vi A(0) san sang ngay.)
**Check:** phai xet SPT sau A (B,D truoc C) + chung minh A-chay-ngay + tong 19. Dap an chi "20" ma khong xet B,D,C la thieu.

## T3 — Doan con ngan nhat tong >= K (thuat toan + chung minh)
Mang so nguyen (co the am). Tim do dai nho nhat cua doan con lien tiep, khong rong, tong >= K.
1. Vi sao sliding window thuong SAI (ke ca bien the mo rong phai)?
2. Phan vi du cu the.
3. Thuat toan O(n): tong tien to + deque don dieu (giam dan theo prefix).
4. Chung minh 2 quy tac loai deque an toan (loai trai khi tim duoc ung vien tot hon; loai phai de giu don dieu).
5. Khong ton tai -> tra ve gi (quy uoc ro rang, vd -1).

**Key:** VD sach: nums=[1,2,-3,4], K=4. Sliding window (mo rong phai, thu hep trai khi tong>=K): start=0: end=0..3 tong=4>=K ghi dai 4, thu hep start=1 tong=3<4, het mang. Dap an 4 — SAI (dap an [4] dai 1). Nguyen nhan: so am pha tinh don dieu (thu hep trai khong bao toan toi uu).
**Check:** VD dung + giai thich nguyen nhan (so am pha tinh don dieu) + deque 2 quy tac co chung minh + quy uoc -1.

## T4 — Linearizability (dong thoi)
Thanh ghi ban dau 0. Lich su: W1=write(1) [t=1,4]; R1=read->[0] [t=2,3]; W2=write(2) [t=5,6]; R2=read->[1] [t=4.5,7].
1. Co linearizable khong? Dua thu tu + diem tuyen tinh hoa kha di.
2. Neu R2 tra ve 0 thi sao?
3. Vi sao thu tu tra ve != thu tu tuyen tinh hoa (noi ro).

**Key:** 1. CO: R1 doc 0 trong [2,3] → diem R1 truoc W1 (W1 chua xong luc R1 bat dau? W1 [1,4] overlap R1 [2,3]: chon lin(R1) < lin(W1) OK vi overlap). R2 doc 1 trong [4.5,7]: lin(W1) < lin(R2), lin(W2)? W2 [5,6] overlap R2: R2 doc 1 (gia tri W1) → lin(R2) truoc lin(W2). Thu tu: R1, W1, R2, W2 (kiem tra real-time: R1[2,3]<W1? lin phai trong interval: lin(R1)∈[2,3], lin(W1)∈[1,4]: chon 2.5 < 3 ✓; lin(R2)∈[4.5,7] > 3 ✓; lin(W2)∈[5,6] > lin(R2)? chon lin(R2)=4.7 < 5 ✓). Doc: R1 truoc W1 → 0 ✓; R2 sau W1 truoc W2 → 1 ✓. Linearizable.
2. R2=0: can lin sau W1? R2 doc 0 → lin(R2) truoc lin(W1). Nhung R1 doc 0 truoc/song song... real-time: R1 ket thuc t=3, R2 bat dau 4.5 → lin(R1) < lin(R2). Ca 2 doc 0, W1 viet 1 trong [1,4]: lin(W1) phai sau lin(R2) (de R2 doc 0) → lin(W1) > 4.5, trong [1,4]?? 4.5 > 4 VO LY → khong linearizable. (W1 ket thuc t=4 < R2 bat dau 4.5 nen W1 phai truoc R2.)
3. Vi: lin point chi can nam trong interval, khong phai luc return; op ket thuc muon van co the lin som (neu overlap cho phep).
**Check:** cau 1 dung + cau 2 chi ra mau thuan real-time W1[1,4] vs R2-start-4.5 + cau 3 giai thich interval.

## T5 — Va cham bam 64-bit (cong thuc + xap xi + chan)
1M dinh danh nga nhien doc lap, deu, khong gian 64-bit.
1. Cong thuc CHINH XAC P(>=1 va cham).
2. Xap xi so.
3. Tim b (nguyen, nho nhat) de P(va cham) <= 1e-12 (dieu kien: khong gian 2^b, 1M dinh danh), dung chan hop hoac danh gia chat.
4. Neu ro ket luan nao xap xi / bao dam.

**Key:** 1. P = 1 - (2^64)!/((2^64-1e6)! (2^64)^1e6) = 1 - prod_{i=0}^{n-1}(1-i/N), N=2^64, n=1e6.
2. ≈ n(n-1)/(2N) ≈ 1e12/(2*1.8e19) ≈ 2.7e-8.
3. Chan hop: P(∪Aij) <= C(n,2)/2^b ≈ 5e11/2^b <= 1e-12 → 2^b >= 5e23 → b >= log2(5e23) ≈ 78.7 → b=79. (Danh gia chat hon: 1-exp(-x)>=... dung lower-bound? Union-bound cho upper → b=79 bao dam.)
4. (2) xap xi (Poisson/exponential approx); (1) chinh xac; (3) bao dam (upper-bound).
**Check:** cong thuc tich dung + so 2.7e-8 + b=79 voi lap luan union-bound + phan biet approx/guarantee.
