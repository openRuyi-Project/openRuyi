# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           cmux
%define go_import_path  github.com/soheilhy/cmux

Name:           go-github-soheilhy-cmux
Version:        0.1.5
Release:        %autorelease
Summary:        Connection multiplexer for Go network servers
License:        Apache-2.0
URL:            https://github.com/soheilhy/cmux
#!RemoteAsset:  sha256:199232ece74332f408a38e4d38e7ca942b3e66ae58074ca95d3f069693e0dca1
Source0:        https://github.com/soheilhy/cmux/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(google.golang.org/grpc)

Provides:       go(github.com/soheilhy/cmux) = %{version}

Requires:       go(golang.org/x/net)

%description
cmux multiplexes connections on one listener by matching their initial
payload, allowing multiple protocols to share the same network port.

%files
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
