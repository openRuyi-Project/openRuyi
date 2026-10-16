# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           spdystream
%define go_import_path  github.com/docker/spdystream
%define commit_id       449fdfce4d962303d702fec724ef0ad181c92528

Name:           go-github-docker-spdystream
Version:        0+git20260922.449fdfc
Release:        %autorelease
Summary:        Multiplexed streams using SPDY for Go
License:        Apache-2.0 AND BSD-3-Clause AND CC-BY-SA-4.0
URL:            https://github.com/docker/spdystream
#!RemoteAsset:  sha256:4e1fe2258502e5eebaca247caf93fd63a0ddf92a0388d65bf6be42c833a2e549
Source0:        https://github.com/docker/spdystream/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
# The spdy package retains Go BSD headers; the archive omits their license text.
# https://github.com/golang/go/blob/go1.6.1/LICENSE
Source1:        LICENSE.Go
BuildArch:      noarch
BuildSystem:    golangmodules

# https://github.com/moby/spdystream/commit/aef7e4d3b91cd2ae97dde4e2260c828465a9573b
Patch1000:      1000-Fix-WebSocket-stream-handling-and-tests.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gorilla/websocket)

Provides:       go(github.com/docker/spdystream) = %{version}

Requires:       go(github.com/gorilla/websocket)

%description
Multiplexed streams using SPDY for Go.

%prep -a
cp %{SOURCE1} LICENSE.Go

%files
%doc README.md
%license LICENSE LICENSE.docs LICENSE.Go
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
