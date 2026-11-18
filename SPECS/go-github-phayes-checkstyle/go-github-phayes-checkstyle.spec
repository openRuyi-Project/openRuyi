# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           checkstyle
%define go_import_path  github.com/phayes/checkstyle
%define commit_id       bfd46e6a821d07762e664fb4fdde8bb90bb3668c

Name:           go-github-phayes-checkstyle
Version:        0+git20261029.bfd46e6
Release:        %autorelease
Summary:        Read and write Checkstyle XML reports in Go
License:        BSD-3-Clause
URL:            https://github.com/phayes/checkstyle
#!RemoteAsset:  sha256:2f103e80ce894894c9162ee69f5d40483b77641f25345d63b443426df229ffe7
Source0:        https://github.com/phayes/checkstyle/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
Checkstyle reads, creates, and writes Checkstyle XML reports containing
source-code diagnostics. The complete source repository includes its
upstream serialization tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
