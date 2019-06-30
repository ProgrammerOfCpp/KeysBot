#########################
ENG_BTN_TEXT = '🇬🇧 English'
RUS_BTN_TEXT = 'Русский'
STORE_BTN_TEXT = 'Store'
WALLET_BTN_TEXT = 'Wallet'
SETTINGS_BTN_TEXT = 'Settings'
SUPPORT_BTN_TEXT = 'Support'
###########################
START_MSG = 'Please select your language.'
STORE_MSG = 'Below is the list of active lots. If you want to search some lots by the name or description just enter a string to search.'
STORE_NOT_FOUND = 'The Store is empty! You may try to go to Setting section and Toggle Store mode to see all available lots.'
SEARCH_RESULTS = 'Search results:'
WALLET_MSG = """Your wallet balance:
<b>{:.6f}BTC</b>
Total loaded:
<b>{:.6f}BTC</b>
Total spent:
<b>{:.6f}BTC</b>"""
SETTINGS_MSG = 'Please choose the option.'
SUPPORT_MSG = """👋 Welcome to @keysender_bot! 

I will help you to buy and sell string keys. For buying the key you need to load some BTC to the Wallet. Then go to the Store and choose the lot to buy. If you want to sell some keys just create a new lot in Settings section. Pretty Easily! Enjoy!"""
###########################
NEW_LOT_BTN = 'New lot.'
MANAGE_LOTS_BTN = 'Manage lots.'
SET_NEW_ADDRESS_BTN = 'Set new address to send.'
TOGGLE_STORE_MODE_BTN = 'Toggle Store mode'
###########################
FAV_MODE_ON = 'Your Store mode is now set to <b>Faforites</b>. This means that you will see only your favorite lots in the Store section. Toggle to switch to All mode.'
FAV_MODE_OFF = 'Your Store mode is now set to <b>All</b>. This means that you will see all lots in the Store section. Toggle to switch to Favorites mode.'
###########################
INPUT_ADDRESS_TEXT = "Please Paste the new address you want to Send money to:"
INCORRECT_VALUE = "Please input correct value"
INPUT_ADDRESS_SUCCESS = """BTC address to Send is <b>{}</b>
Use command /out AMOUNT, for example: /out 1.5 
Specified amount will be sent to your address during an hour (min: 0.02BTC)."""
ADDRESS_NOT_SET = """BTC address to send is <b>not set</b>.
Please go to Settings section and set BTC address to Send money to."""
###########################
LOTS_LIST = 'Your lots list (push to edit):'
LOT_TITLE = '{0} ({1:.5f}EUR)'
INPUT_TITLE = 'Please enter the short and clear name of your lot. Try not to use more than 100 symbols.'
INPUT_DESCRIPTION = 'Please enter the description of your lot. Try not to use more than 2500 symbols.'
INPUT_PRICE = 'Please enter the price of one key of your lot in EUR. For example  0.5. Min. value is {:.5f}EUR'
INPUT_KEYS = 'Submit a key or a bunch of keys separated by next line. All message limit is 2500 symbols.'
VALUE_SET_SUCCESS = '👍 The value was set successfully.'
TRY_ANOTHER_TITLE = 'The name is already taken!'
VALUE_SET_SUCCESS_QUANTITY = '👍 The value was set successfully. ({} items)'
LOT_CREATED = 'Great! Your new lot has been created successfully! To Activate your lot please go to "Manage my lots" section and set appropriate lot status.'
SKIP_HINT = '💡 Hint: you can use /skip (or just /sk) command to save the current description and skip this step.'
###############################
ACTIVATE_BTN = "Activate"
DEACTIVATE_BTN = "Deactivate"
EDIT_BTN = "Edit"
DELETE_BTN = "Delete"
BUY_FOR = 'Buy the key for {0:.5f}EUR'
LOT_ACTIVATED = "Your lot is now <b>activated</b> and will be shown to the users."
LOT_DEACTIVATED = "Your lot is now <b>deactivated</b> and will not be shown to the users."
LOT_DELETED = "Your lot is completely deleted."
LOT_INFO = """<b>{}</b>

 {}


Status:  {}

Lot keys (All/Sold/Available):  {}/{}/{}

Rating:  👍 {}   👎 {}
"""
##############################
PAYMENT_WARNING = """The amount of <b>{:.7f}BTC</b> will be debited from your wallet. Please note, that the bot takes no responsibility for the user's lots. This operation can not be cancelled. Are you sure you want to continue?"""
PAYMENT_YES = "Yes"
PAYMENT_NO = "No"
KEYS_OVER = "It seems like all the keys were sold"
TRANSACTION_ERROR = "Error while performing transaction."
PAYMENT_LOW_BALANCE = "😬 Ooops! Seems like there are not enough funds on your wallet! Please add some funds and come again!"
PAYMENT_SUCCESS_SEND = "Operation status: success"
PAYMENT_SUCCESS_BUY = """Operation status: success
Below is your key. After approving a key works you can set Like or Dislike to this lot which will affect the lot rating."""
PAYMENT_DISLIKE = "👎Dislike"
PAYMENT_LIKE = "👍Like"
WALLET_LOAD_BTN = "Load"
WALLET_SEND_BTN = "Send"
WALLET_HISTORY_BTN = "History"
PAYMENT_TYPE_BUY = "buy"
PAYMENT_TYPE_SEND = "send"
RECENT_TRANSACTIONS = """Your recent transactions:

"""
TRANSACTION =  "<b>{}</b> {:.8f} ({})\n"
WALLET_LOAD_MSG = """Your personal BTC address for loading the wallet:

<b>{}</b>

Your wallet balance will be updated after several network confirmations (usually during an hour). 
You can use your wallet balance to buy some keys in the Store or Send any amount to any BTC address through the blockchain (1% comission).
🌞 Actual BTC rates
1 BTC = {:.8f} USD
1 BTC = {:.8f} EUR"""
