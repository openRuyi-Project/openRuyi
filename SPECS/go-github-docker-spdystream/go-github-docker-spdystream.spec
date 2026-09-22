# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           spdystream
%define go_import_path  github.com/docker/spdystream
%define go_test_include %{shrink:
    %{go_import_path}
    %{go_import_path}/spdy
}

Name:           go-github-docker-spdystream
Version:        0+git20160310.449fdfc
Release:        %autorelease
Summary:        A multiplexed stream library using spdy
License:        Apache-2.0
URL:            https://github.com/docker/spdystream
VCS:            git:https://github.com/docker/spdystream.git
#!RemoteAsset:  sha256:4e1fe2258502e5eebaca247caf93fd63a0ddf92a0388d65bf6be42c833a2e549
Source0:        https://github.com/docker/spdystream/archive/449fdfce4d96.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n spdystream-449fdfce4d962303d702fec724ef0ad181c92528
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gorilla/websocket)

Provides:       go(github.com/docker/spdystream) = %{version}

Requires:       go(github.com/gorilla/websocket)

%description
This package provides the github.com/docker/spdystream Go module source.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
