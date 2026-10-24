import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")

# Fake API demo - ông thay bằng API thật của ông
def get_ff_info(uid):
    # Ví dụ data trả về, ông thay bằng code call API Free Fire
    return f"""
🎮 **FREE FIRE INFO**
├ UID: {uid}
├ Tên: KenVipGm
├ Level: 29
├ Like: 19204
├ Region: ID
└ Status: Hoạt động

🌐 Tra cứu lúc: Giờ Việt Nam
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """
😈 **BDZ INFO BOT — HỆ THỐNG TRA CỨU FREE FIRE**

🎮 **DANH SÁCH LỆNH:**
├ /allinfo <uid> : Tra cứu toàn bộ thông tin
├ /check <uid> : Kiểm tra tình trạng Khóa/Ban
├ /search <tên> : Tìm theo UID hoặc Tên
├ /level <uid> : Xem chi tiết Cấp độ
├ /stats br <uid> : Thống kê Sinh tồn
├ /stats cs <uid> : Thống kê Tử chiến
└ /outfit <uid> : Xem nhân vật & trang phục

Gõ /allinfo 13246235234 để test
"""
    await update.message.reply_text(text)

async def allinfo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Dùng: /allinfo <uid>")
        return
    uid = context.args[0]
    result = get_ff_info(uid)
    await update.message.reply_text(result)

async def check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Dùng: /check <uid>")
        return
    uid = context.args[0]
    await update.message.reply_text(f"✅ UID {uid} - Trạng thái: Bình thường, không bị ban")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("allinfo", allinfo))
app.add_handler(CommandHandler("check", check))

app.run_polling()
