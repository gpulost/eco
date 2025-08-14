#!/usr/bin/env python3
import http.server
import socketserver
import webbrowser
import os
import sys

# 设置端口
PORT = 8000

# 切换到当前目录
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # 添加CORS头以支持本地文件访问
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def start_server():
    """启动HTTP服务器"""
    try:
        with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
            print(f"🚀 服务器启动成功!")
            print(f"📊 上证指数可视化页面: http://localhost:{PORT}")
            print(f"📁 服务目录: {os.getcwd()}")
            print(f"⏹️  按 Ctrl+C 停止服务器")
            print("-" * 50)
            
            # 自动打开浏览器
            try:
                webbrowser.open(f'http://localhost:{PORT}')
                print("✅ 浏览器已自动打开")
            except:
                print("⚠️  请手动打开浏览器访问上述地址")
            
            print("-" * 50)
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n👋 服务器已停止")
        sys.exit(0)
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ 端口 {PORT} 已被占用，请尝试其他端口或关闭占用程序")
            print(f"💡 您也可以修改 PORT 变量使用其他端口")
        else:
            print(f"❌ 启动服务器失败: {e}")
        sys.exit(1)

if __name__ == "__main__":
    start_server()