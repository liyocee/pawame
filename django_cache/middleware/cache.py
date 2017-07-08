
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from django.core.cache import caches

class APICacheMiddleware(MiddlewareMixin):
    def __init__(self, get_response=None):
        self.get_response = get_response
        self.cached_urls = settings.CACHE_URLS
        self.cache = caches['default'] # use default cache, Todo - make this configurable to allow different caching backends

    def process_request(self, request):
        return self.cache.get(request.path)

    def process_response(self, request, response):

        if request.method == 'GET': # only cache GET requests
            url_cache_config = self._get_url_cache_config(request.path)

            if url_cache_config:
                # cache the response for the url
                cache_key = request.path
                cache_timeout = url_cache_config[1] * 60 # cache config are in minutes
                self.cache.set(cache_key, response, cache_timeout)
        return response

    def _get_url_cache_config(self, url_path):
        """
        Check if a particular API endpoint has been defined to be cached in
        the settings.CACHE_URLS and return its cache configuration
        """
        for cached_url in self.cached_urls:
            if url_path == cached_url[0]:
                return cached_url

        return None
