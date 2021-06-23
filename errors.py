# ************************************ ERROR MESSAGE FILE **********************************************#


def concat(error):
    """

    :param error:
    :return:
    """
    if isinstance(error, str):
        return ".".join(["backend.common", error])
    else:
        return "error message is not string type"


# ROLLING APP ERROR MESSAGES

PhoneOtpSendSuccessfully = concat("PhoneOtpSendSuccessfully")
XP_AMOUNT_REQUIRED = concat("XpAmountRequired")
USER_WALLET_NOT_FOUND = concat("UserWalletNotFound")
SERVER_ERR_UNABLE_TO_FETCH_YR_WLT_BALANCE = concat("ServerErrUnableToFetchYrWltBalance")
YU_DONT_HAVE_ENOUGH_AMT_TO_CNVT_IN_YOUR_WLT = concat(
    "YuDontHaveEnoughAmtToCnvtInYourWlt"
)
YOU_CANNOT_CONVERT_LESS_THAN = concat("YouCanNotConvertLessThan")
YOU_CANNOT_CONVERT_GREATER_THAN = concat("YouCanNotConvertGreaterThan")
ERROR_FROM_NODE_JS_API_SIDE = concat("ErrorFromNodeJsApiSide")
WALLET_ID_REQUIRED = concat("WalletIdRequired")
CRYPTO_AMOUNT_REQUIRED = concat("CryptoAmountRequired")
PLAN_FIELD_IS_REQUIRED = concat("PlanFieldIsRequired")
PLAN_FIELD_IS_NOT_VALID_CHOICE = concat("PlanFieldNotVaildChoice")
YOU_ALREADY_HAVING_THIS_PLAN_MEMBERSHIP = concat("YouAlreadyHavingThisPlanMembership")
NOT_ENGH_AMT_TO_CHOICE_PLAN_IN_YR_WLT = concat(
    "YouDontHaveEnghAmntToChoiceThatPlanInYrWlt"
)
SERVER_ERROR_TRY_AGAIN = concat("ServerErrorTryAgain")
AMOUNT_REQUIRED = concat("AmountRequired")
CHK_MIN_DEPOSIT_LIMIT = concat("CheckMinimumDepoisitLimit")
CHK_PER_DAY_DEPOSIT_LIMIT = concat("CheckPerDayDepoisitLimit")
CHK_MIN_WITHDRAW_LIMIT = concat("CheckMinimumWithdrawLimit")
CHK_PER_DAY_WITHDRAW_LIMIT = concat("CheckPerDayWithdrawLimit")
CHK_PER_MONTH_WITHDRAW_LIMIT = concat("CheckPerMonthWithdrawLimit")
CANT_PLACE_ORDER_MORE_THAN = concat("CantPlaceOrderMoreThanAmount")
YOU_CANT_EXCD_LIMIT = concat(
    "CantPurchaseMoreThan"
)  # you cannot exceed limit of 500$ per month
PLEASE_WAIT_FOR_SOMETIME = concat("PleaseWaitForSometimeWeAreUpdatingYourBalance")
Translation_In_Progress = concat("TransactionInprogress")

SOME_THING_WENT_WRONG = concat("SomeThingWentWrong")
MINIMUM_BTC_REQUIRED = concat("MinimumBTCRequired")

# XCHAT APP ERROR MESSAGES

