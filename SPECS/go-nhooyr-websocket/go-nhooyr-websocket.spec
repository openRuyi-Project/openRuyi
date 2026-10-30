# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           websocket-old
%define go_import_path  nhooyr.io/websocket

Name:           go-nhooyr-websocket
Version:        1.8.17
Release:        %autorelease
Summary:        WebSocket library for the nhooyr.io import path
License:        ISC
URL:            https://github.com/nhooyr/websocket-old
#!RemoteAsset:  sha256:d9621607c0dc71442ecd2933f69d05c4094a8c40287709a405d2e30028b5715f
Source0:        https://github.com/nhooyr/websocket-old/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# https://github.com/coder/websocket/commit/aec630d59c74431ffd33ada5a75acf564d27863f
Patch1000:      1000-fix-conform-to-stricter-printf-usage-in-Go-1.24.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
# Retain dependencies of both nested modules, including comparison tests.
BuildRequires:  go(github.com/bytedance/sonic)
BuildRequires:  go(github.com/chenzhuoyu/base64x)
BuildRequires:  go(github.com/gabriel-vasile/mimetype)
BuildRequires:  go(github.com/gin-contrib/sse)
BuildRequires:  go(github.com/gin-gonic/gin)
BuildRequires:  go(github.com/go-playground/locales)
BuildRequires:  go(github.com/go-playground/universal-translator)
BuildRequires:  go(github.com/go-playground/validator/v10)
BuildRequires:  go(github.com/gobwas/httphead)
BuildRequires:  go(github.com/gobwas/pool)
BuildRequires:  go(github.com/gobwas/ws)
BuildRequires:  go(github.com/goccy/go-json)
BuildRequires:  go(github.com/gorilla/websocket)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/klauspost/cpuid/v2)
BuildRequires:  go(github.com/leodido/go-urn)
BuildRequires:  go(github.com/lesismal/llib)
BuildRequires:  go(github.com/lesismal/nbio)
BuildRequires:  go(github.com/mattn/go-isatty)
BuildRequires:  go(github.com/modern-go/concurrent)
BuildRequires:  go(github.com/modern-go/reflect2)
BuildRequires:  go(github.com/pelletier/go-toml/v2)
BuildRequires:  go(github.com/twitchyliquid64/golang-asm)
BuildRequires:  go(github.com/ugorji/go/codec)
BuildRequires:  go(golang.org/x/arch)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/time)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(%{go_import_path}) = %{version}
Provides:       go(%{go_import_path}/internal/bpool) = %{version}
Provides:       go(%{go_import_path}/internal/errd) = %{version}
Provides:       go(%{go_import_path}/internal/test) = %{version}
Provides:       go(%{go_import_path}/internal/test/assert) = %{version}
Provides:       go(%{go_import_path}/internal/test/wstest) = %{version}
Provides:       go(%{go_import_path}/internal/test/xrand) = %{version}
Provides:       go(%{go_import_path}/internal/thirdparty) = %{version}
Provides:       go(%{go_import_path}/internal/util) = %{version}
Provides:       go(%{go_import_path}/internal/xsync) = %{version}
Provides:       go(%{go_import_path}/wsjson) = %{version}

Requires:       go(golang.org/x/time)

%description
This WebSocket implementation provides context-aware connections,
compression, JSON helpers, and net.Conn integration. It preserves the
nhooyr.io/websocket import path used by existing applications and includes
the complete upstream repository with examples and comparison tests.

%prep -a
# Install the nested example module at its declared import path and keep
# its local replacement pointing to the complete parent module.
mv internal/examples examples
sed -i 's|=> ../..$|=> ..|' examples/go.mod

%files
%doc README.md
%license LICENSE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
