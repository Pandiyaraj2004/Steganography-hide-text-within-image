# Image Steganography

> Hide and recover text inside an image through a simple Flask interface.

**Python · Flask · Pillow · Stegano**

## What it demonstrates

A complete upload → image processing → download workflow using least-significant-bit (LSB) steganography.

- Encode a message into an uploaded image.
- Save and download the resulting image.
- Upload an encoded image to recover its message.
- Display validation and result messages through server-rendered templates.

## Try it locally

```bash
git clone https://github.com/Pandiyaraj2004/Steganography-hide-text-within-image.git
cd Steganography-hide-text-within-image
python -m pip install flask pillow stegano
python app.py
```

Open http://localhost:5000. For a reliable demonstration, use a lossless PNG image and a short test message.

1. Choose **Encode**, upload a PNG, and enter a test message and password.
2. Download the encoded image.
3. Choose **Decode**, upload that image, and enter the same password.

## Implementation

| Path | Responsibility |
| --- | --- |
| [app.py](app.py) | Encode, decode, and download routes |
| [templates](templates) | Forms and results |
| [static/style.css](static/style.css) | Interface styling |
| `uploads/` | Original and encoded images |

## Design boundary

The password is stored alongside the message in the hidden payload and checked during decoding. This is a demonstration of steganography, **not encryption** or secure secret storage. Recompression and image editing can destroy the payload. Use non-sensitive test data; production use would require encryption, upload limits, file validation, and cleanup.

---

Built by **Pandiyaraj A** · [Portfolio](https://pandiyaraj.netlify.app/) · [GitHub](https://github.com/Pandiyaraj2004) · [LinkedIn](https://www.linkedin.com/in/pandiyaraj-a-mca/)
