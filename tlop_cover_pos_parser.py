#this is from the source code of http://thepablo.life/js/functions.js
t  = """goUp(0, at(1,   0));     goDown(0,  at(1,  0));     goLeft(0, at(1,  0));     goRight(0, at(1,  0)); 
      goUp(0, at(2,   0));     goDown(2,  at(2,  0));     goLeft(0, at(2,  0));     goRight(0, at(2,  0)); 
      goUp(0, at(3,   0));     goDown(3,  at(3,  0));     goLeft(0, at(3,  0));     goRight(0, at(3,  0)); 
      goUp(0, at(4,   0));     goDown(5,  at(4,  0));     goLeft(0, at(4,  0));     goRight(0, at(4,  0)); 
      goUp(0, at(5,   0));     goDown(7,  at(5,  0));     goLeft(0, at(5,  0));     goRight(0, at(5,  0)); 
      goUp(0, at(6,   0));     goDown(8,  at(6,  0));     goLeft(0, at(6,  0));     goRight(0, at(6,  0)); 
      goUp(0, at(7,   0));     goDown(10, at(7,  0));     goLeft(0, at(7,  0));     goRight(0, at(7,  0)); 
      goUp(10, at(8,  0));     goDown(0,  at(8,  0));     goLeft(0, at(8,  0));     goRight(3, at(8,  0)); 
      goUp(20, at(9,  0));     goDown(0,  at(9,  0));     goLeft(0, at(9,  0));     goRight(0, at(9,  0)); 
      goUp(39, at(10, 0));     goDown(0,  at(10, 0));     goLeft(0, at(10, 0));     goRight(3, at(10, 0)); 
      goUp(38, at(11, 0));     goDown(0,  at(11, 0));     goLeft(0, at(11, 0));     goRight(3, at(11, 0)); 
      goUp(36, at(12, 0));     goDown(0,  at(12, 0));     goLeft(0, at(12, 0));     goRight(3, at(12, 0)); 
      goUp(34, at(13, 0));     goDown(0,  at(13, 0));     goLeft(0, at(13, 0));     goRight(3, at(13, 0)); 
      goUp(32, at(14, 0));     goDown(0,  at(14, 0));     goLeft(0, at(14, 0));     goRight(3, at(14, 0)); 
      goUp(31, at(15, 0));     goDown(0,  at(15, 0));     goLeft(0, at(15, 0));     goRight(3, at(15, 0)); 
      goUp(30, at(16, 0));     goDown(0,  at(16, 0));     goLeft(0, at(16, 0));     goRight(3, at(16, 0)); 
      goUp(36, at(17, 0));     goDown(0,  at(17, 0));     goLeft(3, at(17, 0));     goRight(0, at(17, 0)); 
      goUp(34, at(18, 0));     goDown(0,  at(18, 0));     goLeft(3, at(18, 0));     goRight(0, at(18, 0)); 
      goUp(33, at(19, 0));     goDown(0,  at(19, 0));     goLeft(3, at(19, 0));     goRight(0, at(19, 0)); 
      goUp(32, at(20, 0));     goDown(0,  at(20, 0));     goLeft(3, at(20, 0));     goRight(0, at(20, 0)); 
      goUp(30, at(21, 0));     goDown(0,  at(21, 0));     goLeft(3, at(21, 0));     goRight(0, at(21, 0)); 
      goUp(28, at(22, 0));     goDown(0,  at(22, 0));     goLeft(3, at(22, 0));     goRight(0, at(22, 0)); 
      goUp(26, at(23, 0));     goDown(0,  at(23, 0));     goLeft(3, at(23, 0));     goRight(0, at(23, 0));
      goUp(25, at(24, 0));     goDown(0,  at(24, 0));     goLeft(3, at(24, 0));     goRight(0, at(24, 0)); 
      
  //COLUMN 2          
      goUp(0, at(1,   1));     goDown(102, at(1,  1));    goLeft(0, at(1,  1));     goRight(0,  at(1, 1)); 
      goUp(0, at(2,   1));     goDown(103, at(2,  1));    goLeft(0, at(2,  1));     goRight(0,  at(2, 1)); 
      goUp(0, at(3,   1));     goDown(105, at(3,  1));    goLeft(0, at(3,  1));     goRight(0,  at(3, 1)); 
      goUp(0, at(4,   1));     goDown(106, at(4,  1));    goLeft(0, at(4,  1));     goRight(0,  at(4, 1)); 
      goUp(0, at(5,   1));     goDown(108, at(5,  1));    goLeft(0, at(5,  1));     goRight(0,  at(5, 1)); 
      goUp(0, at(6,   1));     goDown(109, at(6,  1));    goLeft(0, at(6,  1));     goRight(0,  at(6, 1)); 
      goUp(0, at(7,   1));     goDown(110, at(7,  1));    goLeft(0, at(7,  1));     goRight(0,  at(7, 1)); 
      goUp(0, at(8,  1));      goDown(107, at(8,  1));    goLeft(2, at(8,  1));     goRight(0,  at(8, 1)); 
      goUp(0, at(9,  1));      goDown(82,  at(9,  1));    goLeft(0, at(9,  1));     goRight(1,  at(9, 1)); 
      goUp(0, at(10, 1));      goDown(78,  at(10, 1));    goLeft(2, at(10, 1));     goRight(0,  at(10, 1)); 
      goUp(0, at(11, 1));      goDown(80,  at(11, 1));    goLeft(2, at(11, 1));     goRight(0,  at(11, 1)); 
      goUp(0, at(12, 1));      goDown(81,  at(12, 1));    goLeft(2, at(12, 1));     goRight(0,  at(12, 1)); 
      goUp(0, at(13, 1));      goDown(82,  at(13, 1));    goLeft(2, at(13, 1));     goRight(0,  at(13, 1)); 
      goUp(0, at(14, 1));      goDown(84,  at(14, 1));    goLeft(2, at(14, 1));     goRight(0,  at(14, 1)); 
      goUp(0, at(15, 1));      goDown(85,  at(15, 1));    goLeft(2, at(15, 1));     goRight(0,  at(15, 1)); 
      goUp(0, at(16, 1));      goDown(87,  at(16, 1));    goLeft(2, at(16, 1));     goRight(0,  at(16, 1)); 
      goUp(0, at(17, 1));      goDown(95,  at(17, 1));    goLeft(0, at(17, 1));     goRight(10, at(17, 1)); 
      goUp(0, at(18, 1));      goDown(97,  at(18, 1));    goLeft(0, at(18, 1));     goRight(10, at(18, 1)); 
      goUp(0, at(19, 1));      goDown(99,  at(19, 1));    goLeft(0, at(19, 1));     goRight(10, at(19, 1)); 
      goUp(0, at(20, 1));      goDown(100, at(20, 1));    goLeft(0, at(20, 1));     goRight(10, at(20, 1)); 
      goUp(0, at(21, 1));      goDown(102, at(21, 1));    goLeft(0, at(21, 1));     goRight(10, at(21, 1)); 
      goUp(0, at(22, 1));      goDown(103, at(22, 1));    goLeft(0, at(22, 1));     goRight(10, at(22, 1)); 
      goUp(0, at(23, 1));      goDown(105, at(23, 1));    goLeft(0, at(23, 1));     goRight(10, at(23, 1));
      goUp(0, at(24, 1));      goDown(107, at(24, 1));    goLeft(0, at(24, 1));     goRight(10, at(24, 1)); 
      
  //COLUMN 3          
      goUp(0, at(1,  2));      goDown(83,  at(1,  2));     goLeft(0,  at(1,  2));     goRight(0, at(1, 2)); 
      goUp(0, at(2,  2));      goDown(85,  at(2,  2));     goLeft(0,  at(2,  2));     goRight(0, at(2, 2)); 
      goUp(0, at(3,  2));      goDown(86,  at(3,  2));     goLeft(0,  at(3,  2));     goRight(0, at(3, 2)); 
      goUp(0, at(4,  2));      goDown(88,  at(4,  2));     goLeft(0,  at(4,  2));     goRight(1, at(4, 2)); 
      goUp(0, at(5,  2));      goDown(89,  at(5,  2));     goLeft(0,  at(5,  2));     goRight(1, at(5, 2)); 
      goUp(0, at(6,  2));      goDown(91,  at(6,  2));     goLeft(0,  at(6,  2));     goRight(1, at(6, 2)); 
      goUp(0, at(7,  2));      goDown(92,  at(7,  2));     goLeft(0,  at(7,  2));     goRight(1, at(7, 2)); 
      goUp(0, at(8,  2));      goDown(94,  at(8,  2));     goLeft(0,  at(8,  2));     goRight(1, at(8, 2)); 
      goUp(0, at(9,  2));      goDown(90,  at(9,  2));     goLeft(0,  at(9,  2));     goRight(3, at(9, 2)); 
      goUp(0, at(10, 2));      goDown(91,  at(10, 2));     goLeft(0,  at(10, 2));     goRight(3, at(10, 2)); 
      goUp(0, at(11, 2));      goDown(93,  at(11, 2));     goLeft(0,  at(11, 2));     goRight(3, at(11, 2)); 
      goUp(0, at(12, 2));      goDown(94,  at(12, 2));     goLeft(0,  at(12, 2));     goRight(3, at(12, 2)); 
      goUp(0, at(13, 2));      goDown(96,  at(13, 2));     goLeft(0,  at(13, 2));     goRight(2, at(13, 2)); 
      goUp(0, at(14, 2));      goDown(97,  at(14, 2));     goLeft(0,  at(14, 2));     goRight(3, at(14, 2)); 
      goUp(0, at(15, 2));      goDown(99,  at(15, 2));     goLeft(0,  at(15, 2));     goRight(2, at(15, 2)); 
      goUp(0, at(16, 2));      goDown(101, at(16, 2));     goLeft(0,  at(16, 2));     goRight(3, at(16, 2)); 
      goUp(17, at(17, 2));     goDown(95,  at(17, 2));     goLeft(28, at(17, 2));     goRight(0, at(17, 2)); 
      goUp(17, at(18, 2));     goDown(97,  at(18, 2));     goLeft(28, at(18, 2));     goRight(0, at(18, 2)); 
      goUp(17, at(19, 2));     goDown(99,  at(19, 2));     goLeft(28, at(19, 2));     goRight(0, at(19, 2)); 
      goUp(17, at(20, 2));     goDown(100, at(20, 2));     goLeft(28, at(20, 2));     goRight(0, at(20, 2)); 
      goUp(17, at(21, 2));     goDown(102, at(21, 2));     goLeft(28, at(21, 2));     goRight(0, at(21, 2)); 
      goUp(17, at(22, 2));     goDown(103, at(22, 2));     goLeft(28, at(22, 2));     goRight(0, at(22, 2)); 
      goUp(17, at(23, 2));     goDown(105, at(23, 2));     goLeft(28, at(23, 2));     goRight(0, at(23, 2));
      goUp(17, at(24, 2));     goDown(107, at(24, 2));     goLeft(28, at(24, 2));     goRight(0, at(24, 2));"""
