screen.blit(data["assets"]["overlay"], (0,0))

screen.blit(data["surfaces"][data["page"]], (0,0))

if not pygame.mouse.get_pressed()[0]:
    data["cache"]["swipecache"] -= 1 if data["cache"]["swipecache"] > 0 else 0

if data["cache"]["swipecache"] == 0 and pygame.mouse.get_pressed()[0]:
    data["cache"]["mouseposcache"] = list(pygame.mouse.get_pos())[1]

data["cache"]["swipecache"] += pygame.mouse.get_pressed()[0]