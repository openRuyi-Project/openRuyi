# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           rardecode
%define go_import_path  github.com/nwaples/rardecode/v2

Name:           go-github-nwaples-rardecode-v2
Version:        2.2.5
Release:        %autorelease
Summary:        A go package for reading RAR archives
License:        BSD-2-Clause
URL:            https://github.com/nwaples/rardecode
#!RemoteAsset:  sha256:8c9cc16f5e0aa08896cf4197b3437d422d857d4e53ade5498866fbf186802c2d
Source0:        https://github.com/nwaples/rardecode/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/nwaples/rardecode/v2) = %{version}

%description
A go package for reading RAR archives.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