THIS_REQUIRED_FIELD = concat("ThisRequiredField")
TO_USER_MUST_FRIEND = concat("ToUserMustFriend")
FRIEND_NOT_FOUND = concat("FriendNotFound")
GROUP_NOT_EXIST = concat("GroupNotExist")
ADMINS_UPDATE_GROUP_DETAILS = concat("AdminsUpdateGroupDetails")
GROUP_DOES_NOT_EXIST = concat("Groupdoesnotexist")
GROUP_CHAT_NOT_EXIST = concat("GroupChatNotExist")
CHAT_NOT_FOUND = concat("ChatNotFound")
CHANNEL_NOT_FOUND = concat("ChannelNotFound")
WRONG_FORMAT = concat("WrongFormat")
RECORD_NOT_EXISTS = concat("RecordNotExists")
UNAUTHORIZED_USER = concat("UnauthorizedUser")
RECORD_DELETED = concat("RecordDeleted")
CHANNEL_ID_REQUIRED = concat("ChannelIdRequired")
CHANNEL_NOT_EXIST_ID = concat("ChannelNotExistId")
RECORD_IS_NOT_EXISTS = concat("Recordisnotexists")
RECORD_DELETED_SUCCESSFULLY = concat("Recorddeletedsuccessfully")
ACCESS_DENIED_TO_DO_ACTION = concat("AccessDeniedToDoAction")
MESSAGE_NOT_EXIST = concat("MessageNotExist")
PERSONAL_CHAT_NOT_FOUND = concat("PersonalChatNotFound")
YOU_BALANCE_NOT_SUFFICIENT = concat("YouBalancetNotsufficiant")
YOU_TRANSFER_MIN_MAX_TP = concat("YouTransferMinMaxTP")
YOUR_TRANSACTION_SUCCESSFULLY = concat("YourTransactionSuccessfully")
YOUR_BALANCE_NOT_SUFFICIENT = concat("YouBalancetNotsufficiant")
PLEASE_TRY_AGAIN = concat("PlsTryAgain")
SUCCESSFULL_GIFT_CARD_WILL_SEND = concat(
    "TransactionisPlacedSuccessfullyGiftCardwillSend"
)
GREETING_MESSAGE_NOT_EXIST = concat("GreetingMsgNotExist")
RECORD_NOT_FOUND = concat("RecodNotFound")
AMOUNT_IS_REQUIRED_FIELD = concat("AmountIsRequiredField")
FROM_WALLET_FIELD_IS_REQUIRED = concat("From_walletFieldIsRequired")
YOU_CANNOT_PURCHASE_LESS_THAN_100_TP = concat("YouCanNotPurchaseLessThan100TP")
NOT_ALLOWED_WALLET_TO_PURCHASE_TP = concat("NotAllowedWalletToPurchaseTP")
ONLY_TP_PURCHASE_ALLOWED = concat("OnlyTPPurchaseAllowed")
NOT_OTC_MORE_THAN_AVAILABLE_BALANCE = concat("NotOtcMoreThanAvailableBalance")
SERVER_ERROR_PLEASE_TRY_AGAIN = concat("ServerErrorPleaseTryAgain")
CHANNEL_ID_IS_REQUIRED_FIELD = concat("ChannelIdIsRequiredField")
ALREADY_VIP_MEMBER = concat("AlreadyVIPMember")
FAIL_UPDATE_BDG_COUNT = concat("FailUpdateBdgCount")
INVITE_CODE_DOES_NOT_EXIST = concat("InviteCodeDoesNotExist")
INVITE_CODE_EXPIRED = concat("InviteCodeExpired")
INVITE_CODE_ALREADY_USED = concat("InviteCodeAlreadyUsed")
TO_WALLET_FIELD_IS_REQUIRED = concat("To_walletFieldIsRequired")
USR_ID_NOT_EXIST = concat("UserIdsNotExist")
NO_GROUP_WITH_GROUP_ID = concat("NoGroupWithGroupid")
ONLY_ADMIN_UPDATES = concat("OnlyAdminUpdates")
ONLY_SENDER_EDIT_MSG = concat("OnlySenderEditMessage")
ONLY_SENDER_DELETE_MSG = concat("OnlySenderDeleteMessage")
USER_NOT_GRP_MEMBER = concat("UserNotGroupMember")
MEMBER_LEAVED_GRP_SUCCESSFULLY = concat("MemberLeavedGroupSuccessfully")
GROUP_NOT_FOUND = concat("GroupNotFound")
GROUP_DOES_NOT_EXIST_THIS_USR = concat("GroupNotExistThisUser")
THIS_USR_IS_NOT_DELETE_CHANNEL = concat("ThisUserisNotDeleteChannel")
FRIEND_REQUEST_SENT_SUCCESSFULLY = concat("FriendRequestSentSuccessfully")
REQUEST_ALREADY_SENT = concat("RequestAlreadySent")
FRIEND_REQUEST_ACCEPTED = concat("FriendRequestAccepted")
REQUEST_NOT_FOUND = concat("RequestNotFound")
REQUEST_REJECTED = concat("RequestRejected")
REQUEST_CANCELLED = concat("RequestCancelled")
TRIGGER_SENT_SUCCESFULLY = concat("TriggerSentSuccessfully")
USER_NOT_FOUND = concat("UserNotFound")
REMOVE_FRIEND = concat("RemoveFriend")
PROFILE_CONFIG_UPDATED = concat("ProfileConfigurationUpdated")
FOLLOW_CHANNEL_SUCCESSFULLY = concat("FollowedChannelSuccessfully")
CONVERSATION_NOT_FOUND = concat("ConversationNotFound")
USER_EXIST_AS_MEMBER = concat("UserExistAsMember")
CHOICE_EITHER_ONE_OR_TWO = concat("ChoiceEitherOneOrTwo")
USER_LOGOUT = concat("UserLogout")
MESSAGE_SENT = concat("MessageSent")
SENDER_CHANNEL_ADMIN = concat("SenderChannelAdmin")
RECIEVER_NOT_FOUND = concat("ReceiverNotFound")
MEMBER_MADE_ADMIN = concat("MemberMadeAdmin")
UN_AUTHORIZED = concat("UnAuthorized")
YOUR_ACC_DISABLED_CONTACT_SUPPORT = concat("YourAccountDisabledContactSupportTeam")
TELEGRAM_UN_AUTH_DATA = concat("TelegramUnAuthData")
ADMIN_HAV_WRITE_UPDAT_ACCESS = concat("AdminhaveWriteUpdateAccess")
GREETING_EXIST_FOR_CHANNEL = concat("GreetingExistForChannel")
CHANNEL_ADMIN_HAVE_ACCESS = concat("ChannelAdminhaveAccess")
USER_EXIST_AS_ADMIN = concat("UserExistAsAdmin")
USER_EXIST_AS_WRITER = concat("UserExistAsWriter")
USER_NOT_IN_CHANNEL = concat("UserNotInChannel")
YOU_NOT_EXIST_IN_CHANNEL = concat("YouNotExistInChannel")
ONLY_ADMIN_CAN_GEN_CHANel_INVIT_LINK = concat("OnlyAdminCanGenerateChannelInviteLink")
CHANNEL_INVITE_CODE_GENERATED = concat("ChannelInviteCodeGenerated")
CHANNEL_INVITE_CODE_INVALID = concat("ChannelInvitationCodeInvalid")
CHANEL_CREATER_ROL_CANOT_BE_UPDTED = concat("ChannelCreatorRoleCannotBeUpdated")
USER_NOT_EXIST_AS_MEMBER = concat("UserNotExistAsMember")
USER_ALREADY_CHANNEL_ADMIN = concat("UserAlreadyChannelAdmin")
USER_ALREADY_EXIST = concat("UserAlreadyExist")
InvalidReferralCode = concat("InvalidReferralCode")
MultipleReferralCodeObjectFound = concat("MultipleReferralCodeObjectFound")
TIMELINE_TYPE_IS_MUST = concat("timelinetypeismust")
FLD_IS_CANNOT_BE_EDITED = concat("FieldCannotBeEdited")
KEYWORD_ALREADY_EXIST = concat("KeywordAlradyExist")
KEYWORD_DELETED = concat("KewordDeleted")
ONLY_GROUP_MEMBER_CAN_DO_THIS = concat("OnlyGroupMemberCanDoThis")
ONLY_CREATOR_CAN_EDIT_OR_DELETE_THIS = concat("OnlyCreatorCanEditOrDeleteThis")
GROUPNOTE_NOT_EXIST = concat("GroupNoteNotExist")
GROUP_ID_IS_MUST = concat("GroupIdIsMust")
ONLY_OWNER_CAN_DO_THIS = concat("OnlyOwnerCanDoThis")
YOU_ALREADY_HAVE_A_NUMBER = concat("YouAlreadyHaveANumber")
PLEASE_CHECK_T_AND_C = concat("PleaseCheckTAndC")
COMMENT_NOT_EXIST = concat("CommentNotExist")
REFERRAL_CODE_IS_INVALID = concat("RererralCodeIsInvalid")
USER_DO_NOT_HAVE_PHONE_NUMBER = concat('UserDoNotHavePhoneNumber')
YOU_DO_NOT_HAVE_SUFFICIENT_BALANCE = concat('YouDoNotHaveSufficientBalance')
YOU_CAN_NOT_EXCHANGE_LESS_THEN_FIVE_TOUKU_POINTS = concat('YouCanNotExchangeLessThenFiveToukuPoints')
# XIGOLO PAYMENT APP ERROR MESSAGES

AMT_FIELD_IS_REQUIRED = concat("AmountFieldIsRequired")
CRYPTO_TYPE_IS_REQUIRED = concat("CryptoTypeIsRequired")
INVALID_USER_WALLET = concat("InvalidUserWallet")
PICKED_OPTION_REQUIRED = concat("PickedOptionRequired")

# TERAMINE

UNIT_FIELD_REQUIRED = concat("UnitFieldRequired")

# XANA OTC APP ERROR MESSAGES


ODR_TYP_REQUIRED = concat("OrderTypeRequired")
CURRENCY_TYP_PARAM_REQUIRED = concat("CurrencyTypeParamRequired")
ODR_TYP_NOT_VALID_CHOICE = concat("OrderTypeNotValidChoice")
ODR_ID_REQUIRED = concat("OrderIdRequired")
SELECTED_SELL_ODR_CLOSED = concat("SelectedSellOrderClosed")
WLT_ID_REQUIRED = concat("WalletIdRequired")
INVALID_USR_WLT = concat("InvalidUserWallet")
SELECTED_BUY_ODR_CLOSED = concat("SelectedBuyOrderClosed")
PRICE_FIELD_IS_REQUIRED = concat("PriceFieldIsRequired")
MIN_AMOUNT_FIELD_IS_REQUIRED = concat("MinAmountFieldIsRequired")
CONVERT_CURRENCY_TYP_FIELD_IS_REQUIRED = concat("ConvertCurrencyTypeFieldIsRequired")
PAYMENT_MTD_FIELD_IS_REQUIRED = concat("PaymentMethodsFieldIsRequired")
DONT_HAVE_ENOUGH_BALANCE = concat("DontHaveEnoughBalance")
ODR_NOT_FOUND = concat("OrderNotFound")
SELL_ODR_ALL_IN_PROGRESS = concat("SellOrderAllIn-Progress")
ODR_ALREADY_COMPLETED = concat("OrderAllReadyCompleted")
ODR_FAILURE = concat("OrderFailure")
ODR_ALLREADY_CANCELED = concat("OrderAllReadyCanceled")
MESSAGE_REQUIRED = concat("MessageRequired")
ODR_DEAD_LINE_OVERED = concat("OrderDeadlineOvered")
PAYMENT_DONE_BY_USER = concat("PaymentDoneByUser")
ODR_PAYMENT_NOT_COMPLETED = concat("OrderPaymentNotCompleted")
RELEASE_DONE_BY_USER = concat("ReleaseDoneByUser")
RATE_REQUIRED = concat("RateRequired")
AUTO_RELEASE_DONE_BY_SYSTEM = concat("AutoReleaseDoneBySystem")
REGISTER_BONUS_ALREADY_RECEIVED = concat("RegisterBonusAlreadyReceived")

