# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           filepath-securejoin
%define go_import_path  github.com/cyphar/filepath-securejoin
# OBS returns "resource temporarily unavailable" for several openat2 symlink
# loop cases, and the racing mkdir stress test hits "too many open files" on
# riscv64. TestPartialLookup_RacingRename also exceeds the 10m go test timeout
# on riscv64 workers, so skip this test package. - HNO3Miracle
%define go_test_exclude_glob %{go_import_path}*

Name:           go-github-cyphar-filepath-securejoin
Version:        0.7.0
Release:        %autorelease
Summary:        Secure path joining helpers for Go
License:        BSD-3-Clause AND MPL-2.0
URL:            https://github.com/cyphar/filepath-securejoin
#!RemoteAsset:  sha256:f3bef272555f9ffefff504762ec92235cfe50891dedba1c2281d970323d7c367
Source0:        https://github.com/cyphar/filepath-securejoin/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/davecgh/go-spew)
BuildRequires:  go(github.com/pmezard/go-difflib)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(github.com/cyphar/filepath-securejoin) = %{version}

Requires:       go(golang.org/x/sys)

%description
filepath-securejoin provides helpers for securely joining untrusted path
components under a trusted root without escaping that root.

%files
%doc CHANGELOG.md
%doc README.md
%license COPYING.md
%license LICENSE.BSD
%license LICENSE.MPL-2.0
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
