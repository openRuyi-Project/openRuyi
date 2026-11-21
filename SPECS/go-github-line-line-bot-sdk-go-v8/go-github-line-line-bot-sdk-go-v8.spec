# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           line-bot-sdk-go
%define go_import_path  github.com/line/line-bot-sdk-go/v8

Name:           go-github-line-line-bot-sdk-go-v8
Version:        8.20.1
Release:        %autorelease
Summary:        LINE Messaging API SDK for Go
License:        Apache-2.0
URL:            https://github.com/line/line-bot-sdk-go
#!RemoteAsset:  sha256:a7f171a2e94e205823d2a105b7c59bb58c00b3641cd23887ff18db3b669d0c8b
Source0:        https://github.com/line/line-bot-sdk-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/line/line-bot-sdk-go/v8) = %{version}

%description
The LINE Messaging API SDK for Go makes it easy to develop bots using LINE
Messaging API, and you can create a sample bot within minutes.

%package        tests
Summary:        Regression tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       go

%description    tests
Go regression test sources for go-github-line-line-bot-sdk-go-v8.

%files
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/account_link_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/audience_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/channel_access_token/tests/api/api_channel_access_token_test_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/channel_access_token/tests/handwritten/api_GetsAllValidChannelAccessTokenKeyIds_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/channel_access_token/tests/handwritten/api_IssueStatelessChannelToken_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/channel_access_token/tests/handwritten/api_VerifyChannelTokenByJWT_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/client_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/delivery_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/flex_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/get_bot_info_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/get_content_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/get_count_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/get_follower_ids_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/get_ids_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/get_profile_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/get_quota_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/get_summary_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/httphandler/httphandler_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/insight/tests/api/api_insight_test_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/insight_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/leave_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/liff/tests/api/api_liff_test_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/liff_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/manage_audience/tests/handwritten/api_multipart_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/message_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/messaging_api/tests/handwritten/api_CloseCoupon_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/messaging_api/tests/handwritten/api_CreateCoupon_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/messaging_api/tests/handwritten/api_GetCouponDetail_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/messaging_api/tests/handwritten/api_GetFollowers_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/messaging_api/tests/handwritten/api_GetMembersIds_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/messaging_api/tests/handwritten/api_ListCoupon_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/messaging_api/tests/handwritten/api_WithHttpInfo_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/messaging_api/tests/handwritten/calling_api_twice_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/messaging_api/tests/handwritten/model_coupon_message_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/messaging_api/tests/handwritten/model_datetime_picker_action_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/messaging_api/tests/handwritten/model_limit_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/messaging_api/tests/handwritten/model_reply_message_request_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/messaging_api/tests/handwritten/model_sticker_message_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/messaging_api/tests/handwritten/model_text_message_v2_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/module/tests/api/api_line_module_test_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/module_attach/tests/api/api_line_module_attach_test_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/oauth2_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/oauth_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/progress_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/raw_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/richmenu_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/send_message_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/shop/tests/api/api_shop_test_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/template_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/validate_message_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/webhook/httphandler_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/webhook/tests/handwritten/model_source_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/webhook_test.go
%exclude /usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/util/find_dollar_sign_test.go
%doc README.md
%license LICENSE.txt
%{go_sys_gopath}/%{go_import_path}

%files tests
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/account_link_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/audience_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/channel_access_token/tests/api/api_channel_access_token_test_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/channel_access_token/tests/handwritten/api_GetsAllValidChannelAccessTokenKeyIds_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/channel_access_token/tests/handwritten/api_IssueStatelessChannelToken_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/channel_access_token/tests/handwritten/api_VerifyChannelTokenByJWT_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/client_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/delivery_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/flex_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/get_bot_info_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/get_content_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/get_count_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/get_follower_ids_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/get_ids_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/get_profile_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/get_quota_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/get_summary_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/httphandler/httphandler_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/insight/tests/api/api_insight_test_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/insight_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/leave_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/liff/tests/api/api_liff_test_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/liff_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/manage_audience/tests/handwritten/api_multipart_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/message_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/messaging_api/tests/handwritten/api_CloseCoupon_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/messaging_api/tests/handwritten/api_CreateCoupon_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/messaging_api/tests/handwritten/api_GetCouponDetail_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/messaging_api/tests/handwritten/api_GetFollowers_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/messaging_api/tests/handwritten/api_GetMembersIds_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/messaging_api/tests/handwritten/api_ListCoupon_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/messaging_api/tests/handwritten/api_WithHttpInfo_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/messaging_api/tests/handwritten/calling_api_twice_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/messaging_api/tests/handwritten/model_coupon_message_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/messaging_api/tests/handwritten/model_datetime_picker_action_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/messaging_api/tests/handwritten/model_limit_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/messaging_api/tests/handwritten/model_reply_message_request_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/messaging_api/tests/handwritten/model_sticker_message_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/messaging_api/tests/handwritten/model_text_message_v2_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/module/tests/api/api_line_module_test_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/module_attach/tests/api/api_line_module_attach_test_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/oauth2_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/oauth_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/progress_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/raw_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/richmenu_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/send_message_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/shop/tests/api/api_shop_test_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/template_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/validate_message_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/webhook/httphandler_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/webhook/tests/handwritten/model_source_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/linebot/webhook_test.go
/usr/share/gocode/src/github.com/line/line-bot-sdk-go/v8/util/find_dollar_sign_test.go

%changelog
%autochangelog
