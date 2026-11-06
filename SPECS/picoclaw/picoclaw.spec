# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           picoclaw
%define go_import_path  github.com/sipeed/picoclaw

Name:           picoclaw
Version:        0.3.1
Release:        %autorelease
Summary:        PicoClaw: Ultra-Efficient AI Assistant in Go
License:        MIT
URL:            https://github.com/sipeed/picoclaw
#!RemoteAsset:  sha256:df66f2f9a6fecf6f1396311b4a7881afc34d5f4209e2bebd6d91fb2b142d78d0
Source0:        https://github.com/sipeed/picoclaw/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildSystem:    golang

# https://go.dev/doc/godebug
Patch2000:      2000-enable-current-HTTP-routing-for-GOPATH-builds.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go-github-yeongaori-discordgo-fork
BuildRequires:  procps-ng
BuildRequires:  go(fyne.io/systray)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/azcore)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go/sdk/azidentity)
BuildRequires:  go(github.com/SevereCloud/vksdk/v3)
BuildRequires:  go(github.com/adhocore/gronx)
BuildRequires:  go(github.com/anthropics/anthropic-sdk-go) >= 1.50.2
BuildRequires:  go(github.com/atc0005/go-teams-notify/v2)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2/config)
BuildRequires:  go(github.com/caarlos0/env/v11)
BuildRequires:  go(github.com/charmbracelet/lipgloss)
BuildRequires:  go(github.com/creack/pty)
BuildRequires:  go(github.com/eclipse/paho.mqtt.golang)
BuildRequires:  go(github.com/ergochat/irc-go)
BuildRequires:  go(github.com/ergochat/readline)
BuildRequires:  go(github.com/github/copilot-sdk/go)
BuildRequires:  go(github.com/gomarkdown/markdown)
BuildRequires:  go(github.com/google/jsonschema-go)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/gorilla/websocket)
BuildRequires:  go(github.com/h2non/filetype)
BuildRequires:  go(github.com/kagisearch/kagi-openapi-golang)
BuildRequires:  go(github.com/larksuite/oapi-sdk-go/v3)
BuildRequires:  go(github.com/line/line-bot-sdk-go/v8)
BuildRequires:  go(github.com/mdp/qrterminal/v3)
BuildRequires:  go(github.com/minio/selfupdate)
BuildRequires:  go(github.com/modelcontextprotocol/go-sdk) = 1.6.1
BuildRequires:  go(github.com/muesli/termenv)
BuildRequires:  go(github.com/mymmrac/telego)
BuildRequires:  go(github.com/open-dingtalk/dingtalk-stream-sdk-go)
BuildRequires:  go(github.com/openai/openai-go/v3)
BuildRequires:  go(github.com/pion/rtp)
BuildRequires:  go(github.com/pion/webrtc/v3)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/rs/zerolog)
BuildRequires:  go(github.com/slack-go/slack)
BuildRequires:  go(github.com/spf13/cobra)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/tencent-connect/botgo)
BuildRequires:  go(go.mau.fi/util)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/term)
BuildRequires:  go(golang.org/x/time)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/yaml.v3)
BuildRequires:  go(maunium.net/go/mautrix)
BuildRequires:  go(modernc.org/sqlite)

Requires:       procps-ng

%description
PicoClaw is an ultra-lightweight personal AI assistant inspired by NanoBot. It
was rebuilt from the ground up in Go through a "self-bootstrapping" process —
the AI Agent itself drove the architecture migration and code optimization.

%build
%go_common
export GOFLAGS="-buildmode=pie -trimpath"
cd %{_builddir}/go/src/%{go_import_path}
%__go generate ./...
%__go build %{go_build_flags_default} -o %{_builddir}/%{_name} ./cmd/picoclaw
%__go build %{go_build_flags_default} -o %{_builddir}/%{_name}-launcher ./web/backend

%install
install -D -m 0755 %{_builddir}/%{_name} %{buildroot}%{_bindir}/%{_name}
install -D -m 0755 %{_builddir}/%{_name}-launcher %{buildroot}%{_bindir}/%{_name}-launcher

%check -p
export GODEBUG=httpmuxgo121=0

%files
%license LICENSE*
%doc README*
%{_bindir}/%{_name}
%{_bindir}/%{_name}-launcher

%changelog
%autochangelog
