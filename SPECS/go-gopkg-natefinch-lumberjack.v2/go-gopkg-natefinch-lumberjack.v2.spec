# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           lumberjack
%define go_import_path  gopkg.in/natefinch/lumberjack.v2

Name:           go-gopkg-natefinch-lumberjack.v2
Version:        2.2.1
Release:        %autorelease
Summary:        Rolling log file writer for Go
License:        MIT
URL:            https://github.com/natefinch/lumberjack
#!RemoteAsset:  sha256:935582f3f3377f09604bce4ab0488092d71c0d9ff3e9359a397f00ab6caed658
Source0:        https://github.com/natefinch/lumberjack/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
Lumberjack provides a Go log writer that rotates files according to size, age,
and backup count limits.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
