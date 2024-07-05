# Bulk-Image-Compression-Using-Python-s-PIL-Library
Learn efficient bulk image compression using Python's PIL library. Compress JPG, PNG, BMP, GIF, and TIFF files in one batch, reducing sizes without quality loss. Perfect for optimizing storage and enhancing website speed.

<p>&nbsp;</p>
<ul>
<li><strong>Purpose</strong>: Reduces file sizes of images to optimize web page loading times.</li>
<li><strong>Directory Setup</strong>:
<ul>
<li><code>directory</code>: Source directory where original images are located.</li>
<li><code>target_directory</code>: Destination for compressed images, created if non-existent.</li>
</ul>
</li>
<li><strong>Supported Formats</strong>: Supports JPEG, PNG, BMP, GIF, and TIFF formats.</li>
<li><strong>Compression Parameters</strong>:
<ul>
<li>JPEG/JPG images are saved with quality set to 20 for optimal compression.</li>
<li>Other formats are optimized without quality loss.</li>
</ul>
</li>
<li><strong>Error Handling</strong>: Handles permissions errors and other exceptions gracefully.</li>
<li><strong>Output</strong>: Prints each image's compression status for confirmation.</li>
</ul>
<h4>How to Use:</h4>
<ol>
<li>
<p><strong>Modify Directory</strong>: Set the <code>directory</code> variable to the path containing your images.</p>
</li>
<li>
<p><strong>Run the Script</strong>: Execute the script to compress all supported image files (.jpg, .jpeg, .png, .bmp, .gif, .tiff) found in the specified directory.</p>
</li>
</ol>
<p><strong>Usage</strong>: Ensure Python and PIL (Pillow) are installed. Modify <code>directory</code> to point to your image folder, run the script to compress images efficiently.</p>
<p>Note: Adjust quality parameter as needed for JPEG/JPG images to balance compression and visual quality.</p>
