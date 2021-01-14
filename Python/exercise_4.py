import random
import re
import textwrap

def generate_random_text(text):
    words = text.split()
    # remove non characters (?,;.' ,etc)
    words = [re.sub(r'\W+', '', word).lower() for word in words if re.sub(r'\W+', '', word).isalpha()]

    word_triplets = []
    for w1, w2, w3 in zip(words[0:-2], words[1:-1], words[2:]):
        word_triplets.append((w1, w2, w3))

    random.shuffle(word_triplets)

    used_triplets = []
    output_text = []
    ref_triplet = random.choice(word_triplets)
    output_text.extend(ref_triplet)

    while len(output_text) < 200:
        for word_triplet in word_triplets:
            if ref_triplet[1] == word_triplet[0] and ref_triplet[2] == word_triplet[1] and word_triplet not in used_triplets:
                output_text.append(word_triplet[2])
                used_triplets.append(word_triplet)
                ref_triplet = word_triplet
                break
        else:
            break

    return ' '.join(output_text)


if __name__ == '__main__':
    text = '''October arrived, spreading a damp chill over the grounds and into the castle. Madam Pomfrey, the nurse, was
    kept busy by a sudden spate of colds among the staff and students. Her Pepperup potion worked instantly, though it left
    the drinker smoking at the ears for several hours afterward. Ginny Weasley, who had been looking pale, was bullied
    into taking some by Percy. The steam pouring from under her vivid hair gave the impression that her whole head was on
    fire.
    Raindrops the size of bullets thundered on the castle windows for days on end; the lake rose, the flower beds turned
    into muddy streams, and Hagrid's pumpkins swelled to the size of garden sheds. Oliver Wood's enthusiasm for regular
    training sessions, however, was not dampened, which was why Harry was to be found, late one stormy Saturday afternoon
    a few days before Halloween, returning to Gryffindor Tower, drenched to the skin and splattered with mud.
    Even aside from the rain and wind it hadn't been a happy practice session. Fred and George, who had been spying on
    the Slytherin team, had seen for themselves the speed of those new Nimbus Two Thousand and Ones. They reported that
    the Slytherin team was no more than seven greenish blurs, shooting through the air like missiles.
    As Harry squelched along the deserted corridor he came across somebody who looked just as preoccupied as he was.
    Nearly Headless Nick, the ghost of Gryffindor Tower, was staring morosely out of a window, muttering under
    his breath, ". . . don't fulfill their requirements . . . half an inch, if that . . ." 
    Nearly ten years had passed since the Dursleys had woken up to find their nephew on the front step, but Privet Drive 
    had hardly changed at all. The sun rose on the same tidy front gardens and lit up the brass number four on the 
    Dursleys' front door; it crept into their living room, which was almost exactly the same as it had been on the night 
    when Mr. Dursley had seen that fateful news report about the owls. Only the photographs on the mantelpiece really 
    showed how much time had passed. Ten years ago, there had been lots of pictures of what looked like a large pink beach 
    ball wearing different-colored bonnets - but Dudley Dursley was no longer a baby, and now the photographs showed a 
    large blond boy riding his first bicycle, on a carousel at the fair, playing a computer game with his father, being 
    hugged and kissed by his mother. The room held no sign at all that another boy lived in the house, too.
    Yet Harry Potter was still there, asleep at the moment, but not for long. His Aunt Petunia was awake and it was her 
    shrill voice that made the first noise of the day. 
    When he was dressed he went down the hall into the kitchen. The table was almost hidden beneath all Dudley's birthday 
    presents. It looked as though Dudley had gotten the new computer he wanted, not to mention the second television and 
    the racing bike. Exactly why Dudley wanted a racing bike was a mystery to Harry, as Dudley was very fat and hated 
    exercise - unless of course it involved punching somebody. Dudley's favorite punching bag was Harry, but he couldn't 
    often catch him. Harry didn't look it, but he was very fast.

    Perhaps it had something to do with living in a dark cupboard, but Harry had always been small and skinny for his age. 
    He looked even smaller and skinnier than he really was because all he had to wear were old clothes of Dudley's, and 
    Dudley was about four times bigger than he was. Harry had a thin face, knobbly knees, black hair, and bright green 
    eyes. He wore round glasses held together with a lot of Scotch tape because of all the times Dudley had punched him 
    on the nose. The only thing Harry liked about his own appearance was a very thin scar on his forehead that was shaped 
    like a bolt of lightning. He had had it as long as he could remember, and the first question he could ever remember 
    asking his Aunt Petunia was how he had gotten it. 

    Hagrid looked at Harry with warmth and respect blazing in his eyes, but Harry, instead of feeling pleased and proud, 
    felt quite sure there had been a horrible mistake. A wizard? Him? How could he possibly be? He’d spent his life being 
    clouted by Dudley and bullied by Aunt Petunia and Uncle Vernon; if he was really a wizard, why hadn’t they been turned 
     warty toads every time they’d tried to lock him in his cupboard? If he’d once defeated the greatest sorcerer in the 
     world, how come Dudley had always been able to kick him around like a football?
    '''

    random_text = generate_random_text(text)
    print('\n'.join(textwrap.wrap(random_text, 64)))
