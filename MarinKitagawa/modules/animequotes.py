#Made By @Madepranav On Telegram & Github Id Superboyfan
import html
import random
import MarinKitagawa.modules.animequotesstring as animequotesstring
from MarinKitagawa import dispatcher
from telegram import ParseMode, Update
from MarinKitagawa.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async


@run_async
def animequotes(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(animequotesstring.ANIMEQUOTES))
   


ANIMEQUOTES_HANDLER = DisableAbleCommandHandler("animequotes", animequotes)

dispatcher.add_handler(ANIMEQUOTES_HANDLER)


