from yt_concate.pipeline.stops.preflight import Preflight
from yt_concate.pipeline.stops.postflight import Postflight
from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.pipeline.stops.get_video_list import GetVideoList
from yt_concate.pipeline.stops.download_captions import DownLoadCaptions
from yt_concate.pipeline.stops.step import StepException
from yt_concate.utils import Utils

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID,
    }
    steps = [
        Preflight(),
        GetVideoList(),
        DownLoadCaptions(),
        Postflight(),
    ]
    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
