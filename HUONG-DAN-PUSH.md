# Đẩy repo này lên GitHub

Repo này để PUBLIC — nó là portfolio sống cho khách hàng xem. Nhớ: không đẩy dữ liệu job thật (NDA).

## Cách 1: dùng GitHub CLI (nhanh nhất)

```bash
cd ai-trainer-journey
git init
git add .
git commit -m "Khoi tao hanh trinh AI trainer 3 thang"
gh repo create ai-trainer-journey --public --source=. --push
```

## Cách 2: tạo tay trên github.com

1. Vào github.com → New repository → tên `ai-trainer-journey` → Public → Create.
2. Chạy:

```bash
cd ai-trainer-journey
git init
git add .
git commit -m "Khoi tao hanh trinh AI trainer 3 thang"
git branch -M main
git remote add origin https://github.com/<ten-tai-khoan>/ai-trainer-journey.git
git push -u origin main
```

## Mỗi tuần sau đó

```bash
git add .
git commit -m "Tuan X: <tom tat viec da lam>"
git push
```

## Gắn vào profile Upwork

Vào profile Upwork → phần portfolio/link: dán link repo
`https://github.com/<ten-tai-khoan>/ai-trainer-journey`
Khách xem được toàn bộ quá trình học + thí nghiệm + hiện vật của bạn.
