
from watson_developer_cloud import ConversationV1
from watson_bots_communicator.config import WATSON_PASSWORD, WATSON_USERNAME, WATSON_WORKSPACE



class Watson(object):
    
    context = {}
    def __init__(self):
        self.conversation = ConversationV1(username=WATSON_USERNAME,
                                           password=WATSON_PASSWORD,
                                           version='2018-02-16')
    
    def message(self, message_text, tag_join="\n"):
        output_message = []
    
        response = self.conversation.message(workspace_id=WATSON_WORKSPACE,
                                        context=self.context,
                                        input={'text': message_text})
    
        self.context = response['context']
        output_message = response['output']['text']
        
        return tag_join.join(output_message)
        