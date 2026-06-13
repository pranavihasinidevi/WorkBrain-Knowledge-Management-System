import os

files = {
"requirements.txt": "streamlit==1.32.0\nplotly==5.20.0\npandas==2.2.1\nqrcode==7.4.2\nPillow==10.2.0\n",
".gitignore": "__pycache__/\n*.pyc\n.env\nvenv/\n.DS_Store\n",
".streamlit/config.toml": '[theme]\nbase="dark"\nbackgroundColor="#0B0F1A"\nsecondaryBackgroundColor="#0F1629"\nprimaryColor="#6366F1"\ntextColor="#F1F5F9"\n\n[server]\nheadless=true\nenableCORS=false\nport=8501\n',
}

for path, content in files.items():
    os.makedirs(os.path.dirname(path), exist_ok=True) if os.path.dirname(path) else None
    open(path, "w").write(content)
    print(f"OK {path}")

print("Done! Now run: pip install -r requirements.txt")
print("Then run: streamlit run app.py")
