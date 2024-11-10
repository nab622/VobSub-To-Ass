# VobSub Image Extractor/Converter

This is a Python program designed to extract images from .VOB files and convert them to SubStation Alpha format (.ass). The resulting files preserve the original color and appearance of the VobSub files, meaning all langauges are preserved correctly.

This library is based on [VobSub-ML-OCR](https://github.com/vincrichard/VobSub-ML-OCR), which is a python port of [SubtitleEdit](https://github.com/SubtitleEdit/subtitleedit) code.


## Features

1. **Image Extraction**: The program can extract images from provided VobSub files. The user can specify the file and destination folder for the extracted images.

2. **Conversion to SubStation Alpha (.ass)**: The VobSub images are extracted into pixel data, then reconstructed using a special font. The resulting files will be larger than the originals, but they will play on just about anything, and the original subtitles are preserved. So for instance, the Invader Zim DVDs will retain the Irken subtitles.

3. **Parallel Processing**: The program automatically detects an appropriate number of jobs to run in parallel, based on the number of CPU cores available.


## Installation and Setup

The only requirement to run this library is to have Python 3. I don't know exactly which version is required, just use a reasonably up-to-date one and you should be fine.

You should also have `mkvmerge`, `ffprobe` (Part of ffmpeg), and something to rip IDX/SUB files with (I use `mplayer`).

## Usage

To run this script:

```bash
python3 VobSubToAss.py <arguments>
```

To correctly package the resulting subtitles into a video file, ***YOU MUST USE AN MKV FILE*** and you ***MUST*** attach the font to the final file, or it will not display correctly.
Attaching fonts to MKV files is very easy to do with `mkvmerge`. When creating an MKV file, add the subtitle file, then add the following arguments to the end of the command:

`--attachment-mime-type` application/x-truetype-font `--attach-file` <Font Name>

You can also attach fonts to MKV files using FFmpeg, but I do not recommend it since the FFmpeg MKV muxer is broken and subtitles sometimes go missing.


The arguments for this script are:

* `--input_file` The path to the .sub, .idx or .json file to convert.
* `--output_file` The path to use for the .ass file output.
* `--video_width` The width of the original video (Usually 720).
* `--video_height` The height of the original video (Usually 480 or 576).

* `--palette` The color palette (16 RGB hexadecimal colors, delimited with commas).
* `--convert_YUV` (default = False) Optional - this will treat the --palette values as YUV, and convert them to RGB for you automatically.

* `--use_sub_timestamps` (default = False) Optional - this will use the timestamps obtained from the VOB/SUB file, instead of from the IDX file.

* `--crop_data` Optional - the parent video's crop data from FFmpeg, I.E. 720:360:0:58

* `--time_scale` Optional - the multiplier to use on the subtitle timing.
* `--time_offset` Optional - the this will shift the subtitle timing by the specified number of seconds.

* `--resolution_scale` (default = 2) Optional - this value states how much to increase the SubStation Alpha resolution. All other items are scaled to match, so this will not make any visual changes.

* `--line_height` (default = 32) Optional - this value is used to scale the subtitles by the average height of each line. Other factors, like the width and height, may force this value to be less than desired, to avoid truncating on the edges. Valid range from 10 to 120.
* `--margin` (default = 8) Optional - this is how many pixels (Based on the original video resolution) to use as a margin on all four sides.

* `--max_line_spacing` (default = -1) Optional - this is how many rows of transparent pixels to render before stopping. This has the effect of bringing lines of text closer together. Use -1 to disable.
* `--keep_position` (default = True) Optional - this will allow subtitles to keep their original position, whether that be top, middle, bottom, left, center, or right.

* `--alpha_threshold` (default = 35) Optional - any alpha below this intensity will be considered transparent. Range is 0 to 255.
* `--alignment_threshold` (default = 25) Optional - this value is a percentage used to determine the placement of a subtitle on the screen. Higher numbers mean subtitles are more likely to be at the vertical edges and horizontal center of the screen. Valid values are 0 to 100.

* `--font_name` (default = "PixelCaption") Optional - the name of the font to use. Note that this IS NOT the file name, this is the name of the font when used in a word processor or other software!

* `--shadow_size` (default = 1.25) Optional - this will add a 3D shadow effect to the resulting subtitles. Default value is 1, set to 0 to disable. Keep in mind that the subtitles are far more readable with the shadows on.

* `--max_duration` (default = 10) Optional - this sets the maximum duration for subtitles. This may be important in cases where the duration is controlled by the timing on the next subtitle.
* `--min_height` (default = 5) Optional - this sets the minimum height for a subtitle. Anything smaller than this will be ignored. This may be important in cases where the duration is controlled by the timing on the next subtitle. Set to 0 to use all subtitles.
* `--min_width` (default = 5) Optional - this sets the minimum width for a subtitle. Anything smaller than this will be ignored. This may be important in cases where the duration is controlled by the timing on the next subtitle. Set to 0 to use all subtitles.


## For those who wish to use JSON input, here is how to generate it.

* Use `ffprobe` to extract the VobSub packet data from the VOB file:

`ffprobe`
`-analyzeduration` 99999999000000
`-probesize` <VOB file size in bytes>
`-v` quiet
`-i` <VOB file name, concatenated>
`-show_packets`
`-show_data`
`-select_streams` i:0x20 (Subtitle track 1 is 0x20, track 2 is 0x21, track 3 is 0x22, etc)
`-print_format` json

Use the following Python code to clean up the FFmpeg data dump:
```python
	subsOutput = []
	for i in range(len(response)):
		startTime = float(response[i]['pts_time'])
		subData = response[i]['data']
		subData = subData.split('\n')

		newSubData = ''
		x = 0
		while x < len(subData):
			# Remove blank entries!
			if len(subData[x]) == 0:
				subData.pop(x)
				continue
			subData[x] = subData[x].split(': ', 1).pop()
			subData[x] = subData[x].split('  ', 1)
			subData[x].pop()
			subData[x] = subData[x].pop()
			subData[x] = subData[x].split(' ')
			subData[x] = ''.join(subData[x])
			newSubData += subData[x]
			x += 1
		subsOutput.append({ 'startTime' : startTime, 'data' : newSubData })
```

Next, extract the `IDX/SUB` files. We can not use them for the subtitles themselves, because the timing will be wrong. However, we do have to use the IDX file to get the palette.
Split the palette data into a list of 16 elements, one element for each color's hexadecimal values.

If you use `mplayer` to perform this extraction, there is a bug in mplayer that incorrectly reports the palette. To fix this, use the following Python code, and run the `idxToRGB` function below on the palette:

```python
def idxToRGB(color):
	# Apparently IDX files are calculated wrong and are neither RGB nor YUV. What a shock, another bug.
	return YUVStringToRGBString(vobsub_rgb_to_yuv(int(color, 16)))

def intColorToHexColor(color):
	output = intToHex(color)
	if len(output) < 2:
		output = '0' + output
	return output

def vobsub_rgb_to_yuv(rgb):
	# This function was modeled after mplayer's source code. Apparently IDX files are calculated wrong
	# and are neither RGB nor YUV. What a shock, another bug.

	r = (rgb >> 16) & 0xff
	g = (rgb >> 8) & 0xff
	b = rgb & 0xff

	y = (0.299 * r + 0.587 * g + 0.114 * b) * 219 / 255 + 16.5
	u = (-0.16874 * r - 0.33126 * g + 0.5 * b) * 224 / 255 + 128.5
	v = (0.5 * r - 0.41869 * g - 0.08131 * b) * 224 / 255 + 128.5

	return intColorToHexColor(int(y) << 16 | int(u) << 8 | int(v))

def YUVStringToRGBString(inputString):
	# This function takes a 6-digit hexadecimal value for YUV color and converts it to RGB
	output = ''
	tempColors = YUVToRGB(int(inputString[0:2], 16), int(inputString[2:4], 16), int(inputString[4:6], 16))

	i = 0
	while i < len(tempColors):
		tempColors[i] = hex(tempColors[i])
		tempColors[i] = tempColors[i].split('0x')[1]
		j = 2 - len(tempColors[i])
		while j > 0:
			tempColors[i] = '0' + tempColors[i]
			j -= 1
		i += 1

	return ''.join(tempColors)

def YUVToRGB(inputY, inputU, inputV):
	inputY -= 16
	inputU -= 128
	inputV -= 128

	outputR = 1.164 * inputY + 1.596 * inputV
	outputG = 1.164 * inputY - 0.392 * inputU - 0.813 * inputV
	outputB = 1.164 * inputY + 2.017 * inputU

	return [ clamp(int(outputR), 0, 255), clamp(int(outputG), 0, 255), clamp(int(outputB), 0, 255) ]
```

Finally, you can put everything together in a `JSON` object:
```
data = {
	"palette"		: <Palette List>,
	"subpictures"	: <Subtitle Data Packets List>
}
```

Write this object to a `JSON` file somewhere on your disk. This will be the file you give the script with `input_file`.


## Happy converting!

