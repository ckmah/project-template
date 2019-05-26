from slacker import Slacker


class Notify:
    '''
    A class for posting Slack messages.
    '''

    def __init__(self, token=None, username='beep', channel='beep'):
        '''
        username : str, default 'beep'
            description

        channel : str, default 'beep'
            description
        '''
        if not token:
            print('Token not specified.')
            return

        self.slack = Slacker(token)
        self.username = username
        self.channel = channel
        self.token = token

    def msg_start(self):
        self.msg('Start :slack:')

    def msg_end(self):
        self.msg('Finished :ok_hand:')

    def msg(self, msg='Hello :v:'):
        '''
        msg : str, default 'Hello :v:'
            Message to post to slack. Emojis can be used with standard Slack syntax.
        '''
        response = self.slack.chat.post_message(channel=self.channel,
                                           text=msg,
                                           username=self.username)

    def msg_file(self, fname=None):
        response = self.slack.files.upload(file_=fname,
                                      channels=self.channel,
                                      initial_comment=fname)
        assert response["ok"]
