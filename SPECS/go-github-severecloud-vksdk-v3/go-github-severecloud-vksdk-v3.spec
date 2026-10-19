# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           vksdk
%define go_import_path  github.com/SevereCloud/vksdk/v3
%define go_test_exclude %{shrink:
    %{go_import_path}
    %{go_import_path}/api
    %{go_import_path}/api/oauth
    %{go_import_path}/callback
}

Name:           go-github-severecloud-vksdk-v3
Version:        3.3.1
Release:        %autorelease
Summary:        VK SDK for Golang
License:        MIT
URL:            https://github.com/SevereCloud/vksdk
#!RemoteAsset:  sha256:ccfb7c97526135efe9b03c44d7da06f0eaad0b77fff56426f8444828da677368
Source0:        https://github.com/SevereCloud/vksdk/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gorilla/schema)
BuildRequires:  go(github.com/gorilla/websocket)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/vmihailenco/msgpack/v5)
BuildRequires:  go(golang.org/x/text)

Provides:       go(github.com/SevereCloud/vksdk/v3) = %{version}

Requires:       go(github.com/gorilla/schema)
Requires:       go(github.com/gorilla/websocket)
Requires:       go(github.com/klauspost/compress)
Requires:       go(github.com/vmihailenco/msgpack/v5)
Requires:       go(golang.org/x/text)

%description
VK SDK for Golang ready implementation of the main VK API functions for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
