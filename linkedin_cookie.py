#!/usr/bin/env python
# -*- coding:utf-8 -*-
# time 2018-11-17
# Author fcj
# message 领英cookie数据
import time

t = int(round(time.time())) - 80

normal_list = [
    'bcookie="v=2&2945bbdb-b6ac-4909-8213-00f420089b8e"; bscookie="v=1&201811291035236afc4284-8400-414e-8696-22d22c9037'
    '8dAQHt61OLAtWJ_M_JFdAXeixpONTVudB-"; sl="v=1&P5Lsp"; visit="v=1&G"; li_at=AQEDASmrPB4DyCGLAAABZ18KCb0AAAFngxaNvVEA'
    'eCfl72J1O5VSbmUgHzD-V5VkWW8_ivnKmvfAczkVCQRWm7FQYP97h5lqC9qU1oB8l726Sz-TzIopMf_2l9SlJla0M8cCuhWGLe7dUFcZvvYF6cK-; '
    'JSESSIONID="ajax:34174191"; wwepo=true; liap=true; li_cc=AQGlTtXlrOEh-wAAAWdfCgs7iIuM-658MJVIJIh0MhkNEj'
    'Smfr_KJUK_u8b_y6u4DmspGRElM_Pm; _lipt=CwEAAAFnXwoR_JoCTPLlrPgXmftMIhSuaK5i5NBj6z5kfmCTpc8AV_t-Z5cq9v431M13qfSKJnOv'
    'ZktmuF8xmop1sMaze_uERHhBcG8IFXco72cLofcgVosMoiZnsOCGKsBHfq06yyckDJkcdWOcRVAZ-RAzGpw7x2X5Smq2CabWvlRNE_8F8M4lvHxfPw'
    'EUqLai_RHxHXs9xiug80XwM3vdS74gxfOG0r9DNIWWmpi3cMd2sA; _guid=257d7406-676a-4ef6-88f1-db5636e54c9f; li_oatml=AQH3BgX'
    '7OedALwAAAWdfKkOlHRuupFv1NEge0BldIYEx6Yc5DB53_QGR53q4soOlYcHGCgkapO2ljYOpozPRnYBTElecMClu; UserMatchHistory=AQKs5d'
    'f6Bzf21QAAAWdfKkcME7Yo_4S-rOYPDkbxwZGFb7pylYNXQWuicSxMoTlC9LTHOvXOCwaPgYGk-UgV28rnDlddkLplA6li5y_zssHevLXimikuRV1g'
    'HFQL-pqFQpp1HA; lang=v=2&lang=zh-cn; spectroscopyId=f76d9843-1746-4725-99e3-560dd7db8a40; lidc="b=SB02:g=83:u=4:i='
    ''+str(t)+':t=1543567053:s=AQFIm1jbNDHcEhaqnEVl_wdc4D7a2RTG"',

    'bcookie="v=2&2945bbdb-b6ac-4909-8213-00f420089b8e"; bscookie="v=1&201811291035236afc4284-8400-414e-8696-22d22c9037'
    '8dAQHt61OLAtWJ_M_JFdAXeixpONTVudB-"; sl="v=1&P5Lsp"; visit="v=1&G"; li_at=AQEDASmrPB4DyCGLAAABZ18KCb0AAAFngxaNvVEA'
    'eCfl72J1O5VSbmUgHzD-V5VkWW8_ivnKmvfAczkVCQRWm7FQYP97h5lqC9qU1oB8l726Sz-TzIopMf_2l9SlJla0M8cCuhWGLe7dUFcZvvYF6cK-; '
    'JSESSIONID="ajax:3417"; wwepo=true; liap=true; li_cc=AQGlTtXlrOEh-wAAAWdfCgs7iIuM-658MJVIJIh0MhkNEj'
    'Smfr_KJUK_u8b_y6u4DmspGRElM_Pm; _lipt=CwEAAAFnXwoR_JoCTPLlrPgXmftMIhSuaK5i5NBj6z5kfmCTpc8AV_t-Z5cq9v431M13qfSKJnOv'
    'ZktmuF8xmop1sMaze_uERHhBcG8IFXco72cLofcgVosMoiZnsOCGKsBHfq06yyckDJkcdWOcRVAZ-RAzGpw7x2X5Smq2CabWvlRNE_8F8M4lvHxfPw'
    'EUqLai_RHxHXs9xiug80XwM3vdS74gxfOG0r9DNIWWmpi3cMd2sA; _guid=257d7406-676a-4ef6-88f1-db5636e54c9f; li_oatml=AQH3BgX'
    '7OedALwAAAWdfKkOlHRuupFv1NEge0BldIYEx6Yc5DB53_QGR53q4soOlYcHGCgkapO2ljYOpozPRnYBTElecMClu; UserMatchHistory=AQKs5d'
    'f6Bzf21QAAAWdfKkcME7Yo_4S-rOYPDkbxwZGFb7pylYNXQWuicSxMoTlC9LTHOvXOCwaPgYGk-UgV28rnDlddkLplA6li5y_zssHevLXimikuRV1g'
    'HFQL-pqFQpp1HA; lang=v=2&lang=zh-cn; spectroscopyId=0f090d0b-80e9-4c68-8161-e7e6092dfd90; lil-lang=zh_CN; lidc="b='
    'SB02:g=83:u=4:i='+str(t)+':t=1543567053:s=AQH2zDhkcEPlLNbxLX90kl1Rz5yxighM"',

    'bcookie="v=2&2945bbdb-b6ac-4909-8213-00f420089b8e"; bscookie="v=1&201811291035236afc4284-8400-414e-8696-22d22c9037'
    '8dAQHt61OLAtWJ_M_JFdAXeixpONTVudB-"; sl="v=1&P5Lsp"; visit="v=1&G"; li_at=AQEDASmrPB4DyCGLAAABZ18KCb0AAAFngxaNvVEA'
    'eCfl72J1O5VSbmUgHzD-V5VkWW8_ivnKmvfAczkVCQRWm7FQYP97h5lqC9qU1oB8l726Sz-TzIopMf_2l9SlJla0M8cCuhWGLe7dUFcZvvYF6cK-; '
    'JSESSIONID="ajax:341741"; wwepo=true; liap=true; li_cc=AQGlTtXlrOEh-wAAAWdfCgs7iIuM-658MJVIJIh0MhkNEj'
    'Smfr_KJUK_u8b_y6u4DmspGRElM_Pm; _lipt=CwEAAAFnXwoR_JoCTPLlrPgXmftMIhSuaK5i5NBj6z5kfmCTpc8AV_t-Z5cq9v431M13qfSKJnOv'
    'ZktmuF8xmop1sMaze_uERHhBcG8IFXco72cLofcgVosMoiZnsOCGKsBHfq06yyckDJkcdWOcRVAZ-RAzGpw7x2X5Smq2CabWvlRNE_8F8M4lvHxfPw'
    'EUqLai_RHxHXs9xiug80XwM3vdS74gxfOG0r9DNIWWmpi3cMd2sA; _guid=257d7406-676a-4ef6-88f1-db5636e54c9f; li_oatml=AQH3BgX'
    '7OedALwAAAWdfKkOlHRuupFv1NEge0BldIYEx6Yc5DB53_QGR53q4soOlYcHGCgkapO2ljYOpozPRnYBTElecMClu; UserMatchHistory=AQKs5d'
    'f6Bzf21QAAAWdfKkcME7Yo_4S-rOYPDkbxwZGFb7pylYNXQWuicSxMoTlC9LTHOvXOCwaPgYGk-UgV28rnDlddkLplA6li5y_zssHevLXimikuRV1g'
    'HFQL-pqFQpp1HA; lang=v=2&lang=zh-cn; spectroscopyId=b6a827d3-f3e7-48aa-b503-52b232f0c7ea; lidc="b=SB02:g=83:u=4:i='
    ''+str(t)+':t=1543567053:s=AQHN9jDongDdjBM1jYSy4DP9vjYW-hdf"',

    'bcookie="v=2&2945bbdb-b6ac-4909-8213-00f420089b8e"; bscookie="v=1&201811291035236afc4284-8400-414e-8696-22d22c9037'
    '8dAQHt61OLAtWJ_M_JFdAXeixpONTVudB-"; sl="v=1&P5Lsp"; visit="v=1&G"; li_at=AQEDASmrPB4DyCGLAAABZ18KCb0AAAFngxaNvVEA'
    'eCfl72J1O5VSbmUgHzD-V5VkWW8_ivnKmvfAczkVCQRWm7FQYP97h5lqC9qU1oB8l726Sz-TzIopMf_2l9SlJla0M8cCuhWGLe7dUFcZvvYF6cK-; '
    'JSESSIONID="ajax:3417872"; wwepo=true; liap=true; li_cc=AQGlTtXlrOEh-wAAAWdfCgs7iIuM-658MJVIJIh0MhkNEj'
    'Smfr_KJUK_u8b_y6u4DmspGRElM_Pm; _lipt=CwEAAAFnXwoR_JoCTPLlrPgXmftMIhSuaK5i5NBj6z5kfmCTpc8AV_t-Z5cq9v431M13qfSKJnOv'
    'ZktmuF8xmop1sMaze_uERHhBcG8IFXco72cLofcgVosMoiZnsOCGKsBHfq06yyckDJkcdWOcRVAZ-RAzGpw7x2X5Smq2CabWvlRNE_8F8M4lvHxfPw'
    'EUqLai_RHxHXs9xiug80XwM3vdS74gxfOG0r9DNIWWmpi3cMd2sA; _guid=257d7406-676a-4ef6-88f1-db5636e54c9f; li_oatml=AQH3BgX'
    '7OedALwAAAWdfKkOlHRuupFv1NEge0BldIYEx6Yc5DB53_QGR53q4soOlYcHGCgkapO2ljYOpozPRnYBTElecMClu; UserMatchHistory=AQKs5d'
    'f6Bzf21QAAAWdfKkcME7Yo_4S-rOYPDkbxwZGFb7pylYNXQWuicSxMoTlC9LTHOvXOCwaPgYGk-UgV28rnDlddkLplA6li5y_zssHevLXimikuRV1g'
    'HFQL-pqFQpp1HA; lang=v=2&lang=zh-cn; spectroscopyId=3fb86003-a2c6-46bc-8515-e8e91daa5513; lil-lang=zh_CN; lidc="b='
    'SB02:g=83:u=4:i='+str(t)+':t=1543567053:s=AQFVJq3IgYIgtJRjYAwRdoXAbuaDdWXI"'

]


