# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gcfg
%define go_import_path  github.com/go-git/gcfg/v2

Name:           go-github-go-git-gcfg
Version:        2.0.2
Release:        %autorelease
Summary:        go-gcfg/gcfg fork for usage in src-d/go-git
License:        BSD-3-Clause
URL:            https://github.com/go-git/gcfg
#!RemoteAsset:  sha256:2d8f25f12e4bec0349cdc5265bca20803adde83edb6fe31690e52506914fe5e3
Source0:        https://github.com/go-git/gcfg/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/go-git/gcfg) = %{version}
Provides:       go(github.com/go-git/gcfg/v2) = %{version}

%description
Gcfg reads INI-style configuration files into Go structs;
supports user-defined types and subsections.

%install -a
# Keep the existing unversioned import path for its current consumers while
# installing the canonical v2 module and its internal imports at their own path.
cp -a . %{buildroot}%{go_sys_gopath}/github.com/go-git/gcfg/

%check -a
# Check the compatibility import using the same sources shipped in the RPM.
export GOPATH=%{buildroot}%{_datadir}/gocode:%{_builddir}/go:%{_datadir}/gocode
%__go test %{go_test_flags_default} github.com/go-git/gcfg

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/github.com/go-git/gcfg

%changelog
%autochangelog
