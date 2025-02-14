import speedtest
import datetime
import json
import requests

TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN"
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID"

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "Markdown"}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Error sending message to Telegram: {e}")

def load_history():
    try:
        with open("speedtest_results.json", "r") as file:
            data = [json.loads(line) for line in file]
        return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_result(result):
    with open("speedtest_results.json", "a") as file:
        file.write(json.dumps(result) + "\n")

def calculate_average(history):
    if not history:
        return {"Download Speed (Mbps)": 0, "Upload Speed (Mbps)": 0, "Ping (ms)": 0}
    
    total_download = sum(entry["Download Speed (Mbps)"] for entry in history) / len(history)
    total_upload = sum(entry["Upload Speed (Mbps)"] for entry in history) / len(history)
    total_ping = sum(entry["Ping (ms)"] for entry in history) / len(history)
    
    return {
        "Download Speed (Mbps)": round(total_download, 2),
        "Upload Speed (Mbps)": round(total_upload, 2),
        "Ping (ms)": round(total_ping, 2)
    }

def check_speed():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        
        download_speed = st.download() / 1_000_000
        upload_speed = st.upload() / 1_000_000
        ping = st.results.ping
        
        server = st.get_best_server()
        isp = st.results.client.get("isp", "Unknown")
        ip = st.results.client.get("ip", "Unknown")
        location = f"{server['name']}, {server['country']}"
        
        result = {
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "ISP": isp,
            "IP Address": ip,
            "Test Server": location,
            "Ping (ms)": round(ping, 2),
            "Download Speed (Mbps)": round(download_speed, 2),
            "Upload Speed (Mbps)": round(upload_speed, 2)
        }
        
        save_result(result)
        history = load_history()
        averages = calculate_average(history)
        
        result_message = (
            "📡 *Speed Test Result:*\n"
            f"🏢 *ISP:* {isp}\n"
            f"🌍 *IP:* {ip}\n"
            f"📍 *Server:* {location}\n"
            f"⏳ *Ping:* {ping:.2f} ms\n"
            f"⬇️ *Download:* {download_speed:.2f} Mbps\n"
            f"⬆️ *Upload:* {upload_speed:.2f} Mbps\n\n"
            "📊 *Average Speeds:*\n"
            f"⬇️ *Avg Download:* {averages['Download Speed (Mbps)']} Mbps\n"
            f"⬆️ *Avg Upload:* {averages['Upload Speed (Mbps)']} Mbps\n"
            f"⏳ *Avg Ping:* {averages['Ping (ms)']} ms"
        )
        
        print(json.dumps(result, indent=4))
        print("\nAverage Speeds from History:")
        print(json.dumps(averages, indent=4))
        
        send_to_telegram(result_message)
        
    except Exception as e:
        print(f"Error running speed test: {e}")

if __name__ == "__main__":
    check_speed()
