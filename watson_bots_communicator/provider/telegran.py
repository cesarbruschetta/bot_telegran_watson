

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from watson_bots_communicator.core.basebot import BaseBot
from watson_bots_communicator.config import TELEGRAN_TOKEN



logger = logging.getLogger(__name__)


class TelegranBot(BaseBot):
    
    def __init__(self):
        super(TelegranBot, self).__init__()
        
        self.updater = Updater(TELEGRAN_TOKEN)
        self.dp = self.updater.dispatcher


    def error(self, bot, update, error):
        logger.error('Update "%s" caused error "%s"' % (update, error))


    def message(self, bot, update):
        
        update.message.reply_text(
            self.watson.message(update.message.text)
        )

    
    def register(self):
    
        # self.dp.add_handler(CommandHandler('hello', hello))
        self.dp.add_handler(MessageHandler(Filters.text, self.message))
        
        # log all errors
        self.dp.add_error_handler(self.error)
    
        # Start the Bot
        self.updater.start_polling()
    
        # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT. This should be used most of the time, since
        # start_polling() is non-blocking and will stop the bot gracefully.
        self.updater.idle()