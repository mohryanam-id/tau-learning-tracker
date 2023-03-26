"""
Arguments
Keyword Arguments
"""


def info(name, salary='unknown', *args, **kwargs):
    """
    :param name:
    :param salary:
    :return:
    """

    print('{} has salary: {}'.format(name, salary))
    print('another info: {}, {}'.format(args, kwargs))


info('Ryan', 100000000000)
info('Ryan')
info('Ryan', 1000000, 'Test', Kantor='Secret')
info('Ryan', Kantor='Secret')