pro_cookie = [
    'bcookie="v=2&2945bbdb-b6ac-4909-8213-00f420089b8e"; bscookie="v=1&201811291035236afc4284-8400-414e-8696-22d22c9037'
    '8dAQHt61OLAtWJ_M_JFdAXeixpONTVudB-"; sl="v=1&P5Lsp"; visit="v=1&G"; li_at=AQEDASmrPB4DyCGLAAABZ18KCb0AAAFngxaNvVEA'
    'eCfl72J1O5VSbmUgHzD-V5VkWW8_ivnKmvfAczkVCQRWm7FQYP97h5lqC9qU1oB8l726Sz-TzIopMf_2l9SlJla0M8cCuhWGLe7dUFcZvvYF6cK-; '
    'JSESSIONID="ajax:341872"; wwepo=true; liap=true; li_cc=AQGlTtXlrOEh-wAAAWdfCgs7iIuM-658MJVIJIh0MhkNEj'
    'Smfr_KJUK_u8b_y6u4DmspGRElM_Pm; _lipt=CwEAAAFnXwoR_JoCTPLlrPgXmftMIhSuaK5i5NBj6z5kfmCTpc8AV_t-Z5cq9v431M13qfSKJnOv'
    'ZktmuF8xmop1sMaze_uERHhBcG8IFXco72cLofcgVosMoiZnsOCGKsBHfq06yyckDJkcdWOcRVAZ-RAzGpw7x2X5Smq2CabWvlRNE_8F8M4lvHxfPw'
    'EUqLai_RHxHXs9xiug80XwM3vdS74gxfOG0r9DNIWWmpi3cMd2sA; _guid=257d7406-676a-4ef6-88f1-db5636e54c9f; li_oatml=AQH3BgX'
    '7OedALwAAAWdfKkOlHRuupFv1NEge0BldIYEx6Yc5DB53_QGR53q4soOlYcHGCgkapO2ljYOpozPRnYBTElecMClu; UserMatchHistory=AQKs5d'
    'f6Bzf21QAAAWdfKkcME7Yo_4S-rOYPDkbxwZGFb7pylYNXQWuicSxMoTlC9LTHOvXOCwaPgYGk-UgV28rnDlddkLplA6li5y_zssHevLXimikuRV1g'
    'HFQL-pqFQpp1HA; lang=v=2&lang=zh-cn; spectroscopyId=197e5aea-9115-467b-bf9e-e4c40f86c461; lil-lang=zh_CN; lidc="b='
    'SB02:g=83:u=4:i='+str(t)+':t=1543567053:s=AQFAeVeTiFEI2YkEcCTnYSl9Ujfx1HYw"',

    'bcookie="v=2&2945bbdb-b6ac-4909-8213-00f420089b8e"; bscookie="v=1&201811291035236afc4284-8400-414e-8696-22d22c9037'
    '8dAQHt61OLAtWJ_M_JFdAXeixpONTVudB-"; sl="v=1&P5Lsp"; visit="v=1&G"; li_at=AQEDASmrPB4DyCGLAAABZ18KCb0AAAFngxaNvVEA'
    'eCfl72J1O5VSbmUgHzD-V5VkWW8_ivnKmvfAczkVCQRWm7FQYP97h5lqC9qU1oB8l726Sz-TzIopMf_2l9SlJla0M8cCuhWGLe7dUFcZvvYF6cK-; '
    'JSESSIONID="ajax:341743872"; wwepo=true; liap=true; li_cc=AQGlTtXlrOEh-wAAAWdfCgs7iIuM-658MJVIJIh0MhkNEj'
    'Smfr_KJUK_u8b_y6u4DmspGRElM_Pm; _lipt=CwEAAAFnXwoR_JoCTPLlrPgXmftMIhSuaK5i5NBj6z5kfmCTpc8AV_t-Z5cq9v431M13qfSKJnOv'
    'ZktmuF8xmop1sMaze_uERHhBcG8IFXco72cLofcgVosMoiZnsOCGKsBHfq06yyckDJkcdWOcRVAZ-RAzGpw7x2X5Smq2CabWvlRNE_8F8M4lvHxfPw'
    'EUqLai_RHxHXs9xiug80XwM3vdS74gxfOG0r9DNIWWmpi3cMd2sA; _guid=257d7406-676a-4ef6-88f1-db5636e54c9f; li_oatml=AQH3BgX'
    '7OedALwAAAWdfKkOlHRuupFv1NEge0BldIYEx6Yc5DB53_QGR53q4soOlYcHGCgkapO2ljYOpozPRnYBTElecMClu; UserMatchHistory=AQKs5d'
    'f6Bzf21QAAAWdfKkcME7Yo_4S-rOYPDkbxwZGFb7pylYNXQWuicSxMoTlC9LTHOvXOCwaPgYGk-UgV28rnDlddkLplA6li5y_zssHevLXimikuRV1g'
    'HFQL-pqFQpp1HA; lang=v=2&lang=zh-cn; spectroscopyId=e8c6b6bd-9b49-465a-847a-79c68a76668d; lidc="b=SB02:g=83:u=4:i='
    ''+str(t)+':t=1543567053:s=AQHJXC8uiF0XIQSeeK6gYBmQqkN0zbte"',

    'bcookie="v=2&2945bbdb-b6ac-4909-8213-00f420089b8e"; bscookie="v=1&201811291035236afc4284-8400-414e-8696-22d22c9037'
    '8dAQHt61OLAtWJ_M_JFdAXeixpONTVudB-"; sl="v=1&P5Lsp"; visit="v=1&G"; li_at=AQEDASmrPB4DyCGLAAABZ18KCb0AAAFngxaNvVEA'
    'eCfl72J1O5VSbmUgHzD-V5VkWW8_ivnKmvfAczkVCQRWm7FQYP97h5lqC9qU1oB8l726Sz-TzIopMf_2l9SlJla0M8cCuhWGLe7dUFcZvvYF6cK-; '
    'JSESSIONID="ajax:341746543872"; wwepo=true; liap=true; li_cc=AQGlTtXlrOEh-wAAAWdfCgs7iIuM-658MJVIJIh0MhkNEj'
    'Smfr_KJUK_u8b_y6u4DmspGRElM_Pm; _lipt=CwEAAAFnXwoR_JoCTPLlrPgXmftMIhSuaK5i5NBj6z5kfmCTpc8AV_t-Z5cq9v431M13qfSKJnOv'
    'ZktmuF8xmop1sMaze_uERHhBcG8IFXco72cLofcgVosMoiZnsOCGKsBHfq06yyckDJkcdWOcRVAZ-RAzGpw7x2X5Smq2CabWvlRNE_8F8M4lvHxfPw'
    'EUqLai_RHxHXs9xiug80XwM3vdS74gxfOG0r9DNIWWmpi3cMd2sA; _guid=257d7406-676a-4ef6-88f1-db5636e54c9f; li_oatml=AQH3BgX'
    '7OedALwAAAWdfKkOlHRuupFv1NEge0BldIYEx6Yc5DB53_QGR53q4soOlYcHGCgkapO2ljYOpozPRnYBTElecMClu; UserMatchHistory=AQKs5d'
    'f6Bzf21QAAAWdfKkcME7Yo_4S-rOYPDkbxwZGFb7pylYNXQWuicSxMoTlC9LTHOvXOCwaPgYGk-UgV28rnDlddkLplA6li5y_zssHevLXimikuRV1g'
    'HFQL-pqFQpp1HA; lang=v=2&lang=zh-cn; spectroscopyId=ca7bea95-0a9c-4594-b020-95b46d8982f8; lidc="b=SB02:g=83:u=4:i='
    ''+str(t)+':t=1543567053:s=AQGydxq6SIQA0Qh97KB9RDwdXSE73CFJ"',

    'bcookie="v=2&2945bbdb-b6ac-4909-8213-00f420089b8e"; bscookie="v=1&201811291035236afc4284-8400-414e-8696-22d22c9037'
    '8dAQHt61OLAtWJ_M_JFdAXeixpONTVudB-"; sl="v=1&P5Lsp"; visit="v=1&G"; li_at=AQEDASmrPB4DyCGLAAABZ18KCb0AAAFngxaNvVEA'
    'eCfl72J1O5VSbmUgHzD-V5VkWW8_ivnKmvfAczkVCQRWm7FQYP97h5lqC9qU1oB8l726Sz-TzIopMf_2l9SlJla0M8cCuhWGLe7dUFcZvvYF6cK-; '
    'JSESSIONID="ajax:341741543872"; wwepo=true; liap=true; li_cc=AQGlTtXlrOEh-wAAAWdfCgs7iIuM-658MJVIJIh0MhkNEj'
    'Smfr_KJUK_u8b_y6u4DmspGRElM_Pm; _lipt=CwEAAAFnXwoR_JoCTPLlrPgXmftMIhSuaK5i5NBj6z5kfmCTpc8AV_t-Z5cq9v431M13qfSKJnOv'
    'ZktmuF8xmop1sMaze_uERHhBcG8IFXco72cLofcgVosMoiZnsOCGKsBHfq06yyckDJkcdWOcRVAZ-RAzGpw7x2X5Smq2CabWvlRNE_8F8M4lvHxfPw'
    'EUqLai_RHxHXs9xiug80XwM3vdS74gxfOG0r9DNIWWmpi3cMd2sA; _guid=257d7406-676a-4ef6-88f1-db5636e54c9f; li_oatml=AQH3BgX'
    '7OedALwAAAWdfKkOlHRuupFv1NEge0BldIYEx6Yc5DB53_QGR53q4soOlYcHGCgkapO2ljYOpozPRnYBTElecMClu; UserMatchHistory=AQKs5d'
    'f6Bzf21QAAAWdfKkcME7Yo_4S-rOYPDkbxwZGFb7pylYNXQWuicSxMoTlC9LTHOvXOCwaPgYGk-UgV28rnDlddkLplA6li5y_zssHevLXimikuRV1g'
    'HFQL-pqFQpp1HA; lang=v=2&lang=zh-cn; spectroscopyId=898a577e-686b-42ea-b00d-24f7811beb1c; lidc="b=SB02:g=83:u=4:i='
    ''+str(t)+':t=1543567053:s=AQHbZGz2FcTZuSqrk3OISiltmGfiRvnM"'
]

