# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           thelper
%define go_import_path  github.com/kulti/thelper

Name:           go-github-kulti-thelper
Version:        0.7.1
Release:        %autorelease
Summary:        Thelper detects golang test helpers without t.Helper() call
License:        MIT
URL:            https://github.com/kulti/thelper
#!RemoteAsset:  sha256:b087aec500dbcc27b9d6901773fbeaee65d57a68f2eb69648a5a704c25c91fc3
Source0:        https://github.com/kulti/thelper/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/kulti/thelper) = %{version}
Provides:       go(github.com/kulti/thelper/pkg/analyzer) = %{version}

Requires:       go(golang.org/x/tools)

%description
Thelper detects golang test helpers without t.Helper() call.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n thelper-%{version}

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/kulti/thelper

%changelog
%autochangelog