def m():
    return {'x':0,'y':0}
from collections import defaultdict
d = defaultdict(m)
for i in t.split(';'):
    i = i.strip()
    try:
        indices = (int(i.split('(')[-1].split(',')[0]), int(i.split(',')[-1].split(')')[0]))
        j = i.split('(')
        typ = j[0]
        offset = int(j[1].split(',')[0])
        if typ == "goUp":
            d[indices]['y'] -= offset
        elif typ == 'goDown':
            d[indices]['y'] += offset
        elif typ=='goLeft':
            d[indices]['x'] -= offset
        elif typ=='goRight':
            d[indices]['x'] += offset
    except:
        print(i)
print(d)

def make_text_shadows(d, scaling_factor = 2):
    #positions = d.values()
    x_offset_trans = {0:0, 1:291, 2:565}
    text_shadows = 'text-shadow:'
    for index, position in d.items():
        i = index[0]
        j = index[1]
        text_shadows += '{x}px {y}px 0 {hexx},'.format(x=((position['x']+x_offset_trans[j])/scaling_factor),y=((position['y']+i*31)/scaling_factor), hexx='#000')
    return text_shadows[:-1]

print(make_text_shadows(d))
#each coordinate is divided by the scaling factor
def make_css(scaling_factor = 2):
    t_s = make_text_shadows(d, scaling_factor)
    css = """body{{
            background:rgb(247, 140, 88)
    }}
    #text{{
            color:rgb(247, 140, 88);
            white-space: pre;
            position:fixed;
            top:20%;
            left:20%;
            font: bold 13.5px 'Helvetica Neue', Helvetica, Arial, sans-serif;
            {text_shadows}
    }}
    #text:after{{
            display:block;
            content:'';
            position:relative;
            height:82px; 
            width:118px;
            background-size:contain;
            background-image:url('ye.png');
            top:362px;
            left:25px;
    }}""".format(font_size = 27/scaling_factor, text_shadows = t_s, imgh = 164/scaling_factor,
                 imw = 236/scaling_factor, imgy = 724/scaling_factor, imgx = 50/scaling_factor, 
