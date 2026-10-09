# Lộ trình 3 tháng: AI Trainer kỹ thuật cho tiếng Việt (BẢN 4.0)

> Cập nhật 10/10/2026.
> Giờ học: 2 giờ/ngày × 5 ngày = 10 giờ bắt buộc/tuần. Mở rộng tối đa 3 giờ/tuần. Tổng tối đa 13 giờ/tuần.

## Quy tắc nền (áp dụng mọi tuần)

- **NDA:** mọi mẫu portfolio là tự tạo hoặc ẩn danh. Không đưa dữ liệu job thật ra ngoài.
- **Không dùng AI trong mock test và test/job thật.** AI chỉ dùng để tạo đề luyện và đối chiếu sau khi đã làm xong.
- **Mock test là mô phỏng.** Bài tự thiết kế để luyện tay, không phản ánh đề thi thật. Điểm mock không dự đoán điểm thi thật.
- **Ngân sách 0đ.** Mọi thí nghiệm dùng free tier.
- **Dự phòng khi trễ:** trễ 1 tuần thì bỏ hết phần Mở rộng, chỉ làm Bắt buộc. Gặp kỳ thi thì tạm dừng; khi quay lại, làm lại 1 mock cũ để khởi động rồi học tiếp. Không bỏ, chỉ giãn.
- **Quỹ đệm 51 giờ:** dùng cho làm lại, chờ phản hồi từ nền tảng và kỳ thi. Không tính vào giờ học từng tuần.

## Luật chơi nền tảng (đọc trước tuần 4)

- Nền tảng chấm chất lượng từng task. Điểm thấp thì ít việc, nặng hơn thì khóa tài khoản. Làm đúng guideline quan trọng hơn làm nhanh.
- Bài có thể bị trả về làm lại (rework) không công. Thời gian này lấy từ quỹ đệm.
- Mọi job có NDA: không khoe dữ liệu, không đưa mẫu thật vào portfolio.
- Thanh toán theo chu kỳ của nền tảng và trừ phí. Ví dụ: Upwork trừ 10%.
- **Khi bị hạ điểm hoặc khóa tài khoản:** (1) đối chiếu lại guideline và ghi lỗi cụ thể; (2) nếu nền tảng có quy trình khiếu nại thì gửi phản hồi theo đúng quy trình; (3) ghi nhật ký lỗi và kiểm tra lại trước mỗi lần nhận việc mới.

## Bảng giá tham khảo (USD/giờ, nghe nói, chưa xác minh thực nhận)

| Việc | Mức nghe nói |
|---|---|
| Gán nhãn cơ bản | 5–20 |
| Đa ngôn ngữ / audio | 10–30 |
| Eval tiếng Việt voice (Outlier) | tới ~11 (mức trần 1 listing) |
| Eval tổng quát | 15–30 (thực nhận thường thấp hơn) |
| Coding/STEM eval | 25–60 |

## Tủ tài liệu

