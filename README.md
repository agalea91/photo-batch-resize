# Photo Batch Resize ## Installation
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## CLI Usage

1. Put photos in `images` folder.
2. Run the app:
```
venv/bin/python batch_resize.py --max-px-size'1920' --images-folder='images'
```
3. The resized photos will be written to: `images-1080px`

