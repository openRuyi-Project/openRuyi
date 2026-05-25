# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           socket
%define go_import_path  github.com/mdlayher/socket

Name:           go-github-mdlayher-socket
Version:        0.6.0
Release:        %autorelease
Summary:        Package socket provides a low-level network connection type which integrates with Go's runtime network poller to provide asynchronous I/O and deadline support. MIT Licensed.
License:        MIT
URL:            https://github.com/mdlayher/socket
#!RemoteAsset:  sha256:4832cc911767d0a22f3b7c4288518d51c522ed43ee0b3128554952c1b9016c6e
Source0:        https://github.com/mdlayher/socket/archive/refs/tags/v0.6.0.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n socket-0.6.0

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/go-cmp/cmp)
BuildRequires:  go(github.com/google/go-cmp/cmp/cmpopts)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/net/bpf)
BuildRequires:  go(golang.org/x/net/nettest)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sync/errgroup)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/sys/unix)

Provides:       go(github.com/mdlayher/socket) = %{version}
Provides:       go(github.com/mdlayher/socket/internal/sockettest) = %{version}

Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/net/bpf)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/sync/errgroup)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/sys/unix)


%description
socket [Image: Test Status]
(https://github.com/mdlayher/socket/workflows/Test/badge.svg)
(https://github.com/mdlayher/socket/actions) [Image: Go Reference]
(https://pkg.go.dev/badge/github.com/mdlayher/socket.svg)
(https://pkg.go.dev/github.com/mdlayher/socket) [Image: Go Report Card]
(https://goreportcard.com/badge/github.com/mdlayher/socket)
(https://goreportcard.com/report/github.com/mdlayher/socket)

Package socket provides a low-level network connection type which
integrates with Go's runtime network poller to provide asynchronous I/O
and deadline support. MIT Licensed.

%files
%doc README.md
%doc CHANGELOG.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