dis_cookie = [

    'bcookie="v=2&2945bbdb-b6ac-4909-8213-00f420089b8e"; bscookie="v=1&201811291035236afc4284-8400-414e-8696-22d22c9037'
    '8dAQHt61OLAtWJ_M_JFdAXeixpONTVudB-"; sl="v=1&P5Lsp"; visit="v=1&G"; li_at=AQEDASmrPB4DyCGLAAABZ18KCb0AAAFngxaNvVEA'
    'eCfl72J1O5VSbmUgHzD-V5VkWW8_ivnKmvfAczkVCQRWm7FQYP97h5lqC9qU1oB8l726Sz-TzIopMf_2l9SlJla0M8cCuhWGLe7dUFcZvvYF6cK-; '
    'JSESSIONID="ajax:3417543872"; wwepo=true; liap=true; li_cc=AQGlTtXlrOEh-wAAAWdfCgs7iIuM-658MJVIJIh0MhkNEj'
    'Smfr_KJUK_u8b_y6u4DmspGRElM_Pm; _lipt=CwEAAAFnXwoR_JoCTPLlrPgXmftMIhSuaK5i5NBj6z5kfmCTpc8AV_t-Z5cq9v431M13qfSKJnOv'
    'ZktmuF8xmop1sMaze_uERHhBcG8IFXco72cLofcgVosMoiZnsOCGKsBHfq06yyckDJkcdWOcRVAZ-RAzGpw7x2X5Smq2CabWvlRNE_8F8M4lvHxfPw'
    'EUqLai_RHxHXs9xiug80XwM3vdS74gxfOG0r9DNIWWmpi3cMd2sA; _guid=257d7406-676a-4ef6-88f1-db5636e54c9f; li_oatml=AQH3BgX'
    '7OedALwAAAWdfKkOlHRuupFv1NEge0BldIYEx6Yc5DB53_QGR53q4soOlYcHGCgkapO2ljYOpozPRnYBTElecMClu; UserMatchHistory=AQKs5d'
    'f6Bzf21QAAAWdfKkcME7Yo_4S-rOYPDkbxwZGFb7pylYNXQWuicSxMoTlC9LTHOvXOCwaPgYGk-UgV28rnDlddkLplA6li5y_zssHevLXimikuRV1g'
    'HFQL-pqFQpp1HA; lang=v=2&lang=zh-cn; spectroscopyId=87b33d2d-e9e0-4189-80e1-b208fdd94df5; lil-lang=zh_CN; lidc="b='
    'SB02:g=83:u=4:i='+str(t)+':t=1543567053:s=AQGiRIoQz3HMguRZLjuGpdJVwKHTAc97"',

    'bcookie="v=2&2945bbdb-b6ac-4909-8213-00f420089b8e"; bscookie="v=1&201811291035236afc4284-8400-414e-8696-22d22c9037'
    '8dAQHt61OLAtWJ_M_JFdAXeixpONTVudB-"; sl="v=1&P5Lsp"; visit="v=1&G"; li_at=AQEDASmrPB4DyCGLAAABZ18KCb0AAAFngxaNvVEA'
    'eCfl72J1O5VSbmUgHzD-V5VkWW8_ivnKmvfAczkVCQRWm7FQYP97h5lqC9qU1oB8l726Sz-TzIopMf_2l9SlJla0M8cCuhWGLe7dUFcZvvYF6cK-; '
    'JSESSIONID="ajax:3413872"; wwepo=true; liap=true; li_cc=AQGlTtXlrOEh-wAAAWdfCgs7iIuM-658MJVIJIh0MhkNEj'
    'Smfr_KJUK_u8b_y6u4DmspGRElM_Pm; _lipt=CwEAAAFnXwoR_JoCTPLlrPgXmftMIhSuaK5i5NBj6z5kfmCTpc8AV_t-Z5cq9v431M13qfSKJnOv'
    'ZktmuF8xmop1sMaze_uERHhBcG8IFXco72cLofcgVosMoiZnsOCGKsBHfq06yyckDJkcdWOcRVAZ-RAzGpw7x2X5Smq2CabWvlRNE_8F8M4lvHxfPw'
    'EUqLai_RHxHXs9xiug80XwM3vdS74gxfOG0r9DNIWWmpi3cMd2sA; _guid=257d7406-676a-4ef6-88f1-db5636e54c9f; li_oatml=AQH3BgX'
    '7OedALwAAAWdfKkOlHRuupFv1NEge0BldIYEx6Yc5DB53_QGR53q4soOlYcHGCgkapO2ljYOpozPRnYBTElecMClu; UserMatchHistory=AQKs5d'
    'f6Bzf21QAAAWdfKkcME7Yo_4S-rOYPDkbxwZGFb7pylYNXQWuicSxMoTlC9LTHOvXOCwaPgYGk-UgV28rnDlddkLplA6li5y_zssHevLXimikuRV1g'
    'HFQL-pqFQpp1HA; lang=v=2&lang=zh-cn; lidc="b=SB02:g=83:u=4:i='+str(t)+':t=1543567053:s=AQGp6jBonbaZV3vIUUKwLy-vecZ'
    'uIuYT"; lil-lang=zh_CN',

    'bcookie="v=2&2945bbdb-b6ac-4909-8213-00f420089b8e"; bscookie="v=1&201811291035236afc4284-8400-414e-8696-22d22c9037'
    '8dAQHt61OLAtWJ_M_JFdAXeixpONTVudB-"; sl="v=1&P5Lsp"; visit="v=1&G"; li_at=AQEDASmrPB4DyCGLAAABZ18KCb0AAAFngxaNvVEA'
    'eCfl72J1O5VSbmUgHzD-V5VkWW8_ivnKmvfAczkVCQRWm7FQYP97h5lqC9qU1oB8l726Sz-TzIopMf_2l9SlJla0M8cCuhWGLe7dUFcZvvYF6cK-; '
    'JSESSIONID="ajax:3417419872"; wwepo=true; liap=true; li_cc=AQGlTtXlrOEh-wAAAWdfCgs7iIuM-658MJVIJIh0MhkNEj'
    'Smfr_KJUK_u8b_y6u4DmspGRElM_Pm; _lipt=CwEAAAFnXwoR_JoCTPLlrPgXmftMIhSuaK5i5NBj6z5kfmCTpc8AV_t-Z5cq9v431M13qfSKJnOv'
    'ZktmuF8xmop1sMaze_uERHhBcG8IFXco72cLofcgVosMoiZnsOCGKsBHfq06yyckDJkcdWOcRVAZ-RAzGpw7x2X5Smq2CabWvlRNE_8F8M4lvHxfPw'
    'EUqLai_RHxHXs9xiug80XwM3vdS74gxfOG0r9DNIWWmpi3cMd2sA; _guid=257d7406-676a-4ef6-88f1-db5636e54c9f; li_oatml=AQH3BgX'
    '7OedALwAAAWdfKkOlHRuupFv1NEge0BldIYEx6Yc5DB53_QGR53q4soOlYcHGCgkapO2ljYOpozPRnYBTElecMClu; UserMatchHistory=AQKs5d'
    'f6Bzf21QAAAWdfKkcME7Yo_4S-rOYPDkbxwZGFb7pylYNXQWuicSxMoTlC9LTHOvXOCwaPgYGk-UgV28rnDlddkLplA6li5y_zssHevLXimikuRV1g'
    'HFQL-pqFQpp1HA; lang=v=2&lang=zh-cn; lidc="b=SB02:g=83:u=4:i='+str(t)+':t=1543567053:s=AQFfujHrVw9yddWCEAKK6M9QGio'
    'dHb3T"'

    'bcookie="v=2&2945bbdb-b6ac-4909-8213-00f420089b8e"; bscookie="v=1&201811291035236afc4284-8400-414e-8696-22d22c9037'
    '8dAQHt61OLAtWJ_M_JFdAXeixpONTVudB-"; sl="v=1&P5Lsp"; visit="v=1&G"; li_at=AQEDASmrPB4DyCGLAAABZ18KCb0AAAFngxaNvVEA'
    'eCfl72J1O5VSbmUgHzD-V5VkWW8_ivnKmvfAczkVCQRWm7FQYP97h5lqC9qU1oB8l726Sz-TzIopMf_2l9SlJla0M8cCuhWGLe7dUFcZvvYF6cK-; '
    'JSESSIONID="ajax:341741"; wwepo=true; liap=true; li_cc=AQGlTtXlrOEh-wAAAWdfCgs7iIuM-658MJVIJIh0MhkNEj'
    'Smfr_KJUK_u8b_y6u4DmspGRElM_Pm; _lipt=CwEAAAFnXwoR_JoCTPLlrPgXmftMIhSuaK5i5NBj6z5kfmCTpc8AV_t-Z5cq9v431M13qfSKJnOv'
    'ZktmuF8xmop1sMaze_uERHhBcG8IFXco72cLofcgVosMoiZnsOCGKsBHfq06yyckDJkcdWOcRVAZ-RAzGpw7x2X5Smq2CabWvlRNE_8F8M4lvHxfPw'
    'EUqLai_RHxHXs9xiug80XwM3vdS74gxfOG0r9DNIWWmpi3cMd2sA; _guid=257d7406-676a-4ef6-88f1-db5636e54c9f; li_oatml=AQH3BgX'
    '7OedALwAAAWdfKkOlHRuupFv1NEge0BldIYEx6Yc5DB53_QGR53q4soOlYcHGCgkapO2ljYOpozPRnYBTElecMClu; UserMatchHistory=AQKs5d'
    'f6Bzf21QAAAWdfKkcME7Yo_4S-rOYPDkbxwZGFb7pylYNXQWuicSxMoTlC9LTHOvXOCwaPgYGk-UgV28rnDlddkLplA6li5y_zssHevLXimikuRV1g'
    'HFQL-pqFQpp1HA; lang=v=2&lang=zh-cn; lidc="b=SB02:g=83:u=4:i='+str(t)+':t=1543567053:s=AQFX_rvZVk4mPEBZBodaWCn2cHN'
    'gzqLB"'
]