# XANA NFT APP ERROR MESSAGES

TO_REQUIRED = concat("ToRequired")
TOKEN_ID_REQUIRED = concat("TokenIdRequired")
TOKEN_URI_REQUIRED = concat("tokenUriRequired")
OWNER_REQUIRED = concat("ownerRequired")
SPENDER_REQUIRED = concat("spenderRequired")
IS_PROXY_REQUIRED = concat("isProxyRequired")
FROM_REQUIRED = concat("fromRequired")
OPERATOR_REQUIRED = concat("operatorRequired")
APPROVED_REQUIRED = concat("approvedRequired")
SELL_TYPE_REQUIRED = concat("SellTypeRequired")
CRYPTO_TOKEN_REQUIRED = concat("CryptoTokenRequired")
TYPE_REQUIRED = concat("TypeRequired")
BUY_TYPE_REQUIRED = concat("BuyTypeRequired")

# USER HEAVEN ERROR MESSAGE

ERROR_ULTRA_HEAVEN = concat("ErrorUltraHeaven")
COMING_SOON = concat("ComingSoon")
NO_USER_WITH_ID = concat("NoUserWithId")
YOU_CANNOT_OTC_LESS = concat("YouCanNotOtcLess")
HID_REQUIRED = concat("HidRequired")
INVALID_OLD_HEAVEN = concat("InvalidOldHeaven")
RELEASE_SETTINGS_REQUIRED = concat("ReleaseSettingsRequired")
NO_WALLET_FOR_CURRENCY = concat("NoWalletForCurrency")
CANNOT_RELEASE_MORE_DAY_AND_MONTH = concat("CannotReleaseMoreDayAndMonth")
VARIFY_KYC_FOR_AMOUNT_RELEASE = concat("VarifyKYCForAmountRelease")
NO_USER_WALLET_FOR_USER = concat("NoUserwalletForUser")
ERROR_NODE_JS = concat("ErrorNodeJs")
CANNOT_CREATE_HEAVEN = concat("CannotCreateHeaven")
CANNOT_QUICK_SELL_LESS = concat("CanNotQuickSellLess")
INVALID_HEAVEN_USERNAME = concat("InvalidHeavenUsername")
ANX_AMOUNT_REQUIRED = concat("AnxAmountRequired")
CANNOT_RELEASE_MORE = concat("CannotReleaseMore")
HEAVEN_NOT_FOUND = concat("HeavenNotFound")
CANNOT_QUICK_SELL_MORE_THEN_BALANCE = concat("CanNotQuickSellMoreThenBalance")
CANNOT_RELEASE_MORE_THEN_DAY_MONTH = concat("CannotReleaseMoreThenDayMonth")
PLAN_REQUIRED = concat("PlanRequired")
INVALID_RELEASE_SETTINGS = concat("InvalidReleaseSettings")
USER_WALLET_REQUIRED = concat("UserWalletRequired")
OLD_HEAVEN_REQUIIRED = concat("OldHeavenRequiired")
NOT_ENOUGH_ANX_FOR_HEAVEN_TRANSFER = concat("NotEnoughAnxForHeavenTransfer")
KYC_REQUIRED = concat("KYCRequired")
WILL_PROCESS_HEAVEN_RELEASE_MANUALLY = concat("WillProcessHeavenReleaseManually")
CANCLE_HEAVEN_DISABLED = concat("CancleHeavenDisabled")
INVALID_WALLET = concat("InvalidWallet")
INVEST_AMOUNT_REQUIRED = concat("InvestAmountRequired")
HEAVEN_ID_REQUIRED = concat("HeavenIdRequired")
INVALID_HEAVEN_ID = concat("InvalidHeavenId")
CANNOT_QUICK_SELL = concat("CanNotQuickSell")
NEW_PLAN_REQUIRED = concat("NewPlanRequired")
CANNOT_CREATE_HEAVEN_LESS = concat("CannotCreateHeavenLess")

# USER COUPON ERROR MESSAGE

REWARD_DISTRIBUTION = concat("RewardDistributed")

# CORE ERROR MESSAGE

