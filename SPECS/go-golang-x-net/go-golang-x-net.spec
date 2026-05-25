# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
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
Version:        0.48.0
Release:        %autorelease
Summary:        Go supplementary network libraries
License:        BSD-3-Clause
URL:            https://golang.org/x/net
VCS:            git:https://github.com/golang/net
#!RemoteAsset:  sha256:999b4eeae1b018ce0e2353cd656b47297c57fedcb9a419904ff856de0438898f
Source0:        https://github.com/golang/net/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/term)
BuildRequires:  go(golang.org/x/text)

Provides:       go(golang.org/x/net) = %{version}
Provides:       go(golang.org/x/net/bpf) = %{version}
Provides:       go(golang.org/x/net/context) = %{version}
Provides:       go(golang.org/x/net/context/ctxhttp) = %{version}
Provides:       go(golang.org/x/net/html/charset) = %{version}
Provides:       go(golang.org/x/net/http/httpguts) = %{version}
Provides:       go(golang.org/x/net/http2) = %{version}
Provides:       go(golang.org/x/net/http2/hpack) = %{version}
Provides:       go(golang.org/x/net/idna) = %{version}
Provides:       go(golang.org/x/net/internal/httpcommon) = %{version}
Provides:       go(golang.org/x/net/nettest) = %{version}
Provides:       go(golang.org/x/net/proxy) = %{version}
Provides:       go(golang.org/x/net/publicsuffix) = %{version}
Provides:       go(golang.org/x/net/websocket) = %{version}

Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/term)
Requires:       go(golang.org/x/text)

%description
This package provides supplementary Go networking libraries.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
