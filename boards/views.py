# Create your views here.
from django.http.response import HttpResponseNotFound, HttpResponse
from django.shortcuts import render_to_response, Http404, get_list_or_404
from boards.models import ImageBoard, BoardCategories, Thread, PostInThread



def show_index(request, *args, **kwargs):
    return render_to_response('front.html', {})


def show_frame(request, *args, **kwargs):
    boards_list = ImageBoard.objects.all()

    D = dict()
    for b in boards_list:
        if b.category in D:
            D[b.category].append((b.caption, b.slug_name))
        else:
            D[b.category] = [(b.caption, b.slug_name)]
    return render_to_response('frame.html',
                              {'boards': D},
                              )


def show_news(request, *args, **kwargs):
    return render_to_response('news.html', {})


def show_404(request, *args, **kwargs):
    return HttpResponseNotFound('NOt found!')


def show_thread(request, board_name, thread_number):
    return HttpResponse('[Thread] name: %s, number: %s' % (board_name, thread_number))


def show_board_index(request, board_name, page_number):
    from math import ceil
    page_number = int(page_number)
    #board is not exist
    try:
        i_board = ImageBoard.objects.get(slug_name=board_name)
        page_limit = i_board.threads_on_page
        max_threads = i_board.max_threads_on_board
    except:
        print 'exception'
        return show_404(request)

    num_of_pages = int(ceil(float(max_threads) / page_limit))
    list_of_pages = range(0, num_of_pages)

    begin_number_post = page_limit * page_number
    end_number_post = page_limit * (1 + page_number)

    threads_on_page = get_list_or_404(Thread,
                                      pk__board_owner_id__slug_name=board_name)[begin_number_post:end_number_post]
    threads_with_posts = [(t, []) for t in threads_on_page]
    for t in threads_with_posts:
        thread_post = t[0]
        t[1].extend(PostInThread.objects.all().filter(thread_owner=thread_post))

    return render_to_response('board_page.html', {'board_name': board_name,
                                                  'page_number': page_number,
                                                  'threads_on_page': threads_with_posts,
                                                  # 'posts': posts,
                                                  'pages': list_of_pages
                                                  })