EMAIL_SEND_SUCCESSFULLY = concat("EmailSendSuccessfully")
EMAIL_OTP_SEND_SUCCESSFULLY = concat("EmailOtpSendSuccessfully")
INVALID_TRADE_PASSWORD = concat("InvalidTradePassword")
OTP_VERIFIED = concat("OtpVerified")
TRADE_PASSWORD_REQUIRED = concat("TradePasswordRequired")
ANSWER_REQUIRED = concat("AnswerRequired")
CODE_NOT_VALID = concat("CodeNotValid")
PASSWORD_REQUIRED = concat("PasswordRequired")
SECURITY_ANSWER_NOT_VALID = concat("SecurityAnswerNotValid")
SPECIFIC_USER_LOGIN = concat("SpecificUserLogin")
SECURITY_QUESTION_NOT_FOUND = concat("SecurityQuestionNotFound")
USER_WALLET_FIELD_REQUIRED = concat("UserWalletFieldRequired")
INVITE_USER_EMAIL_SUCCESS = concat("InviteUserEmailSuccess")
INVAILD_TOKEN = concat("InvaildToken")
INVALID_ADDRESS = concat("InValidAddress")
WRONG_USER_ID = concat("WrongUserId")
USER_NOT_FOUND_CHECK_FIRST_LAST_USERNAME = concat("UserNotFoundCheckFirstLastUsername")
COUNTRY_UPDATED = concat("CountryUpdated")
VALID_ADDRESS = concat("ValidAddress")
COUPON_CODE_NOT_VALID = concat("CouponCodeNotValid")
QUESTION_REQUIRED = concat("QuestionRequired")
CURRENCY_NOT_FOUND = concat("CurrencyNotFound")
ENTER_PASSWORD_OR_CODE = concat("EnterPasswordOrCode")
WRONG_CREDENTIALS = concat("WrongCredentials")
REFERRAL_USER_NOT_FOUND = concat("ReferralUserNotFound")
TRY_AGAIN = concat("TryAgain")
INVALID_CURRENT_PASSWORD = concat("InvalidCurrentPassword")
OTP_NOT_CORRECT = concat("OTPNotCorrect")
DESTINATION_ADDRESS_FIELD_REQUIRED = concat("DestinationAddressFieldRequired")
LAST_NAME_REQUIRED = concat("LastNameRequired")
NOT_ENOUGH_AMOUNT_IN_WALLET = concat("NotEnoughAmountInWallet")
USER_ACCOUNT_DISABLED_MINUTE = concat("UserAccountDisabledMinute")
WRONG_CREDENTIALS_PLEASE_PROVIDE_RIGHT_CREDENTIAL = concat(
    "PleaseProvideRightCredential"
)
USER_ACCOUNT_HAS_BEEN_DISABLED = concat("UserAccountHasBeenDisable")
USER_ACCOUNT_DISABLED_FOR_ONE_MINUTE = concat("UserAccountDisabledForOneMinute")
USER_ACCOUNT_DISABLED_FOR_FIVE_MINUTE = concat("UserAccountDisabledForFiveMinute")
USER_ACCOUNT_DISABLED_FOR_FIFTEEN_MINUTE = concat("UserAccountDisabledForFifteenMinute")
USER_ACCOUNT_DISABLED_FOR_THIRTY_MINUTE = concat("UserAccountDisabledForthirtyMinute")
USER_NAME_REQUIRED = concat("UsernameRequired")
OTP_NOT_VERIFIED = concat("OtpNotVerified")
NODE_API_ERROR = concat("NodeApiError")
ACCOUNT_DISABLED_CONTACT_SUPPORT = concat("AccountDisabledContactSupport")
INVITATION_CODE_IS_REQUIRED = concat("InvitationCodeIsRequired")
REFERRAL_CODE_REQUIRED = concat("ReferralCodeRequired")
FIELD_REQUIRED = concat("FieldRequired")
NO_USER_KYC_INFORMATION = concat("NoUserKYCInformation")
REQUIRED_EMAIL_IN_GET = concat("RequiredEmailInGet")
USER_TYPE_REQUIRED = concat("UserTypeRequired")
EMAIL_NOT_FOUND = concat("EmailNotFound")
EMAIL_NOT_VALID = concat("EMAIL_NOT_VALID")
ACCOUNT_DISABLED_CONTACT_SUPPORT_TO_ENABL = concat(
    "AccountDisabledContactSupportToEnableIt"
)
TOKEN_REQUIRED = concat("TokenRequired")
INVALID_USERNAME = concat("InvalidUsername")
CHECK_FIRST_NAME_LAST_NAME = concat("CheckFirstNameLastName")
CODE_REQUIRED = concat("CodeRequired")
NO_USER_HEAVEN_FOUND = concat("NoUserHeavenFound")
PASSWORD_RESET = concat("PasswordReset")
SERVER_ERROR_FETCH_WALLET_BALANCE = concat("ServerErrorFetchWalletBalance")
FAN_OT_SETUP = concat("FANotSetup")
USER_NOT_EXIST = concat("UserNotExist")
USER_NOT_EXIST_IN_TOUKU = concat("UserNotExistInTouku")
USER_NAME_REQUIRED_SENSITIVE = concat("UsernameRequiredSensitive")
TRANSFER_AMOUNT_FIELD_REQUIRED = concat("TransferAmountFieldRequired")
UNABLE_TO_PROCESS_CONTACT_SUPPORT = concat("UnableToProcessContactSupport")
OTP_SEND = concat("OTPSend")
USER_NAME_NOT_ALLOWED = concat("UsernameNotAllowed")
USER_NAME_ALREADY_EXIST = concat("UsernameAlreadyExist")
U_MOB_NUB_HAV_REACHED_ALLOWED_ACC = concat("YreMobNumHaveReachAllowedAccount")
UR_PASS_AND_CONFRM_PASS_DONT_MATCH = concat("YourPassAndConfrmPassDontMatch")
EMAIL_REQUIRED = concat("Emailrequired")
CANT_CREATE_INVESTMENT_MORE_LESS = concat("CantCreateInvestmentMoreLess")
XP_QUANTITY_IS_REQUIRED = concat("XpQuantityIsRequired")
UNABLE_TO_LOGIN = concat("UnableToLogin")
AUTH_FAILED = concat("AuthFailed")
TELEGRAM_AUTH_DATA = concat("TelegramUnAuthData")
DATA_NOT_RELATED_TELEGRAM = concat("DataNotRelatedTelegram")
TRANSACTION_COMPLETED = concat("TransactionCompleted")
USERNAME_NOT_VALID = concat("UsernameNotValid")
EMAIL_PHONE_NOT_EXIST = concat("EmailPhoneDoesNotExistPleaseUpdate")
MINER_FEE_TYPE_REQUIRED = concat("MinerFeeTypeRequired")
USE_DIFFERENT_PASSWORD = concat("YouCanNotUseOldPasswordAsNewPassword")
USE_DIFFERENT_TRADE_PASSWORD = concat("YouCanNotUseOldTradePasswordAsNewTradePassword")
USER_SESSION_ACTIVE = concat("UserAlreadyLoggedInFromAnotherDevice")
SERVICE_NOT_AVAILABLE = concat("ServiceNotAvailable")
THROTTLED = concat("RequestLimitExceeded")

# CRYPTO RACE ERROR MESSAGE

INVALID_CRYPTO_RACE_ID = concat("InvalidCryptoRaceId")
YOU_CANNOT_BET_MORE_THAN = concat("YouCanNotBetMoreThan")
CRYPTO_RACE_ID_REQUIRED_FIELD = concat("CryptoRaceIdRequiredField")
ENTER_VALID_CRYPTO_ID = concat("EnterValidCryptoId")
ANGEL_LIST_CRYPTO_AMOUNT_REQUIRED = concat("AngelListCryptoAmountRequired")
ERROR_FROM_NODE_JS_SERVER = concat("ErrorFromNodejsServer")
NO_RACE_FOUND = concat("NoRaceFound")
PLEASE_ENTER_CRYPTO_RACE_ID = concat("PleaseEnterCryptoRaceId")
WALLET_HAS_NOT_MUCH_AMOUNT_CREATE_THIS_BAT = concat(
    "WalletHasNotMuchAmountCreateThisBat"
)
ERROR_WHILE_FETCHING_USER_BALANCE_TRY_AGAIN = concat(
    "ErrorWhileFetchingUserBalanceTryAgain"
)
CRYPTO_RACE_NOT_FOUND = concat("CryptoRaceNotFound")
CRYPTO_RACE_ID_REQUIRED = concat("CryptoRaceIdRequired")
ANGEL_LIST_ANGEL_TYPE_REQUIRED = concat("AngelListAngelTypeRequired")
ANGEL_LIST_REQUIRED = concat("AangelListRequired")
ANGEL_TYPE_REQUIRED = concat("AngelTypeRequired")
NOT_FOUND = concat("NotFound")

# EXCHANGE2 ERROR MESSAGE

PRIMARY_WALLET_REQUIRED = concat("PrimaryWalletRequired")
HAVE_ENOUGH_AMOUNT_IN_YOUR = concat("HaveEnoughAmountInYour")
NOT_ENOUGH_BALANCE_IN = concat("NotEnoughBalanceIn")
PRIMARY_WALLET_BALANCE_NOT_FOUND = concat("PrimaryWalletBalanceNotFound")
SECONDARY_WALLET_NOT_FOUND = concat("SecondaryWalletNotFound")
SEND_TO_REQUIRED = concat("SendToRequired")
AMOUNT_FIELD_IS_REQUIRED = concat("AmountFieldIsRequired")
PRIMARY_WALLET_IS_WRONG = concat("PrimaryWalletIsWrong")
NOT_ENGH_BAL_IN = concat("NotEnoughBalanceIn")

# ANGEL RACE ERROR MESSAGE

MINIMUM_XP_FOR_BET = concat("MinimumXPForBet")
WALLET_NOT_MUCH_AMOUNT_CREATE_BAT = concat("WalletNotMuchAmountCreateBat")
YOU_ARE_LOSTED_LAST_GAME = concat("YouAreLostedLastGame")
ERROR_FETCHING_BALANCE = concat("ErrorFetchingBalance")
LAST_GAME_RESULTS_NOT_DECLARED = concat("LastGameResultsNotDeclared")
YOU_NOT_PLAY_LAST_GAME = concat("YouNotPlayLastGame")
ANGEL_LIST_REQUIRED_FIELD = concat("Angel_listRequiredField")
ENTER_CRYPTO_RACE_ID = concat("EnterCryptoRaceId")
CRYPTO_RACE_REQUIRED = concat("CryptoRaceRequired")
TOTAL_CRYPTO_AMOUNT_REQUIRED = concat("TotalCryptoAmountRequired")
ERROR_NODE_JS_SERVER = concat("ErrorNodejsServer")
CRYPTO_AMOUNT_REQUIRED_FIELD = concat("CryptoAmountRequiredField")
NOT_BET_MORE = concat("NotBetMore")
BETTING_TIME_OVER = concat("BettingTimeOver")
CANNOT_BET_MORE = concat("CanNotBetMore")
LAST_GAME_NOT_FOUND = concat("LastGameNotFound")
PROFILE_PICTURE_NOT_FOUND = concat("ProfilePictureNotFound")

