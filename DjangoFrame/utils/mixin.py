from django.contrib.auth.decorators import login_required

from DjangoFrame.utils.logger import Log

# 初始化log日志参数路径
logger = Log('utils').logger


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):

        # UserInfoView父类中的as_view
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


if __name__ == '__main__':
    logger.warning('测试。')
