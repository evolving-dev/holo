class holo_io:

    class http:

        def get(url, **kwargs):
            if SETTINGS['connectivity_enabled']:
                try:
                    return HoloResponse(True, requests.get(url, **kwargs))
                except:pass
            return HoloResponse(False)

        def post(url, **kwargs):
            if SETTINGS['connectivity_enabled']:
                try:
                    return HoloResponse(True, requests.post(url, **kwargs))
                except:pass
            return HoloResponse(False)

        def put(url, **kwargs):
            if SETTINGS['connectivity_enabled']:
                try:
                    return HoloResponse(True, requests.put(url, **kwargs))
                except:pass
            return HoloResponse(False)

        def patch(url, **kwargs):
            if SETTINGS['connectivity_enabled']:
                try:
                    return HoloResponse(True, requests.patch(url, **kwargs))
                except:pass
            return HoloResponse(False)

        def delete(url, **kwargs):
            if SETTINGS['connectivity_enabled']:
                try:
                    return HoloResponse(True, requests.delete(url, **kwargs))
                except:pass
            return HoloResponse(False)
