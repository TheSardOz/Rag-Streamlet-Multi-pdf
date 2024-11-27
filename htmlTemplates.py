css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #5b1c97
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
/* not quiet working as intended .stTextInput>div>div {
    position: fixed;
    bottom: 3rem;
    width: calc(100% - 30px);
    padding: 15px;
    background-color: #fff;
    border-radius: 5px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}*/
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/BNqPzVT/artificial-8264664-640.jpg">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.ibb.co/HKsJ3Qz/ass-2025922-640.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''