# ANGEL TOSS ERROR MESSAGE

CRYPTO_TOSS_NOT_FOUND = concat("CryptoTossNotFound")
PLEASE_ENTER_CRYPTO_TOSS_ID = concat("PleaseEnterCryptoTossId")
CRYPTO_AMOUNT_IS_REQUIRED = concat("CryptoAmountIsRequired")
TOSS_IS_REQUIRED_FIELD = concat("TossIsRequiredField")
CRYPTO_TOSS_ID_IS_REQUIRED_FIELD = concat("CryptoTossIdIsRequiredField")
LAST_GAME_HAVE_SOME_ERROR = concat("LastGameHaveSomeError")
NO_GAME_FOUND = concat("NoGameFound")
BETTING_TIME_OVER_OF_THAT_GAME = concat("BettingTimeOverOfThatGame")

# ANGEL TURBO ERROR MESSAGE

INVALID_CRYPTO_TURBO_ID = concat("InvalidCryptoTurboId")
CRYPTO_BET_REQUIRED = concat("CryptoBetRequired")
MULTIPLIER_REQUIRED = concat("MultiplierRequired")

# ANT ERROR MESSAGE

AMT_MUST_B_FRM_AVAILABLE_PKG = concat("AmountMustBeFromAvailablePackages")
ONLY_ONE_ACTIVE_PLAN_AT_A_TIME = concat("YouCanOnlyHaveOneActivePlanAtATime")
PKG_HAS_SAME_GT_PARENT_ACC = concat("PackageHasSameGreaterThenParentAccount")
AU_IS_DISABLED_FOR_NOW = concat("AuIsDisabledForNow")
YOU_DONT_HAV_MINED_HP_AMT = concat("YouDontHaveMinedHpAmount")
NOT_HAV_ENGH_HP_ACC = concat("NotHaveEnoughHPAccount")
NOT_HAV_ENGH_AMT_YOUR = concat("NotHaveEnoughAmountYour")
GVN_HEAVEN_USR_NAME_NOT_VALID = concat("GivenHeavenUsernameNotValid")
SECONDARY_BALANCE_NOT_FOUND = concat("SecondarBalanceNotFound")
SOME_THING_WENT_WRONG_TRY_AGAIN = concat("SomethingWentWrongTryAgain")
U_NOT_HAV_REQ_BAL_IN_RELEASE_ACC = concat("YouNotHaveRequestedBalanceInReleaseAccount")
MIN_REQUIRED_FOR_HEAVEN_OUT = concat("MinimumRequiredForHeavenOut")
USR_PRIMARY_WLT_NOT_FOUND = concat("UserPrimaryWalletNotFound")
U_CAN_NOT_RELEASE_MORE_DOLLAR_PER_MONTH = concat("YouCanNotReleaseMoreDollarPerMonth")
U_CAN_NOT_RELEASE_MORE_DOLLAR_PER_DAY = concat("YouCanNotReleaseMoreDollarPerDay")
ANT_WLT_NOT_FOUND = concat("AntWalletNotFound")
THERE_IS_NOT_USR_WITH_THIS_ID = concat("ThereIsNotUserWithThisId")
PLEASE_TRY_AFTER_SOME_TIME = concat("PleaseTryAfterSometime")
U_DONT_HAV_ENGH_AMT_IN_YOUR_WLT = concat("YouDontHaveEnoughAmountInYourWallet")
GIVEN_HEAVEN_USR_NAME_NOT_VALID = concat("GivenHeavenUsernameNotValid")
SECONDARY_WAL_BALANCE_NOT_FOUND = concat("SecondaryWalletBalanceNotFound")
NOT_ENGH_BAL_IN_SECONDARY_WAL = concat("NotEnoughBalanceInSecondaryWallet")
USR_WAL_BAL_NOT_FOUND = concat("UserWalletBalanceNotFound")
U_DONT_HAV_SUFFICIENT_BAL = concat("YouDontHaveSufficientBalance")
PLEASE_ENTER_TYHE_VALID_USR_NAME = concat("PleaseEnterTheValidUsername")
UNABLE_TO_FETCH_YOUR_WAL_BAL = concat("UnableToFetchYourWalletBalance")
DONT_HAV_ENGH_AMT_TO_TRANSFER = concat("DontHaveEnoughAmountToTransfer")

# ANV ERROR MESSAGE
HARVEST_PLAN_NOT_ALLOWED_TO_REINVEST = concat("HarvestPlanIsNotAllowedToReInvest")
SEED_VALUE_REQUIRED = concat("SeedValueRequired")
WLT_NOT_FOUND_FOR_THIS_CURRENCY = concat("WalletNotFoundForThisCurrency")
U_DONT_HAV_ENGH_AMT_IN_YOUR_WLT_TO_CREATE = concat(
    "YouDontEnghAmtInYourWltToCreateThis"
)
U_DONT_HAV_ENGH_USDV_AMT_TO_CREATE_HEAVEN = concat(
    "YouDontHaveEnghUsdvAmtToCreateHeaven"
)
U_DONT_HAV_ENGH_USDV_AMT_TO_HEAVEN = concat("YouDontHaveEnghUsdvAmntToHeaven")
ONLY_TWO_ACTIVE_PLAN_AT_A_TIME = concat("YouCanOnlyHave2ActiveHeavenAtATime")
HID_IS_REQUIRED_FIELD = concat("HidIsRequiredField")
RELEASE_SETTINGS_NOT_VALID_CHOICE = concat("ReleaseSettingsNotValidChoice")
HARVEST_ID_REQUIRED = concat("HarvestIdRequired")
U_NOT_RELEASE_AMT_BE4_KYC_VERIFY_IS_CNFMD = concat(
    "YouNotReleaseAmountBeforeKycVerificationIsCnfmd"
)
OTC_CURRENTLY_DISABLE = concat("OTCCurrentlyDisable")
NOT_ENGH_AMT_TO_TRANSFER_YOUR_WALLET = concat("NotHaveEnoughAmountToTransferYourWallet")
USER_NAME_FIELD_REQUIRED = concat("UsernameFieldIsRequired")
WALLET_TYPE_REQUIRED = concat("WalletTypeRequired")
TARGET_USER_WALLET_NOT_FOUND = concat("TargetUserWalletNotFound")
ONLY_TRANSFER_UPTO_UP_OR_DOWNLINE_USERS = concat("OnlyTransferToUpOrDownlineUsers")
TRANSFER_USER_NOT_FOUND = concat("TransferUserNotFound")
NOT_HAV_ENGH_AMT_TO_TRANSFER_IN_UR_WLT = concat("NotHaveEnoughAmtToTransferInYourWlt")
SOME_THING_WENT_WRONG_TRY_AFTER_SM_TIME = concat(
    "SomethingWentWrongPlsTryAfterSometime"
)
TRANSFER_SUCCESS = concat("TransferSuccess")
TRANSFER_FAILED_TRY_AFTER_SM_TIME = concat("TransferFailedPlsTryAfterSometime")
ANV_AMT_REQUIRED = concat("AnvAmountRequired")
CANNOT_OTC_MORE_THAN_AVAIL_BAL = concat("CanNotOtcMoreThanAvlBalance")
CAN_TRANSFER_MIN_MAX_ANV = concat("CanTransferMinMaxAnv")
OTC_NOt_ALLOW_4_USDV_TO_USDT_PAIR = concat("OtcNotAllowedForUsdvToUsdtPair")
ORDER_ID_REQUIRED = concat("OrderIDRequired")
REQUESTED_OTC_NOT_FOUND = concat("RequestedOtcNotFound")
OTC_APPROVED_SUCCESSFULLY = concat("OtcApprovedSuccessfully")
UNABLE_TO_FETCH_DATA_FROM_HEAVEN = concat("UnableToFetchDataForHeaven")
OTC_REQ_CANCELLED_SUCCESSFULLY = concat("OtcRequestCancelledSuccessfully")
CANNOT_TRANSFER_MORE_THAN_AVAILABLE_ANV = concat("CanNotTransferMoreThanAvailableAnv")

