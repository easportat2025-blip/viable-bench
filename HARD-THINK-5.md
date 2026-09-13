# HARD-THINK-5 (tư duy nhiều bước có kiểm chứng; chấm tay 0-4/câu)

## Quy tắc chạy
- Chat mới mỗi câu, temp 0.7, thinking ON.
- Không paste đáp án/keys vào đề (giữ dấu tiếng Việt khi paste!).
- Chấm: đúng kết luận + lập luận kiểm tra được (xem check-points).

---

## T1 — Markov: chờ đợi mẫu HTH (xác suất)
Tung một đồng xu công bằng, độc lập, cho đến khi lần đầu xuất hiện mẫu HTH liên tiếp.
Tính kỳ vọng số lần tung. Lập trạng thái + hệ phương trình rõ ràng.
(Không dùng giả định các cửa sổ 3-lần-tung độc lập.)

**Key:** E = 10 (ĐÃ SỬA TỪ 8 NGÀY 2026-09-14: model tự giải ra 10, verify 2 cách — Markov + Conway borders (HTH có border H dài 1 nên E=2^3+2^1=10); HHT mới là 8). Trạng thái: {} (0 khớp), {H} (1), {HT} (2), {HTH} (0, hút). E0 = 1 + 0.5*E1 + 0.5*E0; E1 = 1 + 0.5*E1 + 0.5*E2; E2 = 1 + 0.5*0 + 0.5*E0 (HTT về 0). Giải: E0=10.
**Check:** có trạng thái đúng (đặc biệt từ HTT về 0 chứ không về 1) + hệ 3 phương trình + E=10. Bẫy window-independence phải nói rõ.

## T2 — Lịch tác vụ (tối ưu + chứng minh)
1 máy, không ngắt việc. 4 việc (sẵn sàng, xử lý): A(0,3) B(1,1) C(2,2) D(3,1).
Mục tiêu: tối thiểu tổng thời điểm hoàn thành. Được để máy rảnh chủ động.
Tìm 1 lịch tối ưu + chứng minh tối ưu (không mặc định máy làm ngay khi có việc).

**Key:** Chạy A(0-3): xong A=3. B sẵn sàng t=1 chờ đến 3. Sau t=3 còn B,C,D với release<=3 hết -> SPT: B(1),D(1),C(2) -> thứ tự B,D,C. Tính: B(3-4)=4, D(4-5)=5, C(5-7)=7: tổng A+B+D+C = 3+4+5+7 = 19. Chứng minh: A phải chạy từ 0 (dời A chỉ tăng tổng); lịch A,B,D,C = 19 tối ưu (thử A,B,C,D = 20; chèn B trước A = 22). (Để máy rảnh không giúp vì A(0) sẵn sàng ngay.)
**Check:** phải xét SPT sau A (B,D trước C) + chứng minh A-chạy-ngay + tổng 19. Đáp án chỉ "20" mà không xét B,D,C là thiếu.

## T3 — Đoạn con ngắn nhất tổng >= K (thuật toán + chứng minh)
Mảng số nguyên (có thể âm). Tìm độ dài nhỏ nhất của đoạn con liên tiếp, không rỗng, tổng >= K.
1. Vì sao sliding window thường SAI (kể cả biến thể mở rộng phải)?
2. Phản ví dụ cụ thể.
3. Thuật toán O(n): tổng tiền tố + deque đơn điệu (giảm dần theo prefix).
4. Chứng minh 2 quy tắc loại deque an toàn (loại trái khi tìm được ứng viên tốt hơn; loại phải để giữ đơn điệu).
5. Không tồn tại -> trả về gì (quy ước rõ ràng, vd -1).

**Key:** VD sạch: nums=[1,2,-3,4], K=4. Sliding window (mở rộng phải, thu hẹp trái khi tổng>=K): start=0: end=0..3 tổng=4>=K ghi dài 4, thu hẹp start=1 tổng=3<4, hết mảng. Đáp án 4 — SAI (đáp án [4] dài 1). Nguyên nhân: số âm phá tính đơn điệu (thu hẹp trái không bảo toàn tối ưu).
**Check:** VD đúng + giải thích nguyên nhân (số âm phá tính đơn điệu) + deque 2 quy tắc có chứng minh + quy ước -1.

