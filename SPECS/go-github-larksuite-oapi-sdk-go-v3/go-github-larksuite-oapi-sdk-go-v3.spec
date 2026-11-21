# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           oapi-sdk-go
%define go_import_path  github.com/larksuite/oapi-sdk-go/v3
%define go_test_exclude %{shrink:
    %{go_import_path}/core
    %{go_import_path}/channel/safety
}
%define go_test_exclude_glob %{go_import_path}/sample/*

Name:           go-github-larksuite-oapi-sdk-go-v3
Version:        3.9.4
Release:        %autorelease
Summary:        Feishu OpenPlatform Server SDK
License:        MIT
URL:            https://github.com/larksuite/oapi-sdk-go
#!RemoteAsset:  sha256:2496af6150583facd6161bb87d4bdab62f159225cbf8ded9a97f2598c91f8aa3
Source0:        https://github.com/larksuite/oapi-sdk-go/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gogo/protobuf)
BuildRequires:  go(github.com/gorilla/websocket)

Provides:       go(github.com/larksuite/oapi-sdk-go/v3) = %{version}

Requires:       go(github.com/gogo/protobuf)
Requires:       go(github.com/gorilla/websocket)

%description
Feishu Open Platform offers a series of server-side atomic APIs to achieve
diverse functionalities. However, actual coding requires additional work, such
as obtaining and maintaining access tokens, encrypting and decrypting data,
and verifying request signatures. Furthermore, the lack of semantic
descriptions for function calls and type system support can increase coding
burdens.

To address these issues, Feishu Open Platform has developed the Open Interface
SDK, which incorporates all lengthy logic processes, provides a comprehensive
type system, and offers a semantic programming interface to enhance the coding
experience.

%package        tests
Summary:        Regression tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       go

%description    tests
Go regression test sources for go-github-larksuite-oapi-sdk-go-v3.

%files
%exclude /usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/cache/cache_test.go
%exclude /usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/card/card_test.go
%exclude /usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/bot_identity_test.go
%exclude /usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/card_action_test.go
%exclude /usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/channel_test.go
%exclude /usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/comment_dedup_test.go
%exclude /usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/message_dedup_test.go
%exclude /usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/normalize/converters_test.go
%exclude /usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/normalize/duration_mp4_test.go
%exclude /usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/normalize/duration_ogg_test.go
%exclude /usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/normalize/markdown_test.go
%exclude /usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/normalize/mentions_test.go
%exclude /usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/normalize/parser_test.go
%exclude /usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/outbound/retry_test.go
%exclude /usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/outbound/routing_test.go
%exclude /usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/outbound/splitter_test.go
%exclude /usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/outbound/uploader_test.go
%exclude /usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/pipeline/chat_pipeline_test.go
%exclude /usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/policy_reject_test.go
%exclude /usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/reaction_concurrency_test.go
%exclude /usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/safety/dedup_test.go
%exclude /usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/safety/policy_gate_test.go
%exclude /usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/safety/processing_lock_test.go
%exclude /usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/safety/ssrf_guard_test.go
%exclude /usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/safety/stale_detector_test.go
%exclude /usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/send_retry_test.go
%exclude /usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/send_test.go
%exclude /usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/stream_retry_test.go
%exclude /usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/stream_test.go
%exclude /usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/types/errors_test.go
%exclude /usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/core/accesstoken/access_token_test.go
%exclude /usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/core/appticketmanager_test.go
%exclude /usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/core/cache_test.go
%exclude /usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/core/httpclient_test.go
%exclude /usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/core/httpserverext/httpserverext_test.go
%exclude /usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/core/httptransport_test.go
%exclude /usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/core/reqtranslator_test.go
%exclude /usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/core/tokenmanager_test.go
%exclude /usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/core/utils_test.go
%exclude /usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/event/dispatcher/dispatcher_test.go
%exclude /usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/scene/registration/registration_e2e_test.go
%exclude /usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/scene/registration/registration_test.go
%exclude /usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/ws/client_test.go
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%files tests
/usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/cache/cache_test.go
/usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/card/card_test.go
/usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/bot_identity_test.go
/usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/card_action_test.go
/usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/channel_test.go
/usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/comment_dedup_test.go
/usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/message_dedup_test.go
/usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/normalize/converters_test.go
/usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/normalize/duration_mp4_test.go
/usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/normalize/duration_ogg_test.go
/usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/normalize/markdown_test.go
/usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/normalize/mentions_test.go
/usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/normalize/parser_test.go
/usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/outbound/retry_test.go
/usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/outbound/routing_test.go
/usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/outbound/splitter_test.go
/usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/outbound/uploader_test.go
/usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/pipeline/chat_pipeline_test.go
/usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/policy_reject_test.go
/usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/reaction_concurrency_test.go
/usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/safety/dedup_test.go
/usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/safety/policy_gate_test.go
/usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/safety/processing_lock_test.go
/usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/safety/ssrf_guard_test.go
/usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/safety/stale_detector_test.go
/usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/send_retry_test.go
/usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/send_test.go
/usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/stream_retry_test.go
/usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/stream_test.go
/usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/channel/types/errors_test.go
/usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/core/accesstoken/access_token_test.go
/usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/core/appticketmanager_test.go
/usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/core/cache_test.go
/usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/core/httpclient_test.go
/usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/core/httpserverext/httpserverext_test.go
/usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/core/httptransport_test.go
/usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/core/reqtranslator_test.go
/usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/core/tokenmanager_test.go
/usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/core/utils_test.go
/usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/event/dispatcher/dispatcher_test.go
/usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/scene/registration/registration_e2e_test.go
/usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/scene/registration/registration_test.go
/usr/share/gocode/src/github.com/larksuite/oapi-sdk-go/v3/ws/client_test.go

%changelog
%autochangelog
