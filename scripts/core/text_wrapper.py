def text_wrap(text, width, font, passes=5):
    rendered = font.render(text, False, [0,0,0])
    if rendered.get_width() < width:
        return text #Return the original text if it can be left unchanged
    text_cached = text.replace(".",".\n")
    rendered = []
    for i in text_cached.split("\n"):
        rendered += [font.render(i, False, [0,0,0]).get_width()]
    if max(rendered) < width:
        return text_cached.rstrip() #Return text separated at the end of sentences
    
    rendered = []
    text_cached = text.split(" ")
    for i in text_cached:
        i = i.rstrip() + " "
        rendered += [font.render(i, False, [0,0,0]).get_width()]
    for p in range(passes):
        try:
            for i in range(len(text_cached)-1):
                if rendered[i] + rendered[i+1] < width:
                    rendered[i] += rendered[i+1]
                    del rendered[i+1]
                    text_cached[i] += " "+text_cached[i+1]
                    del text_cached[i+1]
                    i-=1
        except:
            pass
    return "\n".join(text_cached).rstrip()
            