from .common import InfoExtractor


class KokoatvExtractorIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?kokoa\.tv/(?:episode|movie)/(?P<id>.+)/?'
    _TESTS = [{
        'url': 'https://kokoa.tv/episode/%ed%99%98%ec%8a%b9%ec%97%b0%ec%95%a0-%ec%8b%9c%ec%a6%8c-2-2%ed%99%94/',
        'md5': 'TODO: md5 sum of the first 10241 bytes of the video file (use --test)',
        'info_dict': {
            'id': '42',
            'ext': 'mp4',
            'title': 'Video title goes here',
            'thumbnail': r're:^https?://.*\.jpg$',
            # TODO more properties, either as:
            # * A value
            # * MD5 checksum; start the string with md5:
            # * A regular expression; start the string with re:
            # * Any Python type, e.g. int or float
        }
    }]

    def _real_extract(self, url):
        video_id = self._match_id(url)
        webpage = self._download_webpage(url, video_id)

        # Unnecessary
        # title = self._html_search_regex(r'<h1 class="episode_title entry-title">(.+?)</h1>', webpage, 'title')
        link = self._html_search_regex(r'"(https?://(?:dicecake|imedia10|hopvuive)\.com/play\.php\?pid=([0-9]+))"', webpage, 'link')

        webpage1 = self._download_webpage(link, video_id, headers={
            'Referer': url,
        })

        link2 = self._html_search_regex(r'\'(https?://hqplus.vidground.com/watch/(.+?))\'', webpage1, 'video')

        webpage2 = self._download_webpage(link2, video_id, headers={
            'Origin': link,
            'Referer': link,
        })
        info_dict = self._extract_jwplayer_data(
            webpage2, video_id, require_title=False)
        print(info_dict)
        return info_dict
