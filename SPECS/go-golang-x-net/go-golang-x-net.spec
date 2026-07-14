# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           net
%define go_import_path  golang.org/x/net
# So tired, can't stand more flaky tests - 251
%define go_test_exclude_glob %{shrink:
    golang.org/x/net/http2
    golang.org/x/net/quic
}

Name:           go-golang-x-net
Version:        0.56.0
Release:        %autorelease
Summary:        Go supplementary network libraries
License:        BSD-3-Clause
URL:            https://golang.org/x/net
VCS:            git:https://github.com/golang/net
#!RemoteAsset:  sha256:c2097a7d1043e482386bf71f4df9d4e269685809ad057e1c42fa58e5dd8ff4ec
Source0:        https://github.com/golang/net/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/term)
BuildRequires:  go(golang.org/x/text)

Provides:       go(golang.org/x/net) = %{version}

Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/term)
Requires:       go(golang.org/x/text)

%description
This package provides supplementary Go networking libraries.

%check -p
# GOPATH mode does not read the module's Go version, but synctest requires the
# modern timer channel implementation selected by the upstream go directive.
export GODEBUG=asynctimerchan=0

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