# ANV 2 ERROR MESSAGE
USER_NOT_HAVE_MEMBER_TYPE = concat("UserNotHaveMemberType")
PLAN_DAY_REQUIRED = concat("PlanDaysRequired")
PACKAGE_HAS_TO_BE_SAME_GREATER_THAN = concat("PackageHasToBeSameOrGreaterThen")
HAVE_ENGH_HP_IN_UR_MINED_ACC = concat("HaveEnoughHpInYourMinedAccount")
NEED_DOWN_LINE_FOR_HEAVEN_OUT = concat("NeedDownlineForHeavenOut")
NOT_HAV_REQUESTED_BAL_IN_RELEASE_ACC = concat("NotHaveRequestedBalanceInReleaseAccount")
ANV_WALLET_NOT_FOUND = concat("AnvWalletNotFound")
PLAN_DAYS_FLD_REQUIRED = concat("Plan_daysFieldIsRequired")
AMOUNT_AVAIL_PKG = concat("AmountAvailablePackages")
ENTER_THE_VALID_USERNAME = concat("EnterTheValidUsername")
NOT_FETCH_UR_WAL_BAL_TRY_AFTR_SM_TIME = concat(
    "UnableFetchWalletBalanceTryAfterSometime"
)
SLCTD_PAIR_IS_NOT_ALLOWED_FOR_OTC = concat("SelectedPairIsNotAllowedForOtc")
CAN_TRANSFER_MIN_MAX_AU = concat("CanTransferMinMaxAU")
QUIK_SELL_ODR_CREATED_SUCCESSFULLY = concat("QuickSellOrderCreatedSuccessfully")
ALREADY_APPROVED_THAT_OTC = concat("AlreadyApprovedThatOtc")

# ANX_LOTTERY ERROR MESSAGE

NO_LOTTERY_FOUND = concat("NoLotteryFound")
BET_NUM_REQUIRED = concat("BetNumberRequired")
LOTTERY_ID_REQUIRED = concat("LotteryIdRequired")
CURRENCY_TYP_FIELD_IS_REQUIRED_OR_INVALID = concat(
    "CurrencyTypeFieldIsRequiredOrInValid"
)
INVALID_LOTTERY_ID = concat("InvalidLotteryId")
U_CAN_NOT_PLACE_FREE_BET_4_THIS_LOTTERY = concat("YouCanNotPlaceFreeBetForThisLottery")
UR_WLT_HAS_NOT_MUCH_AMT_TO_CREATE_THIS_BAT = concat(
    "YourWalletHasNotMuchAmountToCreateThisBat"
)
PLEASE_ENTR_LOTTRY_ID = concat("PleaseEnterLotteryId")
PLS_ENTR_LOTRY_ID = concat("PleaseEnterLotteryId")
WLT_OR_LOTRY_DOES_NOT_EXIST = concat("WalletOrLotteryDoesNotExist")
USER_CAN_BET = concat("UserCanBet")
USR_CANNOT_BET_DUE_TO_INSUFFICIENT_BAL = concat("UserCannotBetDueToInsufficientBalance")

# BOT API ERROR MESSAGE

TYPE_IS_REQUIRED = concat("TypeIsRequired")
PAIR_IS_REQUIRED = concat("PairIsRequired")
ACTIVE_IS_REQUIRED = concat("ActiveIsRequired")
LIQUIDITY_TARGET_IS_REQUIRED = concat("LiquiditytargetIsRequired")
USER_ID_IS_REQUIRED = concat("UserIdIsRequired")
TASK_ID_IS_REQUIRED = concat("TaskIdIsRequired")
START_TIME_IS_REQUIRED = concat("StarttimeIsRequired")
END_TIME_IS_REQUIRED = concat("EndtimeIsRequired")
TARGET_IS_REQUIRED = concat("TargetIsRequired")
PRICE_TARGET_IS_REQUIRED = concat("PricetargetIsRequired")
VOLUME_TARGET_IS_REQUIRED = concat("VolumetargetIsRequired")

# CHANGE ERROR MESSAGE
THE_EMAIL_IS_ALREADY_REGISTERED = concat("TheEmailIsAlreadyRegistered")
PHONE_NUM_CHANGED_SUCCESSFULLY = concat("PhoneNumberChangedSuccessfully")
VERIFICATION_CODE_NOT_CORRECT = concat("VerificationCodeNotCorrect")
EMAIL_CHANGED_SUCCESSFULLY = concat("EmailChangedSuccessfully")
PHONE_NUM_ALREADY_REGISTERED = concat("PhoneNumberAlreadRegistered")
UPGRADE_AS_MAX_LIMT_REACH = concat("YreMobNumHaRechAllowAcToRegMoreConsiUpgrading")
GET_ANOTHER_OTP = concat("GetAnotherOtp")
EMAIL_ALREADY_EXIST = concat("EmailAlreadRegistered")
# COIN FLIP ERROR MESSAGE
COIN_SIDE_REQUIRED = concat("CoinSideRequired")
INSUFFICIENT_AMOUNT_TO_CREATE_BAT = concat("InsufficientAmountToCreateBat")
ERROR_FETCHING_BALANCE_TRY_AGAIN = concat("ErrorFetchingBalanceTryAgain")
UNABLE_TO_FLIP_COIN_TRY_AGAIN = concat("UnableToFlipCoinTryAgainE")

# NEWS ERROR MESSAGE
NEWS_NOT_EXIST = concat("Newsnotexist")

# OTC API ERROR MESSAGE
BUY_IS_REQUIRED_FIELD = concat("backend.common.BuyIsRequiredField")

# QR CODE CHECK ERROR MESSAGE
TICKET_DOES_NOT_EXIST = concat("TicketDoesNotExist")
FAILED_TICKET_IS_USED = concat("FailedTicketIsUsed")
SUCCESS_VALID_TICKET = concat("SuccessValidTicket")
FAILED_INVALID_TICKET = concat("FailedInvalidTicket")

# SECURITY QUESTION ERROR MESSAGE

USER_QUES_NOT_FOUND = concat("UserQuestionNotFound")
USER_SECURITY_QUES_ALREADY_ADDED = concat("UserSecurityQuestionAllreadyAdded")
USER_SECURITY_QUES_NOT_FOUND = concat("UserSecurityQuestionNotFound")

# METAVERSE ERROR MESSAGE
CRYPTO_IS_REQUIRED_PARAM = concat("CryptoIsRequiredParameter")
WAL_BAL_LESS_THAN_BET_AMT = concat("YrWltBalanceIsLesserThanBatAmt")
SOME_THING_WENT_WRONG_VAL_TRY_AFTER_SM_TIME = concat(
    "SomethingWentWrgvaluePlsTryAfterSometime"
)
SOME_THING_WENT_WRONG_IN_PLACING_BET = concat("SomethingWentWrongInPlacingBet")
REWARD_SENT_SUCCESSFULLY = concat("RewardSentSuccessfully")
SOME_THING_WENT_WRONG_SEND_REWARD_TO_WINNER = concat(
    "SomethingWentWrongSendRewardToWinner"
)
USR_NOT_AUTHORIZ_UPDAT_CHANEL_DETAIL = concat("UserNotAuthorizeUpdateChannelDetails")
TRANSACTION_INCOMPLETE_FRM_NODE = concat("TransactionInCompleteFromNode")
USR_EXISTED_FRM_CHANEL_SUCCESSFULLY = concat("UserExitedFromChannelSuccessfully")
# HEAVEN ERROR MESSAGE

