data["mousePos"] = list(pygame.mouse.get_pos())

if event.type == pygame.MOUSEBUTTONUP:
    data["dd"].detect_click(data["mousePos"])