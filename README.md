# hangulfrequency
Looking at the frequency of each Hangul syllabic block

My Hangul frequency project aims to visualize the relative frequency of Hangul syllabic blocks. Frequency is calculated from a single corpus of data, the Korean Contemporary Corpus of Written Sentences, which I downloaded from <http://nlp.kookmin.ac.kr/kcc/>.

I've kept my first attempt (filename hangulFreq.html), which simply displays a table of all possible syllabic blocks and colors the background of each block according to the block's relative frequency. A white background signifies a frequency of 0, while a red (FF0000) background signifies the most common syllabic block in the dataset, 다. Specifically, the color of the background is determined by setting the green and blue values to decrease linearly with increased relative frequency of the syllabic block.

It turns out, however, that a linear association does not produce a good visualization. In hangulFreq2.html, the color value scale corresponds to the logarithm of the relative frequency of a syllabic block, which produces a better visualization. The user can toggle between a color scale from black to white for high to low frequency, and red to blue for high to low frequency, using a switch in the upper right-hand corner of the page. Clicking on a syllabic block will generate an informational box to the right giving more details about the syllabic block and its occurrences in the data.
