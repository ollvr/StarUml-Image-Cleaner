import xml.etree.ElementTree as ET
import cairosvg


file_path = "Your SVG file path"
output_svg_path = "cleaned_svg.svg"
output_png_path = "cleaned_image.png"


tree = ET.parse(file_path)
root = tree.getroot()


namespaces = {'svg': 'http://www.w3.org/2000/svg'}


for text_element in root.findall('.//svg:text', namespaces):
    if text_element.text and "UNREGISTERED" in text_element.text:
        text_element.text = text_element.text.replace("UNREGISTERED", "")


tree.write(output_svg_path, encoding="utf-8", xml_declaration=True)
print(f"Cleaned SVG saved as '{output_svg_path}'")


cairosvg.svg2png(url=output_svg_path, write_to=output_png_path)
print(f"Converted image saved as '{output_png_path}'")