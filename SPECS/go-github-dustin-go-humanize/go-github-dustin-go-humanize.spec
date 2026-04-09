# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-humanize
%define go_import_path  github.com/dustin/go-humanize

Name:           go-github-dustin-go-humanize
Version:        1.0.1
Release:        %autorelease
Summary:        Go Humans! (formatters for units to human friendly sizes)
License:        MIT
URL:            https://github.com/dustin/go-humanize
#!RemoteAsset
Source0:        https://github.com/dustin/go-humanize/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/dustin/go-humanize) = %{version}

%description
Just a few functions for helping humanize times and sizes.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
