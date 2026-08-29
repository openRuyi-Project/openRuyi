# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           cachecontrol
%define go_import_path  github.com/pquerna/cachecontrol

Name:           go-github-pquerna-cachecontrol
Version:        0.2.0
Release:        %autorelease
Summary:        Implements the logic for HTTP Caching
License:        Apache-2.0
URL:            https://github.com/pquerna/cachecontrol
#!RemoteAsset:  sha256:cfe3fd03d57f1e06d2d4df587383e50b087667fdd23dcc89300e4b47c7a66fef
Source0:        https://github.com/pquerna/cachecontrol/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/pquerna/cachecontrol) = %{version}

%description
HTTP Caching Parser and Interpretation

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
