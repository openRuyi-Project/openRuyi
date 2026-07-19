# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           goutils
%define go_import_path  github.com/Masterminds/goutils

Name:           go-github-masterminds-goutils
Version:        1.1.1
Release:        %autorelease
Summary:        Provides utility functions to manipulate strings in various ways
License:        Apache-2.0
URL:            https://github.com/Masterminds/goutils
#!RemoteAsset:  sha256:6eed023c54f386a71f360e19d34f7a43e640ac44dfc39c22ad4afd7ae04aaa3d
Source0:        https://github.com/Masterminds/goutils/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/Masterminds/goutils) = %{version}

%description
GoUtils provides users with utility functions to manipulate strings in
various ways. It is a Go implementation of some string manipulation
libraries of Java Apache Commons. GoUtils includes the following Java
Apache Commons classes:

 * WordUtils
 * RandomStringUtils
 * StringUtils (partial implementation)

%files
%doc README.md
%license LICENSE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
