from PIL import Image, ImageDraw, ImageFont
import os
import textwrap

text_list = [
    "The character's hands hang naturally at the sides of their body, their body's center of gravity slightly lowered, and they move slowly to the left.",
    "The character runs forward lightly.",
    "The character turns around lightly.",
    "The character swiftly and lightly slides forward, becoming invisible during the process, with agile and clean movements, smoothly and fluently, feeling light and airy.",
    "The character rolls forward lightly and quickly gets up.",
    "The character rolls to the left side lightly and quickly gets up.",
    "The character is hit, their body goes into large stagger, and they get up at a moderate speed. They stagger in panic, leaning backward, while swinging their right arm in the air.",
    "The character holds a greatsword or ultra greatsword in their right hand and performs a charged heavy attack. They squat halfway, lean slightly to the right side with their upper body, and then swing the sword forward. Finally, they return to the original standing posture.",
    "The character holds a greatsword or ultra greatsword in their right hand and performs a non-charged heavy attack. They swing the sword forward from the right side. Finally, they return to the original standing posture.",
    "The character performs a light attack with a thrusting sword held in the left hand. They elegantly perform a flourish with their right hand before thrusting it forward, taking light steps forward. Then, they return to their stance.",
    "The character wields a curved sword and a large curved sword in each hand, and swings the swords in rotation before returning to a standing posture.",
    "The character wields a curved sword and a large curved sword in each hand, and swings the swords in rotation before returning to a standing posture.",
    "The character holds a katana in their right hand, runs quickly and charges, then uses a direct and powerful attack to thrust forward, and finally returns to a standing posture.",
    "The character uses dual-wielding katanas to perform a technique that deflects attacks. They heavily lean to the left side, crouch down, and gather strength. Then, they lunge forward with their right foot and stab with their right hand, before returning to their original stance.",
    "The character wields an axe in their right hand and performs a jumping attack. They jump up, and as they land, they swing the axe forward with their right hand before returning to a standing position.",
    "The character dual wields axes and performs a quick strike, swiftly twisting their waist to the right, stepping forward with their right leg, and slashing downward diagonally with both hands.",
    "The character dual wields halberds and charges a powerful strike. They firmly twist their waist to the side, step forward with their right leg, hold the weapons with both hands, gather strength from the left rear, and then swing in two consecutive circles.",
    "The character holds a pair of boxing gloves in their right hand and swings directly forward with a firm and clean movement.",
    "The character utilizes a technique with curved swords and great curved swords, firmly carries the weapons on their shoulder, rotates to the left, counterclockwise almost one and a half circles, and swings the weapons.",
    "The character is knocked backward, falling on their back, then slowly gets up and stands upright.",
    "The character uses their powerful and heavy hands to push the obstacle forward slowly and with force.",
    "The character clenches their right fist, swings their right arm upward twice, swings their left arm upward, swings their right arm upward again, and raises their right fist high. The action is clean, quick, and joyful.",
    "The character slightly moves their right foot backward and claps their hands multiple times in front of their abdomen, with light, clean, and quick movements, expressing joy and fluidity.",
    "The character jumps up happily, then swings their right fist forward, with powerful, clean, and quick movements, showcasing a sense of wildness, excitement, acrobatics, juggling, dancing, and cheerfulness.",
    "The character kneels on the ground with their legs spread apart, bows their head and bends over in sadness, with light and swift movements, but with a touch of despair.",
    "The character lowers their body, bends their right leg, and extends their left leg forward. They raise their left hand and turn their body clockwise. They rotate 180 degrees to face left, opening their left hand backward in a horse-riding squat pose. Then, they return to a squatting posture.",
    "The character uses a mechanical axe to charge up a heavy attack with their left hand. They step back with their left foot, pulling their left hand back for power. Then, they turn their body forward and lean, swinging their left hand from left to right as their body rotates 360 degrees. Finally, they raise their left hand high, bring down the axe while lifting their right foot, and land in a horse stance facing the right. They then return to a standing position.",
    "The character holds a wedge-shaped weapon with both hands, raising it high above their head. They then take a lunge position with their right leg forward and left leg behind, and swing the weapon downwards.",
    "The character turns to the right, lunges forward, inserts the wedge-shaped weapon into the scabbard on their left hand, gathers strength, then turns clockwise and swings the weapon forward.",
    "The character uses Undead Slasher to perform a two-handed attack. They firmly swing the sword from behind to the front, and then insert the sword into the scabbard on their back."
]


image_size = (300, 300)

output_folder = "textImg"
os.makedirs(output_folder, exist_ok=True)

for index, text in enumerate(text_list):
    # 创建白色背景图片
    image = Image.new("RGB", image_size, "white")
    draw = ImageDraw.Draw(image)

    font_path = "msyh.ttc"  # 微软雅黑
    font_size = 12
    font = ImageFont.truetype(font_path, font_size)

    # 文本框大小
    text_box = (0, 0, image_size[0], image_size[1])

    # 文本自动换行
    wrapped_text = textwrap.fill(text, width=30)  # 每行最大字符数

    # 计算文本绘制位置，上下居中
    text_width, text_height = draw.textsize(wrapped_text, font)
    x = (image_size[0] - text_width) // 2
    y = (image_size[1] - text_height) // 2

    draw.multiline_text((x, y), wrapped_text, font=font, fill="black", align="center")

    image.save(os.path.join(output_folder, f"text_{index + 1}.png"))