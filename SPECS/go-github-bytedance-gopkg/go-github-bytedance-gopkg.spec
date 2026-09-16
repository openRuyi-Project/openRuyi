# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gopkg
%define go_import_path  github.com/bytedance/gopkg
# collection/lscq has assembly only for amd64 and arm64
%define go_test_exclude_glob %{shrink:
    %{go_import_path}/collection/lscq
    %{go_import_path}/lang/channel
    %{go_import_path}/cloud/circuitbreaker
}

Name:           go-github-bytedance-gopkg
Version:        0.1.4
Release:        %autorelease
Summary:        Gopkg is a universal utility collection for Go, it complements offerings such as Boost, Better std, Cloud tools
License:        Apache-2.0
URL:            https://github.com/bytedance/gopkg
#!RemoteAsset:  sha256:68096d49c622f240b74a44612520b3aea92277c43d8a45859b4f431bcc496e2c
Source0:        https://github.com/bytedance/gopkg/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/bytedance/gopkg) = %{version}

Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/sys)

%description
gopkg is a universal Go utility collection covering common language,
collection, caching, and cloud computing needs.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
