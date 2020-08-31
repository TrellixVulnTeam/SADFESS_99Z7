from twitter import Twitter
import time


tw = Twitter()

def start():
    print("Starting program...")
    dms = list()
    while True:
        if len(dms) is not 0:
            for i in range(len(dms)):
                message = dms[i]['message']
                # I take sender_id just in case you want to know who's sent the message
                sender_id = dms[i]['sender_id']
                id = dms[i]['id']
                text = "[BOT] Tweet kamu udah terkirim ya. Kamu udahan ya sedihnya, jangan sedih terus :("

                if len(message) is not 0 and len(message) < 280:
                    # prikitiw is the keyword
                    # if you want to turn off the case sensitive like: priktiw, Prikitiw, pRiKiTiw
                    # just use lower(message) and check it, but please remove the replace function line
                    if "sad" in message.lower():
                        if len(message) is not 0:
                            if dms[i]['media'] is None:
                                print("DM will be posted")
                                tw.post_tweet(message)
                                tw.send_dm(sender_id, text)
                                tw.delete_dm(id)
                            else:
                                print("DM will be posted with media")
                                print(dms[i]['shorted_media_url'])
                                tw.post_tweet_with_media(message, dms[i]['media'],dms[i]['shorted_media_url'], dms[i]['type'])
                                tw.send_dm(sender_id, text)
                                tw.delete_dm(id)
                        else:
                            print("DM deleted because its empty..")
                            tw.delete_dm(id)
                    else:
                        print("DM will be deleted because does not contains keyword..")
                        tw.delete_dm(id)

            dms = list()

        else:
            print("Direct message is empty...")
            dms = tw.read_dm()
            if len(dms) is 0 or dms is None:
                time.sleep(31)

if __name__ == "__main__":
    start()
