from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView

from .batchProcessing.batchRequest import batchUpload_compress, getBatchStatus, getInitImageInfo, startBatchProcess
from .userManagement.register import sendValidCodeEmail, registerNewUser
from .userManagement.login import loginCheck, checkByToken, logoutCheck
from .userManagement.userCenterFunctions import getUserInfo, updateNewUName, updateNewAddInfo, checkInviteCode, updateNewPwd
from .imageProcess.requestFunctions import updateInputAndGetNBI, uploadImage, chooseLastImage, historyImgInfo,getLastAdjustArg
from .historyManagement.history import historyDisplay, deleteHistoryImage, historyFilter, modifyInfo, batchDisplay
from .batchHistoryManagement.bacthHistory import batchHistoryDisplay,batchHistoryWithFilter

urlpatterns = [
    path(r'NBI/admin/', admin.site.urls),
    path(r'NBI/', TemplateView.as_view(template_name='index.html')),

    # '''Image Process'''
    path(r'NBI/Image/upload/', uploadImage, name='uploadImage'),
    path(r'NBI/Image/getResult/', updateInputAndGetNBI, name='inputUpdate'),
    path(r'NBI/Image/chooseLastImage/', chooseLastImage, name='chooseLastImage'),
    path(r'NBI/Image/getLastAdjustArg/', getLastAdjustArg, name='getLastAdjustArg'),

    # """User"""
    path(r"NBI/User/register/sendEmail", sendValidCodeEmail, name="validCodeEmail"),
    path(r"NBI/User/register/", registerNewUser, name="registerNewUser"),
    path(r"NBI/User/checkLogin/", loginCheck, name="loginWithAccount"),
    path(r"NBI/User/logout/", logoutCheck, name="logout"),
    path(r"NBI/User/checkByToken/", checkByToken, name="checkByToken"),
    path(r"NBI/User/getUserInfo/", getUserInfo, name="getUserInfoByToken"),
    path(r"NBI/User/uploadNewUName/", updateNewUName),
    path(r"NBI/User/uploadNewAddInfo/", updateNewAddInfo),
    path(r"NBI/User/uploadNewPwd/", updateNewPwd),
    path(r"NBI/User/inputInviteCode/", checkInviteCode),

    # """History Data"""
    path(r"NBI/History/display/", historyDisplay, name="historyDisplay"),
    path(r'NBI/HistoryDetail/modifyInfo/', modifyInfo, name="historyModifyInfo"),
    path(r'NBI/HistoryDetail/', historyImgInfo, name="HistoryImgInfo"),
    path(r'NBI/History/deleteImage/', deleteHistoryImage, name="deleteOneImage"),
    path(r'NBI/History/getHistoryWithFilter/', historyFilter),
    path(r'NBI/History/batchDisplay/', batchDisplay, name='batchDisplay'),

    # """Batch Processing"""
    path(r"NBI/Batch/upload/compressPack/", batchUpload_compress, name="upload compress package"),
    path(r"NBI/Batch/checkStatus/", getBatchStatus, name="get batch status by batch id"),
    path(r"NBI/Batch/getOriginImage/", getInitImageInfo, name="get batch info after passing package check"),
    path(r"NBI/Batch/startProcess/", startBatchProcess, name="start batch process"),

    # Batch History Display
    path(r"NBI/BatchHistory/display/", batchHistoryDisplay, name="batchHistoryDisplay"),
    path(r'NBI/BatchHistory/getBatchHistoryWithFilter/', batchHistoryWithFilter),
]