CRTHVN_IS_DISABLED_AT_THE_MOMENT = concat("CrtHvnIsDisabledAtTheMoment")
HVN_AMT_REQUIRED = concat("HeavenAmountRequired")
CANT_CRTHVN_MORE_THEN_LESS = concat("CantCrtHvnMoreThanLess")
YOU_CANT_CRTHVN_WITHIN = concat("YouCantCrtHvnWithin")
U_NOT_TRANSFER_MORE_THAN_AVAILABLE_ANX = concat("YouCanNotTransferMoreThanAvailableAnx")
WE_WILL_PROCESS_UR_HVN_RELEASE_MANUALLY_SOON = concat(
    "WeWillProcessYourHeavenReleaseManuallySoon"
)
U_DONT_HAV_ENGH_ANX_TO_TRANSFER_THIS_HVN = concat("YDontHaveEnghAnxToTrnsferThisHeaven")
DATA_NOT_FOUND = concat("DataNotFound")
TX_HASH_REQUIRED = concat("txhashRequired")
NOTE_REQUIRED = concat("noteRequired")

# FRUIT GAME ERROR MESSAGE
ERR_RETRIEVING_SHOPLIST = concat("ErrorRetrievingShopList")
ERROR_KYC_UPDATE = concat("ErrorKYCUpdate")
BANK_DETAIL_NOT_FOUND = concat("BankDetailNotFound")
PLEASE_ADD_BANK_DETAIL_TO_PROCEED = concat("PleaseAddBankDetailToProceed")
YOU_HAVE_FRUITS_IN_THIS_ACC = concat("YouHaveFruitsInThisAccount")
FRUIT_ODR_HISTORY_NOT_FOUND = concat("FruitOdrHistoryNotFound")
PAYMENT_FAILED = concat("PaymentFailed")
ERR_RETRIEVING_HISTORY_LIST = concat("ErrorRetrievingHistoryList")
THIS_FLD_IS_REQUIRED = concat("Thisfieldisrequired")
ODR_ALREADY_RELEASED = concat("OrderAlreadyReleased")
ODR_OK_NOTED = concat("OrderOkNoted")
TRANSLATION_CAPTR_FAIL_CONTACT_SUPPORT = concat(
    "TranslationCaptureProcessFailedPlsContactSupport"
)
FIELD_NOT_NULL = concat("FieldNotNull")
PLAN_NOT_ALLOWED_REINVEST = concat("PlanNotAllowedReinvest")
FRUIT_ODR_UNDER_INVESTIGATION = concat("FruitOrderUnderInvestigation")
MULTIPLE_FGP_WLT_RETURN = concat("MultipleFGPWltReturn")
MULTIPLE_SC_WLT_RETURN = concat("MultipleSCWltReturn")
ORDER_CAPTURED_PAYPAL = concat("OrderAlreadyCaptured")
NOTIFICATION_RELATED_USER = concat("NotificationRelatedUser")
USER_PENALTY_MESSAGE = concat("UserPenaltyMessage")
ERROR_MINIMUM_LIMIT_OF_SC_DEPOSIT = concat("ERROR_MINIMUM_LIMIT_OF_SC_DEPOSIT")
ERROR_MINIMUM_LIMIT_OF_FGP_DEPOSIT = concat("ERROR_MINIMUM_LIMIT_OF_FGP_DEPOSIT")
YOU_HAVE_MATCH_ORDER = concat("YOU_HAVE_MATCH_ORDER")
CRYPTO_MATCH_MSG_FOR_BUYER = concat("CRYPTO_MATCH_MSG_FOR_BUYER")
CRYPTO_MATCH_MSG_FOR_SELLER = concat("CRYPTO_MATCH_MSG_FOR_SELLER")
MSG_TO_BUYER_PENALTY_ON_BUYER = concat("MSG_TO_BUYER_PENALTY_ON_BUYER")
MSG_TO_SELLER_PENALTY_ON_BUYER = concat("MSG_TO_SELLER_PENALTY_ON_BUYER")
MSG_TO_BUYER_PENALTY_ON_SELLER = concat("MSG_TO_BUYER_PENALTY_ON_SELLER")
MSG_TO_SELLER_PENALTY_ON_SELLER = concat("MSG_TO_SELLER_PENALTY_ON_SELLER")
MSG_TO_SELLER_PENALTY_ON_BUYER_PAID = concat("MSG_TO_SELLER_PENALTY_ON_BUYER_PAID")
MSG_TO_BUYER_PENALTY_ON_SELLER_PAID = concat("MSG_TO_BUYER_PENALTY_ON_SELLER_PAID")
PENALTY_RECEIVE_MESSAGE = concat("PENALTY_RECEIVE_MESSAGE")
MSG_ON_ACCOUNT_SUSPENSION = concat("MSG_ON_ACCOUNT_SUSPENSION")
FRUIT_USER_PENALTY_ON_SELLER = concat("FRUIT_USER_PENALTY_ON_SELLER")
FRUIT_USER_PENALTY_ON_BUYER = concat("FRUIT_USER_PENALTY_ON_BUYER")
FRUIT_USER_MSG_TO_SELLER_PENALTY_ON_BUYER = concat(
    "FRUIT_USER_MSG_TO_SELLER_PENALTY_ON_BUYER"
)
FRUIT_USER_MSG_TO_BUYER_PENALTY_ON_SELLER = concat(
    "FRUIT_USER_MSG_TO_BUYER_PENALTY_ON_SELLER"
)
FRUIT_USER_MSG_TO_SELLER_PENALTY_ON_BUYER_PAID = concat(
    "FRUIT_USER_MSG_TO_SELLER_PENALTY_ON_BUYER_PAID"
)
FRUIT_USER_MSG_TO_BUYER_PENALTY_ON_SELLER_PAID = concat(
    "FRUIT_USER_MSG_TO_BUYER_PENALTY_ON_SELLER_PAID"
)
FRUIT_ORDER_RELEASED_MSG_TO_BUYER = concat("FRUIT_ORDER_RELEASED_MSG_TO_BUYER")
FRUIT_ORDER_RELEASED_MSG_TO_SELLER = concat("FRUIT_ORDER_RELEASED_MSG_TO_SELLER")
FRUIT_ORDER_CANCELED_MSG_TO_BUYER = concat("FRUIT_ORDER_CANCELED_MSG_TO_BUYER")
FRUIT_ORDER_CANCELED_MSG_TO_SELLER = concat("FRUIT_ORDER_CANCELED_MSG_TO_SELLER")
MSG_ON_LOW_BUY_BUDGET = concat("MSG_ON_LOW_BUY_BUDGET")
LET_START_TRADE_BANK_KAKAO_DETAIL = concat("LET_START_TRADE_BANK_KAKAO_DETAIL")
LET_START_TRADE_BANK_DETAIL = concat("LET_START_TRADE_BANK_DETAIL")
LET_START_TRADE_KAKAO_DETAIL = concat("LET_START_TRADE_KAKAO_DETAIL")
TRADE_BUY_ORDER_TIME_ERROR = concat("TRADE_BUY_ORDER_TIME_ERROR")


