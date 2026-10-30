# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gosmopolitan
%define go_import_path  github.com/xen0n/gosmopolitan

Name:           go-github-xen0n-gosmopolitan
Version:        1.3.0
Release:        %autorelease
Summary:        Go analyzer for internationalization and localization issues
License:        GPL-3.0-or-later
URL:            https://github.com/xen0n/gosmopolitan
#!RemoteAsset:  sha256:e5b11f7fa65736730b35fe983ac9d77568eaf545e3500cd8d7e2eee279a212a8
Source0:        https://github.com/xen0n/gosmopolitan/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/xen0n/gosmopolitan) = %{version}

Requires:       go(golang.org/x/text)
Requires:       go(golang.org/x/tools)

%description
Go analyzer for internationalization and localization issues.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n gosmopolitan-%{version}

%files
%doc README.md README.zh-Hans.md
%license LICENSE
%{go_sys_gopath}/github.com/xen0n/gosmopolitan

%changelog
%autochangelog
