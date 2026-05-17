#!/usr/bin/env python3
"""
vpn-connector - VPN连接工具
工具编号: tool-080
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import secrets
import string
import hashlib

class App:
    def __init__(self, root):
        self.root = root
        root.title("VPN连接工具 v1.0")
        root.geometry("800x600")
        self.setup_ui()
    
    def setup_ui(self):
        # 标题
        title_frame = tk.Frame(self.root, bg="#F44336", height=60)
        title_frame.pack(fill="x")
        title_frame.pack_propagate(False)
        tk.Label(title_frame, text="🔐 VPN连接工具", font=("Arial", 18, "bold"),
                 fg="white", bg="#F44336").pack(pady=15)
        
        # 主区域
        main = tk.Frame(self.root, padx=20, pady=15)
        main.pack(fill="both", expand=True)
        
        # 密码生成器
        gen_frame = tk.LabelFrame(main, text="🔑 密码生成", font=("Arial", 10, "bold"))
        gen_frame.pack(fill="x", pady=10)
        
        tk.Label(gen_frame, text="长度:").grid(row=0, column=0, padx=10, pady=5)
        self.length_var = tk.IntVar(value=16)
        tk.Scale(gen_frame, from_=8, to=64, orient="horizontal",
                 variable=self.length_var, length=200).grid(row=0, column=1, padx=5, pady=5)
        
        self.upper_var = tk.BooleanVar(value=True)
        self.lower_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=True)
        self.special_var = tk.BooleanVar(value=True)
        
        tk.Checkbutton(gen_frame, text="大写字母", variable=self.upper_var).grid(row=1, column=0, padx=10)
        tk.Checkbutton(gen_frame, text="小写字母", variable=self.lower_var).grid(row=1, column=1, padx=10)
        tk.Checkbutton(gen_frame, text="数字", variable=self.digits_var).grid(row=2, column=0, padx=10)
        tk.Checkbutton(gen_frame, text="特殊字符", variable=self.special_var).grid(row=2, column=1, padx=10)
        
        tk.Button(gen_frame, text="🎲 生成密码", command=self.generate_password,
                  bg="#4CAF50", fg="white", padx=20, pady=8).grid(row=3, column=0, columnspan=2, pady=10)
        
        # 结果显示
        result_frame = tk.LabelFrame(main, text="📋 结果", font=("Arial", 10, "bold"))
        result_frame.pack(fill="both", expand=True, pady=10)
        
        self.result_var = tk.StringVar()
        tk.Entry(result_frame, textvariable=self.result_var, font=("Consolas", 14),
                 width=40).pack(pady=10)
        
        tk.Button(result_frame, text="📋 复制", command=self.copy_result,
                  bg="#2196F3", fg="white", padx=15, pady=5).pack(pady=5)
        
        # 哈希计算
        hash_frame = tk.LabelFrame(main, text="🔒 哈希计算", font=("Arial", 10, "bold"))
        hash_frame.pack(fill="x", pady=10)
        
        tk.Label(hash_frame, text="输入文本:").pack(side="left", padx=10)
        self.hash_input = tk.StringVar()
        tk.Entry(hash_input, width=30).pack(side="left", padx=5)
        tk.Button(hash_frame, text="计算MD5", command=self.calc_md5,
                  bg="#9C27B0", fg="white").pack(side="left", padx=5)
        tk.Button(hash_frame, text="计算SHA256", command=self.calc_sha256,
                  bg="#9C27B0", fg="white").pack(side="left", padx=5)
        
        # 状态
        self.status_var = tk.StringVar(value="就绪")
        tk.Label(main, textvariable=self.status_var, fg="gray").pack(fill="x")
    
    def generate_password(self):
        length = self.length_var.get()
        chars = ""
        
        if self.upper_var.get():
            chars += string.ascii_uppercase
        if self.lower_var.get():
            chars += string.ascii_lowercase
        if self.digits_var.get():
            chars += string.digits
        if self.special_var.get():
            chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
        
        if not chars:
            messagebox.showwarning("提示", "请至少选择一种字符类型！")
            return
        
        password = ''.join(secrets.choice(chars) for _ in range(length))
        self.result_var.set(password)
        self.status_var.set(f"✅ 已生成 {length} 位密码")
    
    def copy_result(self):
        text = self.result_var.get()
        if text:
            self.root.clipboard_clear()
            self.root.clipboard_append(text)
            self.status_var.set("✅ 已复制到剪贴板")
    
    def calc_md5(self):
        text = self.hash_input.get()
        if text:
            result = hashlib.md5(text.encode()).hexdigest()
            self.result_var.set(result)
            self.status_var.set("✅ MD5 计算完成")
    
    def calc_sha256(self):
        text = self.hash_input.get()
        if text:
            result = hashlib.sha256(text.encode()).hexdigest()
            self.result_var.set(result)
            self.status_var.set("✅ SHA256 计算完成")

def main():
    root = tk.Tk()
    App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