# PAYPAL ERROR MESSAGE
TRANSACTION_NOT_FOUND = concat("TransactionNotFound")
FAILED_TO_UPDATE_WALT_BALANCE = concat("FAILED_TO_UPDATE_WALT_BALANCE")
ORDER_ALREADY_CAPTURED = concat("ORDER_ALREADY_CAPTURED")
PAYMENT_FAILED_PLS_CONTACT_SUPPORT = concat("PAYMENT_FAILED_PLS_CONTACT_SUPPORT")


# XTICKET ERROR MESSAGE
INVALID_EVENT_ID = concat("InvalidEventId")
INVALID_PURCHASE_ID = concat("InvalidPurchaseID")
EVENT_ID_REQUIERD = concat("EventIdRequierd")
FAILED_TICKET_IS_USED = concat("FailedTicketIsUsed")
PURCHASE_ID_REQUIERD = concat("PurchaseIdRequierd")
TICKET_NOT_FOUND = concat("TicketNotFound")
NO_ACCESS_PERMISSION = concat("NoAccessPermission")
CANNOT_BUY_TICKET_0 = concat("CanNotBuyTicket0")
NOT_SUFFICIENT_BALANCE = concat("NotSufficientBalance")
FAILED_INVALID_TICKET = concat("FailedInvalidTicket")
INVALID_TICKET_ID_FOR_USER = concat("InvalidTicketIDForUser")
TOCKET_SOLD_BY_OTHER = concat("TocketSoldByOther")
SUCCESS_VALID_TICKET = concat("SuccessValidTicket")
NAME_REQUIRED = concat("NameRequired")


NODE_ERROR_CODES = {
    "600": "backend.common.BidLessThenMinimumPrice",
    "601": "backend.common.UserBTCBalanceLow",
    "609": "backend.common.UserETHBalanceLow",
    "608": "backend.common.InsufficientUserBalance",
    "610": "backend.common.InsufficientUserBalanceUSDT",
    "617": "backend.common.InsufficientUserBalance",
    "618": "backend.common.InsufficientUserBalance",
    "619": "backend.common.UserNotHaveNori",
    "623": "backend.common.UserNotHaveAU",
    "626": "backend.common.UserNotHaveSC",
    "650": "backend.common.CompnayLowBTC",  # original CompanyLowBalance this is to hide from user
    "651": "backend.common.CompnayLowBTC",
    "659": "backend.common.CompnayLowBTC",  # original CompanyLowETH
    "667": "backend.common.CompnayLowBTC",  # original CompanyNotEnoughXp
    "680": "backend.common.InvalidJWTFound",
    "701": "backend.common.TransferringLittleBTC",
    "702": "backend.common.TransferringLittleETH",
    "750": "backend.common.TotalLessThenFee",
    "751": "backend.common.DontHaveEnoughSatoshis",
    "752": "backend.common.MustHaveMinarFee",
    "753": "backend.common.DustAmountCreatedInOutput",
    "754": "backend.common.RemainBalanceToDustAmount",
    "755": "backend.common.EOSTransactionFailur",
    "756": "backend.common.TryAgianErrorCPUStake",
    "757": "backend.common.UnableToSendXpToUser",
    "758": "backend.common.FailedToTransferFunds",
    "759": "backend.common.WentWrongCreatingWallet",
    "760": "backend.common.WentWrongOverBloackchain",
    "761": "backend.common.UnableTOSendRawTransaction",
    "762": "backend.common.IntegerAmount",
    "785": "backend.common.CannotPurchaseQuoteCoin",
    "787": "backend.common.AmountTooLessForTransaction",
    "796": "backend.common.WrongTryAgain",
    "798": "backend.common.WaitPreviousTransactionNotConfirmed",
    "799": "backend.common.MustPayMinarFee",
    "900": "backend.common.MissingUserIdOrCoin",
    "901": "backend.common.InvalidUserAuthentication",
    "902": "backend.common.IncorrectUserType",
    "903": "backend.common.InvalidCryptoCurrenctType",
    "904": "backend.common.CoinNotSupportedForNow",
    "905": "backend.common.EOSAccountCheckFailed",
    "906": "backend.common.InvalidTokenId",
    "907": "backend.common.NoApprovedAccount",
    "908": "backend.common.NoAddressProvided",
    "910": "backend.common.IncorrectParameter",
    "911": "backend.common.NotANVUser",
    "912": "backend.common.CheckANVAndANTQuentity",
    "913": "backend.common.AccountAlreadyExist",
    "914": "backend.common.UsernameAlreadyExist",
    "915": "backend.common.InvalidToAddress",
    "916": "backend.common.OrderStructureNotValid",
    "917": "backend.common.TokenIdMandantory",
    "918": "backend.common.TokenIDAlreadyExpored",
    "951": "backend.common.PleaseContactAdministrator",
    "952": "backend.common.ComingSoon",
    "953": "backend.common.ThisCoinNotAllowedToTransfer",
    "954": "backend.common.CannotAcceptOrderDueToAmount",
    "955": "backend.common.DeductionNotPossible",
    "956": "backend.common.AmountMustBeGreater",
    "957": "backend.common.OrderRejected",
    "958": "backend.common.DeductionNotPossible",
    "959": "backend.common.CannotAcceptOrderDueToAmount",
    "960": "backend.common.NotAcceptingWithdrawRequestForToken",
    "961": "backend.common.MoreTradeForWithdraw",
    "962": "backend.common.CanNotBetTwiceForToken",
    "963": "backend.common.CanNotPlaceBetForOwnToken",
    "964": "backend.common.BidAlreadyPlacedForAmount",
    "965": "backend.common.AmountTooLess",
    "966": "backend.common.UnableProceedYourOrderTryAgainLater",
    "967": "backend.common.EOSTransactionDroppedPleaseTryAgain",
    "968": "backend.common.CanNotPlaceOrderThisAmountMustBeAnInteger",
    "970": "backend.common.ReconsiderOrderPrice",
    "969": "backend.common.SellingJKCAvailableSoon" ,
    "971": "backend.common.CantPlaceLessOrder",
    "972": "backend.common.CantPlaceOrder",
    "973": "backend.common.OrderMinimumAmount",
    "974": "backend.common.FailedToCancel",
    "977": "backend.common.CanNotBuyOrder",
    "978": "backend.common.CryptotypeNotAllowByOwner",
    "1001": "backend.common.BalanceNorUpdated",
    "1002": "backend.common.BetNotPlaced",
    "1003": "backend.common.RecordClearFailed",
    "1004": "backend.common.FailedToAddOrder",
    "1005": "backend.common.FailedToAddBatchOrder",
    "1006": "backend.common.RewardNotReversed",
    "1007": "backend.common.RewardNotGiveSuccess",
    "1008": "backend.common.NotInvested",
    "1009": "backend.common.FailedToSetNewTarget",
    "1010": "backend.common.FailedToSetNewTime",
    "1011": "backend.common.FailedCreateTicketRefund",
    "1012": "backend.common.WithdrawRequestSaveUnsuccessful",
    "1013": "backend.common.BalanceTransferredFailedUpdateDatabase",
    "1051": "backend.common.CodeExceptionErrorInCatchBlock",
    "1052": "backend.common.CountNotMatch",
    "1053": "backend.common.SomethingWentWrong",
    "1054": "backend.common.CancelAllBroke",
    "1101": "backend.common.NotFound",
    "1102": "backend.common.NoTokenFound",
    "1103": "backend.common.NoRecordFound",
    "1104": "backend.common.NoEOSAccountExistForUser",
    "1105": "backend.common.OrderAlreadyTraded",
    "1106": "backend.common.CanNotSentOwn",
    "1188": "backend.common.OtpCodeNotMatched",
    "9999": "backend.common.UnableToConnectServer",
}