user_agent_list = [
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.35'
        '38.77 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.'
        '0.3497.100 Safari/537.'
        '36 Avast/69.1.867.101',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        '69.0.3497.81 Safari/537.36'
]

referer_list = [
        'https://www.linkedin.com/onboarding/start/get-the-app/new/'
]

normal_headers = {
        'method': 'GET',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': '',
        'Referrer': '',
        'cookie': ''
}

pro_headers = {
    'authority': 'www.linkedin.com',
    'method': 'GET',
    'path': '',
    'scheme': 'https',
    'accept': 'application/vnd.linkedin.normalized+json+2.1',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': '',
    'csrf-token': '',
    'dnt': '1',
    'referer': '',
    'user-agent': '',
    'x-li-lang': 'zh_CN',
    'x-li-page-instance': 'urn:li:page:d_flagship3_profile_view_base_contact_details;To+xm9iiQ+iouYU53YXXwg==',
    'x-li-track': '{"clientVersion":"1.2.4317.0","osName":"web","timezoneOffset":8,"deviceFormFactor":"DESKTOP","mpName":"voyager-web"}',
    'x-requested-with': 'XMLHttpRequest',
    'x-restli-protocol-version': '2.0.0'
}


image_headers = {
        'authority': 'www.linkedin.com',
        'method': 'GET',
        'path': '',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'cookie': '',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/70.0.3538.77 Safari/537.36'
}

distance_headers = {
        'authority': 'www.linkedin.com',
        'method': 'GET',
        'path': '',
        'scheme': 'https',
        'accept': 'application/vnd.linkedin.normalized+json+2.1',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': '',
        'csrf-token': '',
        'dnt': '1',
        # 'referer': '',
        'user-agent': '',
        # 'x-li-lang': 'zh_CN',
        # 'x-li-page-instance': 'urn:li:page:d_flagship3_search_srp_people;PMVKmVPNSoCjEqg8xgAHvg==',
        # 'x-li-track': '{"clientVersion":"1.2.4317.0","osName":"web","timezoneOffset":8,"deviceFormFactor":"DESKTOP",'
        #               '"mpName":"voyager-web"}',
        # 'x-requested-with': 'XMLHttpRequest',
        # 'x-restli-protocol-version': '2.0.0'
}
