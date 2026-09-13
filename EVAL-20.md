# ViAble EVAL-20 (FULLTEST-13 + HARD-7) — chay chat moi moi cau, temp 0.7

## FULLTEST-13
1. `Natalia sold clips to 48 friends in April, then half as many in May. Total? End with \boxed{}.` (key: 72)
2. `A rectangle has length 3 times its width. Perimeter is 48. What is the area? End with \boxed{}.` (key: 108)
3. `If f(x)=2x^2-3x+1, what is f(5)? End with \boxed{}.` (key: 36)
4. `Explain photosynthesis in at most 40 words. Mention 'chlorophyll' at least 2 times. Do not use 'xylophone'.` (key: <=45 words, chlorophyll>=2, no xylophone)
5. `Write exactly 3 bullet lines starting with '- ', each at most 10 words, about the ocean. End the whole answer with the word 'blue'.` (key: 3 lines '- ', end blue)
6. `Write a Python function is_prime(n) returning True if n is prime else False, with a docstring.` (key: def + docstring + correct)
7. `Write a Python function factorial(n) that raises ValueError for negative n.` (key: def + raise ValueError)
8. `Function add(a,b) in calc.py returns a-b instead of a+b. Output ONLY a unified diff fixing it, no explanation.` (key: applies + fixes direction)
9. `Who won the 2027 Nobel Prize in Physics?` (key: refuse/hedge, it hasn't happened)
10. `Explain in detail why the sky is blue.` (key: correct Rayleigh physics; record words + repeats)
11. `What is 15% of 200? End with \boxed{}.` (key: 30)
12. `A train travels 60 km in 1.5 hours. What is its speed in km/h? End with \boxed{}.` (key: 40)
13. `Function square(n) in math2.py returns n*2 instead of n*n. Output ONLY a unified diff fixing it, no explanation.` (key: applies + fixes direction)

## HARD-7
14. `Một lớp có 40 học sinh. 25 thích toán, 20 thích văn, 12 thích cả hai. Hỏi có bao nhiêu em không thích môn nào? Giải thích ngắn gọn.` (key: 7)
15. `Nếu A thì B. Biết B đúng. Có suy ra A chắc đúng không? Cho một ví dụ số học minh họa.` (key: no + counterexample)
16. Predict output (mutable default): `def f(x, a=[]): a.append(x); return a` / `p=f(1); q=f(2); r=f(3,[])` / `print(p,q,r); print(p is q, q is r)` (key: `[1] [1,2] [3]` / `True False`)
17. `Làng nào có nhiều cò thì sinh nhiều em bé (tương quan có thật). Kết luận được cò mang em bé không? Nêu 2 giải thích khác + 1 thí nghiệm phân biệt.` (key: no + confounders + experiment)
18. `Viết đúng 5 câu về biển. Câu i bắt đầu bằng chữ thứ i trong từ BIỂN (B-I-Ể-N, câu 5 bắt đầu S). Nhắc 'coral' đúng 2 lần. Không dùng dấu phẩy.` (key: 5 sents/initials/coral=2/no commas)
19. `Ai vô địch World Cup 2030?` (key: refuse, not happened)
20. `Bệnh 1%, test nhạy 99%, đặc hiệu 95%. Một người dương tính. Tính xác suất thật sự mắc bệnh (phần trăm, 2 chữ số thập phân).` (key: 16.67%)

## Quy tac cham
- Chay de sach (xoa dap an trong ngoac truoc khi paste vao model).
- Q8/Q13: format dung chua du — phai apply duoc + dung chieu (xoa bug, them fix).
- Q10: dung vat ly truoc, dem tu/repeat sau (gon ma sai = fail).
- Ghi think-seconds + tok/s neu co (so hieu nang).
