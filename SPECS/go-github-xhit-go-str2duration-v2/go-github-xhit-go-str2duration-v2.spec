# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-str2duration
%define go_import_path  github.com/xhit/go-str2duration/v2

Name:           go-github-xhit-go-str2duration-v2
Version:        2.1.0
Release:        %autorelease
Summary:        Convert string to duration in golang
License:        BSD-3-Clause
URL:            https://github.com/xhit/go-str2duration
#!RemoteAsset
Source0:        https://github.com/xhit/go-str2duration/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/xhit/go-str2duration/v2) = %{version}

%description
Go String To Duration (go-str2duration)

This package allows to get a time.Duration from a string. The string can
be a string retorned for time.Duration or a similar string with weeks or
days too!.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
