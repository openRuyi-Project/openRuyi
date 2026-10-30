# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           grouper
%define go_import_path  github.com/leonklingele/grouper

Name:           go-github-leonklingele-grouper
Version:        1.1.2
Release:        %autorelease
Summary:        Go analyzer for grouped declarations and expressions
License:        GPL-3.0-only
URL:            https://github.com/leonklingele/grouper
#!RemoteAsset:  sha256:bf837884321f25dd3d726fd607dd7340217d74c37881be8dc0a9ffde39a394ec
Source0:        https://github.com/leonklingele/grouper/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/leonklingele/grouper) = %{version}
Provides:       go(github.com/leonklingele/grouper/pkg/analyzer) = %{version}
Provides:       go(github.com/leonklingele/grouper/pkg/analyzer/consts) = %{version}
Provides:       go(github.com/leonklingele/grouper/pkg/analyzer/globals) = %{version}
Provides:       go(github.com/leonklingele/grouper/pkg/analyzer/imports) = %{version}
Provides:       go(github.com/leonklingele/grouper/pkg/analyzer/types) = %{version}
Provides:       go(github.com/leonklingele/grouper/pkg/analyzer/vars) = %{version}

Requires:       go(golang.org/x/tools)

%description
Go analyzer for grouped declarations and expressions.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n grouper-%{version}
# Use packaged dependencies instead of the bundled snapshots.
rm -rf vendor

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/github.com/leonklingele/grouper

%changelog
%autochangelog
