# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           containedctx
%define go_import_path  github.com/sivchari/containedctx

Name:           go-github-sivchari-containedctx
Version:        1.0.3
Release:        %autorelease
Summary:        Containedctx is a linter that detects struct contained context.Context field
License:        MIT
URL:            https://github.com/sivchari/containedctx
#!RemoteAsset:  sha256:08ff59d62131d4793d803c31cc77983c5dec380d8ba2728e755525d3a439f6b7
Source0:        https://github.com/sivchari/containedctx/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gostaticanalysis/testutil)
BuildRequires:  go(github.com/hashicorp/go-version)
BuildRequires:  go(github.com/otiai10/copy)
BuildRequires:  go(github.com/tenntenn/modver)
BuildRequires:  go(github.com/tenntenn/text/transform)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/sivchari/containedctx) = %{version}

Requires:       go(golang.org/x/tools)

%description
Containedctx is a linter that detects struct contained context.Context field.
This package contains the complete upstream Go source and test data.

%prep
%autosetup -p1 -n containedctx-%{version}

%files
%doc README.md
%license LICENCE
%{go_sys_gopath}/github.com/sivchari/containedctx

%changelog
%autochangelog
