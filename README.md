# splash-client

This is the online splash for the djo hackerspace

## Installation

```bash
git clone https://@github.com/ILoveAndLikePizza/splash-client
cd splash-client
python -m venv ENV
source ./ENV/bin/activate
pip install -r requirements.txt
```

Then you can simply run it with `python client.py`, optionally followed by an ip.
If the pip install gives you some kind of python execution error,
you might need to install the python development package: `python-dev` or `python-devel`.

## Usage

Once connected, just press `w`, `a` and `d` to play.
You will automatically be assigned a splash player if a slot is available.

## Info

You can find the splash implementation in the [lichtkrant repo](https://github.com/djoamersfoort/lichtkrant).
