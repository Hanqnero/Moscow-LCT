# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['app_mobile.py'],
    pathex=[],
    binaries=[],
    datas=[('config.ini', '.'), ('runs', 'runs'), ('manifest.json', '.')],
    hiddenimports=['streamlit', 'ultralytics', 'torch', 'cv2', 'PIL', 'numpy', 'pandas', 'yaml'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['matplotlib', 'IPython', 'notebook'],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='TreeDetection',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
