def save_info(request, data):
    req_post = request.POST
    req_files = request.FILES
    data.desc = req_post.get('desc')

    try:
        data.title = req_post.get('title')
    except:
        pass

    try:
        data.status = req_post.get('status')
    except:
        pass

    try:
        data.image_1 = req_files.get('image_1')
    except:
        pass

    try:
        data.image_2 = req_files.get('image_2')
    except:
        pass

    try:
        data.image_3 = req_files.get('image_3')
    except:
        pass

    try:
        data.image_4 = req_files.get('image_4')
    except:
        pass

    try:
        data.image_5 = req_files.get('image_5')
    except:
        pass

    return data