# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           xsync
%define go_import_path  github.com/puzpuzpuz/xsync/v4

Name:           go-github-puzpuzpuz-xsync
Version:        4.4.0
Release:        %autorelease
Summary:        Concurrent data structures for Go
License:        Apache-2.0
URL:            https://github.com/puzpuzpuz/xsync
#!RemoteAsset:  sha256:2cf1919ca2834df8b3fb1b2071eec5d6b6d3246024675047fad211ff8d637755
Source0:        https://github.com/puzpuzpuz/xsync/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/puzpuzpuz/xsync/v4) = %{version}

%description
Concurrent data structures for Go. Aims to provide
more scalable alternatives for some of the data
structures from the standard sync package, but not only.

Apart from direct library dependencies, xsync data
structures can also be met in-code in other libraries
like Otter caching library.

Covered with concurrent stress tests following the
approach described here.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
