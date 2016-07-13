# Python image optimization

Resize images keeping aspect ratio.

### Installation

```sh
$ pyvenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```
### Usage and options
```sh
$ python resize.py [base_width] [base_height]
```

The default aspect ratio is ``800x500``.

resize.py scan the current directory and will process all images ```(.jpg, .gif, .png)``` and put them into ```processed``` folder.