## T4 — Linearizability (đồng thời)
Thanh ghi ban đầu 0. Lịch sử: W1=write(1) [t=1,4]; R1=read->[0] [t=2,3]; W2=write(2) [t=5,6]; R2=read->[1] [t=4.5,7].
1. Có linearizable không? Đưa thứ tự + điểm tuyến tính hoá khả dĩ.
2. Nếu R2 trả về 0 thì sao?
3. Vì sao thứ tự trả về != thứ tự tuyến tính hoá (nói rõ).

**Key:** 1. CÓ: R1 đọc 0 trong [2,3] → điểm R1 trước W1 (W1 [1,4] overlap R1 [2,3]: chọn lin(R1) < lin(W1) OK vì overlap). R2 đọc 1 trong [4.5,7]: lin(W1) < lin(R2), lin(W2)? W2 [5,6] overlap R2: R2 đọc 1 (giá trị W1) → lin(R2) trước lin(W2). Thứ tự: R1, W1, R2, W2 (kiểm tra real-time: lin(R1)∈[2,3], lin(W1)∈[1,4]: chọn 2.5 < 3 ✓; lin(R2)∈[4.5,7] > 3 ✓; lin(W2)∈[5,6] > lin(R2)? chọn lin(R2)=4.7 < 5 ✓). Đọc: R1 trước W1 → 0 ✓; R2 sau W1 trước W2 → 1 ✓. Linearizable.
2. R2=0: cần lin sau W1? R2 đọc 0 → lin(R2) trước lin(W1). Nhưng R1 đọc 0 trước/song song... real-time: R1 kết thúc t=3, R2 bắt đầu 4.5 → lin(R1) < lin(R2). Cả 2 đọc 0, W1 viết 1 trong [1,4]: lin(W1) phải sau lin(R2) (để R2 đọc 0) → lin(W1) > 4.5, trong [1,4]?? 4.5 > 4 VÔ LÝ → không linearizable. (W1 kết thúc t=4 < R2 bắt đầu 4.5 nên W1 phải trước R2.)
3. Vì: lin point chỉ cần nằm trong interval, không phải lúc return; op kết thúc muộn vẫn có thể lin sớm (nếu overlap cho phép).
**Check:** câu 1 đúng + câu 2 chỉ ra mâu thuẫn real-time W1[1,4] vs R2-start-4.5 + câu 3 giải thích interval.

## T5 — Va chạm băm 64-bit (công thức + xấp xỉ + chặn)
1M định danh ngẫu nhiên độc lập, đều, không gian 64-bit.
1. Công thức CHÍNH XÁC P(>=1 va chạm).
2. Xấp xỉ số.
3. Tìm b (nguyên, nhỏ nhất) để P(va chạm) <= 1e-12 (điều kiện: không gian 2^b, 1M định danh), dùng chặn hợp hoặc đánh giá chặt.
4. Nêu rõ kết luận nào xấp xỉ / bảo đảm.

**Key:** 1. P = 1 - (2^64)!/((2^64-1e6)! (2^64)^1e6) = 1 - prod_{i=0}^{n-1}(1-i/N), N=2^64, n=1e6.
2. ≈ n(n-1)/(2N) ≈ 1e12/(2*1.8e19) ≈ 2.7e-8.
3. Chặn hợp: P(∪Aij) <= C(n,2)/2^b ≈ 5e11/2^b <= 1e-12 → 2^b >= 5e23 → b >= log2(5e23) ≈ 78.7 → b=79. (Union-bound cho upper → b=79 bảo đảm.)
4. (2) xấp xỉ (Poisson/exponential approx); (1) chính xác; (3) bảo đảm (upper-bound).
**Check:** công thức tích đúng + số 2.7e-8 + b=79 với lập luận union-bound + phân biệt approx/guarantee.