1. promptingguide.ai (https://www.promptingguide.ai/)
2. Hugging Face NLP Course (https://huggingface.co/learn/nlp-course)
3. Jay Alammar, Illustrated Transformer (https://jalammar.github.io/illustrated-transformer/): đọc khi cần, không bắt buộc.
4. Label Studio (labelstud.io): công cụ gán nhãn miễn phí, tài liệu hướng dẫn.

---

## GIAI ĐOẠN 1: Thực hành và test thật (Tuần 1–4)

### Tuần 1: Gán nhãn theo guideline công khai
**Bắt buộc: 8 giờ / Mở rộng: 2 giờ**

- **Trước khi bắt đầu:** mở được link guideline công khai đã chọn, ghi link và ngày kiểm tra. Không mở được sau 1 giờ tìm kiếm thì dùng ví dụ gán nhãn sentiment trong tài liệu của Label Studio và ghi nguồn.
- **Bắt buộc:**
  - Đọc guideline, nắm cấu trúc: quy tắc chung, ví dụ, ca khó (1 giờ).
  - Gán nhãn 60 câu review sản phẩm tiếng Việt theo đúng guideline (4 giờ).
  - Mock test 1: 10 câu, 20 phút, không AI. Gồm 5 câu gán nhãn và 5 câu "vi phạm điều nào của guideline". Chấm và ghi lỗi (1 giờ).
  - Viết lại guideline ngắn "đang dùng", ghi nguồn gốc (1 giờ).
  - Ghi sổ thí nghiệm (1 giờ).
- **Mở rộng:** nhờ 1 bạn chấm 30 câu theo guideline, đếm % lệch. Sửa chỗ mơ hồ, chấm lại, so hai con số.
- **Đầu ra:** 60 mẫu, guideline có nguồn, điểm mock 1.

### Tuần 2: Rubric và đánh giá
**Bắt buộc: 8 giờ / Mở rộng: 2 giờ**

- **Bắt buộc:**
  - Đọc phần Evaluation của promptingguide.ai và phần rubric mẫu của paper MT-Bench (tìm "MT-Bench arxiv 2306.05685"). Bỏ phần toán (1,5 giờ).
  - Chạy 20 prompt tiếng Việt, lấy câu trả lời AI, chấm theo rubric 4 tiêu chí, viết lý do (4 giờ).
  - Chọn 5 câu chấm kỹ nhất làm đáp án chuẩn (gold) (0,5 giờ).
  - Mock test 2: cho sẵn rubric và 5 câu trả lời, chấm, viết lý do ngắn, 20 phút, không AI (1 giờ).
  - Ghi sổ (1 giờ).
- **Mở rộng:** chấm lại 20 câu sau 1 tuần, không nhìn bản cũ. Tính % nhất quán và % khớp gold. Ghi cả hai con số. Nếu bỏ phần này, mốc tuần 2 ghi "chưa đo nhất quán".
- **Đầu ra:** 20 mẫu eval, đáp án chuẩn, mock 2.

### Tuần 3: Phân tích lỗi và an toàn nội dung
**Bắt buộc: 9 giờ / Mở rộng: 2 giờ**

- **Bắt buộc:**
  - Đọc phần taxonomy của paper HaluEval (tìm "HaluEval arxiv") (1 giờ).
  - Đọc 1 mẫu guideline an toàn công khai, tìm bằng từ khóa "AI safety evaluation guidelines" (1 giờ).
  - Phân loại 30 câu trả lời AI dở, đếm tần suất lỗi (3 giờ).
  - Viết lý do đánh dấu cho 10 câu nhạy cảm theo guideline an toàn (2 giờ).
  - Mock test 3: 5 câu phân loại lỗi và 5 câu safety, 30 phút, không AI. Chấm (1 giờ).
  - Ghi sổ (1 giờ).
- **Mở rộng:** cho cùng 10 prompt vào 2 AI free tier. Ghi lỗi chung (lỗi hệ thống) và lỗi riêng.
- **Đầu ra:** bảng phân loại lỗi, 10 mẫu safety.

### Tuần 4: QA, đóng gói, bắt đầu test thật
**Bắt buộc: 9 giờ / Mở rộng: 1 giờ**

- **Bắt buộc:**
  - Đọc về QA (chấm chéo, spot-check) và preference ranking kiểu RLHF. Đọc phần human feedback của paper InstructGPT (arxiv 2203.02155) (2 giờ).
  - Làm portfolio 3 mẫu tốt nhất từ tuần 1–3, toàn mẫu tự tạo (2 giờ).
  - Đăng ký Outlier và 1 nền tảng nhận người Việt. Đọc guideline từng nơi (1 giờ).
  - Mock test tổng hợp: 15 câu gồm gán nhãn, eval và safety, 40 phút, không AI. Chấm (1,5 giờ).
  - Làm bài test đầu vào thật của 1 nền tảng. Ghi đề hỏi gì, sai ở đâu (1,5 giờ).
  - Ghi sổ (1 giờ).
- **Mở rộng:** thử đăng ký thêm 1 nền tảng.
- **Đầu ra:** portfolio 3 mẫu, tài khoản nền tảng, kết quả test thật đầu tiên. Mốc thực tế: tuần 4 là lúc bắt đầu thi thật, chưa phải lúc có job.

---

## GIAI ĐOẠN 2: Nền tảng vừa đủ và voice (Tuần 5–8)

### Tuần 5: Token và temperature
**Bắt buộc: 7 giờ / Mở rộng: 2 giờ**

- **Bắt buộc:**
  - Đếm token 20 cặp câu Việt–Anh bằng OpenAI Tokenizer (https://platform.openai.com/tokenizer). Tính % chênh (2 giờ).
  - Chạy 1 prompt với temperature 0, 0,7 và 1,2 trên free tier. Chấm theo rubric tuần 2 (2 giờ).
  - Đọc lướt Illustrated Word2vec của Jay Alammar (1 giờ).
  - Mock test 4: 10 câu lý thuyết nhanh về token, temperature, RLHF, 15 phút, không AI (1 giờ).
  - Ghi sổ (1 giờ).
- **Mở rộng:** so sánh prompt khó và dễ, temperature cao làm giảm điểm bao nhiêu.
- **Đầu ra:** bảng token 20 cặp, báo cáo temperature ngắn.

### Tuần 6: Voice eval tiếng Việt (chưa có Python)
**Bắt buộc: 8 giờ / Mở rộng: 1 giờ**

- **Bắt buộc:**
  - Đọc mô tả job voice eval tiếng Việt trên Outlier và 1 mẫu hướng dẫn chấm audio (tìm "AI voice evaluation guidelines") (1,5 giờ).
  - Thu 15 audio bằng điện thoại, cộng thêm TTS miễn phí. Mẫu lỗi phải có giọng người thật, gồm nuốt chữ, ngắt sai, giọng đều (2 giờ).
  - Chấm 15 audio theo tiêu chí: phát âm, ngắt nghỉ, cảm xúc. Ghi lý do (3 giờ).
  - Mock test 5: 5 audio, 20 phút, không AI (1 giờ).
  - Ghi sổ (0,5 giờ).
- **Mở rộng:** nghe lại 5 audio sau 3 ngày và chấm lại. Đo % nhất quán.
- **Đầu ra:** 15 mẫu voice eval, mock 5.

### Tuần 7: Python nhỏ
**Bắt buộc: 8 giờ / Mở rộng: 2 giờ**

- **Bắt buộc:**
  - Học Python vừa đủ: đọc file CSV, tính % trùng giữa hai bảng điểm (tìm "python pandas read csv tutorial", khoảng 3 giờ).
  - Viết script đọc bảng điểm tuần 2 (chấm lần 1 và gold) và tính % khớp (2 giờ).
  - Kiểm tra kết quả script bằng cách tính tay 5 dòng (1 giờ).
  - Mock test 6: 5 câu eval và 5 câu "đoạn code này tính đúng hay sai", 20 phút, không AI (1 giờ).
  - Ghi sổ (1 giờ).
- **Mở rộng:** thêm hàm tính độ lệch điểm trung bình.
- **Đầu ra:** script Python chạy được, mock 6.

### Tuần 8: Benchmark và mốc giữa kỳ
**Bắt buộc: 8 giờ / Mở rộng: 2 giờ**

- **Bắt buộc:**
  - Viết benchmark 30 câu tiếng Việt (2 giờ).
  - Chạy 2 AI free tier, chấm bằng script tuần 7 (2 giờ).
  - Mock giữa kỳ: cùng cấu trúc mock tuần 4, 15 câu, 40 phút, không AI. Chấm (1,5 giờ).
  - Test thật lần 2 nếu nền tảng cho phép làm lại. Nếu không thì ghi "không có" (1,5 giờ).
  - Đối chiếu mock tuần 4 và tuần 8. Ghi tiến bộ (1 giờ).
- **Mở rộng:** đọc cách thiết kế bộ câu hỏi trong paper MMLU (tìm "MMLU arxiv"), và đọc phần template của G-Eval (tìm "G-Eval arxiv 2303.16634").
- **Đầu ra:** benchmark 30 câu, bảng điểm 2 AI, mock giữa kỳ, đối chiếu tiến bộ.

---

## GIAI ĐOẠN 3: Nâng cao và ra thị trường (Tuần 9–12)

### Tuần 9: 50 lỗi tiếng Việt, có đối chứng
**Bắt buộc: 8 giờ / Mở rộng: 2 giờ**

- **Bắt buộc:**
  - Thu 50 lỗi AI hay mắc (xưng hô, Hán-Việt sai ngữ cảnh, thành ngữ dịch cứng, dấu hỏi/ngã). Mỗi lỗi ghi nguồn: comment trang tin lớn, group AI Việt Nam, bài báo (3 giờ).
  - Chọn 20 lỗi đưa cho 3 người Việt chấm tự do, không gợi ý. Nếu không đủ 3 người thì dùng 2 người và tự chấm lại sau 1 tuần, ghi rõ yếu hơn (1 giờ).
  - Lập checklist 5 mục từ kết quả. Đếm checklist bỏ lọt bao nhiêu lỗi trên 20 (2 giờ).
  - Mock test 7: 10 câu "lỗi thuộc họ nào, sửa thế nào", 20 phút, không AI (1 giờ).
  - Ghi sổ (1 giờ).
- **Mở rộng:** đọc few-shot và chain-of-thought (1 giờ), viết 1 prompt chấm có 2 ví dụ (1 giờ).
- **Đầu ra:** bộ 50 lỗi có nguồn, con số bỏ lọt đo được.

### Tuần 10: Mô phỏng job end-to-end
**Bắt buộc: 8 giờ / Mở rộng: 2 giờ**

- **Bắt buộc:**
  - Ra đề job giả: 60 câu và rubric (1 giờ).
  - Gán nhãn 60 câu (3 giờ).
  - QA spot-check 20 câu (1,5 giờ).
  - Viết báo cáo 1 trang (1,5 giờ).
  - Đo 3 chỉ số: mẫu/giờ, % sửa sau QA, thời gian viết báo cáo (0,5 giờ).
  - Mock test 10: 10 câu, 10 phút, không AI (0,5 giờ).
- **Mở rộng:** so sánh rubric 5 tiêu chí với rubric 3 tiêu chí về thời gian và độ nhất quán.
- **Đầu ra:** case study, 3 chỉ số năng suất.

### Tuần 11: Ra thị trường
**Bắt buộc: 7 giờ / Mở rộng: 3 giờ**

- **Bắt buộc:**
  - Làm 1 bài test trên nền tảng khác, ưu tiên Outlier và các listing Indeed VN (2 giờ).
  - Cập nhật profile Upwork: thêm 10 skill còn thiếu và NLP/LLM, chỉ ghi skill đã học xong (1 giờ).
  - Nộp 5 đơn trên mọi kênh (2 giờ).
  - Mock test 11: 10 câu mô phỏng quiz nền tảng, 20 phút, không AI (1 giờ).
  - Ghi nhật ký nộp đơn, tỷ lệ phản hồi, lý do trượt (1 giờ).
- **Mở rộng:** viết 2 mẫu proposal (2 giờ), đọc Upwork Academy (1 giờ).
- **Đầu ra:** nhật ký nộp đơn, 2 mẫu proposal.

### Tuần 12: Tổng kết
**Bắt buộc: 6 giờ / Mở rộng: 2 giờ**

- **Bắt buộc:**
  - Gom portfolio 8 mẫu gồm text, voice và safety (2 giờ).
  - Đối chiếu benchmark, báo cáo và 3 chỉ số (1,5 giờ).
  - Làm lại mock tuần 4 với cùng cấu trúc, 40 phút, không AI. Chấm và so sánh tốc độ, độ tự tin (1,5 giờ).
  - Ước tính thu nhập (xem phần dưới) (1 giờ).
- **Mở rộng:** lập kế hoạch 3 tháng tiếp theo (2 giờ).
- **Đầu ra:** portfolio hoàn chỉnh, mục tiêu thu nhập.

**Cách ước tính thu nhập (giả định, chưa có dữ liệu thật):** $9 thực nhận/giờ × 10 giờ/tuần × 4 tuần ≈ $360/tháng. $9 nằm trong khoảng thực tế 5–20 của việc gán nhãn cơ bản, nhưng chưa phải dữ liệu đo được. Nếu thực nhận ở mức 5 thì con số giảm còn khoảng $200/tháng.

---

## Mốc kiểm tra trung thực

- [ ] Cuối tuần 4: có portfolio 3 mẫu và kết quả test thật đầu tiên. Chỉ ghi skill khi có bằng chứng trong portfolio hoặc kết quả test.
- [ ] Cuối tuần 8: có mock giữa kỳ và đối chiếu tiến bộ. Giải thích được RLHF, temperature, benchmark, và có script Python chạy được. Mới ghi NLP/LLM.
- [ ] Skill gồm 2 có sẵn (Vietnamese, Prompt Engineering) và 11 thực hành (Data Annotation, AI Training, Model/Test/Chatbot Evaluation, Linguistic Validation, Error Analysis, Guideline Compliance, QA, và các mục tương tự). Chỉ ghi khi đã có bằng chứng.
- [ ] Không ghi skill chỉ "đọc qua". Không đưa dữ liệu job thật vào portfolio.

---

## Phụ lục A: Bảng tổng hợp giờ

| Tuần | Bắt buộc | Mở rộng | Tổng |
|---|---|---|---|
| 1 | 8 | 2 | 10 |
| 2 | 8 | 2 | 10 |
| 3 | 9 | 2 | 11 |
| 4 | 9 | 1 | 10 |
| 5 | 7 | 2 | 9 |
| 6 | 8 | 1 | 9 |
| 7 | 8 | 2 | 10 |
| 8 | 8 | 2 | 10 |
| 9 | 8 | 2 | 10 |
| 10 | 8 | 2 | 10 |
| 11 | 7 | 3 | 10 |
| 12 | 6 | 2 | 8 |
| **Tổng** | **94** | **23** | **117** |

Tổng 117 giờ, dưới trần 168 giờ. Quỹ đệm 51 giờ dành cho làm lại, chờ phản hồi và thi cử. Không tuần nào phải giãn, nên lộ trình giữ 12 tuần. Nếu cần giãn thì dùng quỹ đệm để kéo sang tuần 13–14 mà không cần sửa nội dung.

## Phụ lục B: Bảng đối chiếu các điểm đã chê

| Điểm chê | Sửa ở đâu trong 4.0 |
|---|---|
| Bắt buộc 8–10 giờ/tuần, chưa tính thời gian chờ và làm lại | Mỗi tuần bắt buộc ≤ 9 giờ. Quỹ đệm 51 giờ ở phần Quy tắc nền |
| Tuần 3 và 4 quá nặng | Tuần 3 chuyển 2 AI sang Mở rộng. Tuần 4 còn 9 giờ bắt buộc |
| Tuần 1 phụ thuộc file PDF chưa xác nhận | Tuần 1 có bước kiểm tra link trước khi bắt đầu, và có phương án dự phòng |
| Tuần 6 quá tải vì voice và Python cùng lúc | Tuần 6 chỉ voice, tuần 7 mới làm Python |
| Thiếu mốc giữa kỳ | Tuần 8 có mock giữa kỳ và test thật lần 2 |
| Luật nền tảng thiếu cách xử lý khi bị hạ điểm | Mục "Luật chơi nền tảng" có 3 bước xử lý |
| Thu nhập $9 không có nguồn | Phần ước tính tuần 12 ghi là giả định, có khoảng so sánh |
| Tuần 9 cần 3 người chấm, không có cách tuyển | Tuần 9 có phương án dự phòng 2 người và tự chấm lại |
| G-Eval cần few-shot chưa học | Few-shot và chain-of-thought học ở tuần 9 Mở rộng, trước khi viết prompt |
| Tuần 9 đứng trước tuần 10 chưa đủ kỹ năng | Tuần 9 có checklist làm từ kết quả đo của 3 người, không phụ thuộc kỹ năng riêng |
| Số 100 câu quá nhiều | Tuần 1 giảm còn 60 câu, tuần 10 cũng 60 câu |
| Mock test không có cảnh báo | Quy tắc nền ghi rõ mock là mô phỏng, không dự đoán thi thật |

## Phụ lục C: Điểm reviewer vẫn chưa ưng sau vòng cuối

1. **Quỹ đệm 51 giờ chưa phân bổ theo tuần.** Lộ trình nói quỹ này dùng cho làm lại và chờ phản hồi, nhưng chưa có cách đo nó đang được dùng thế nào. Cần thêm một dòng ghi chú cuối mỗi tuần.
2. **Tuần 9 vẫn phụ thuộc vào người thật.** Ba người Việt chấm tự do là điều kiện khó đảm bảo, và phương án 2 người vẫn yếu hơn.
3. **Thu nhập vẫn là giả định.** Con số $9 chỉ có thể kiểm chứng sau khi có dữ liệu thật từ tuần 4 trở đi. Cần cập nhật tuần 12 bằng số liệu thực.
4. **Test thật lần 2 ở tuần 8 phụ thuộc chính sách nền tảng.** Nhiều nền tảng không cho làm lại nhanh. Nếu vậy, mốc giữa kỳ chỉ còn mock, và reviewer không coi đó là đo tiến bộ đủ tin cậy.
5. **Tuần 1 vẫn có rủi ro về link.** Phương án dự phòng dùng ví dụ trong tài liệu Label Studio, nhưng nội dung cụ thể của ví dụ đó chưa được kiểm chứng.
