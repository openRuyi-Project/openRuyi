# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           randutil
%define go_import_path  github.com/pion/randutil

Name:           go-github-pion-randutil
Version:        0.1.0
Release:        %autorelease
Summary:        Helper library for cryptographic and mathmatical randoms
License:        MIT
URL:            https://github.com/pion/randutil
#!RemoteAsset:  sha256:4b0301915ebbfa77c8621cebf99c6c7d71651762a33ce4fa4e6af8994ecd4993
Source0:        https://github.com/pion/randutil/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/pion/randutil) = %{version}

%description
Helper library for cryptographic and mathmatical randoms

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
