# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           tabwriter
%define go_import_path  github.com/liggitt/tabwriter
%define commit_id       89fcab3d43de07060e4fd4c1547430ed57e87f24

Name:           go-github-liggitt-tabwriter
Version:        0+git20260922.89fcab3
Release:        %autorelease
Summary:        Align tabbed text with remembered column widths
License:        BSD-3-Clause
URL:            https://github.com/liggitt/tabwriter
#!RemoteAsset:  sha256:7abd90599d0cbc9900e6d682a88249fc085e15a055eefc8e8b247890a10d8945
Source0:        https://github.com/liggitt/tabwriter/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/liggitt/tabwriter) = %{version}

%description
This library extends Go's text/tabwriter with remembered column widths
that can be reused after flushing or transferred between writers.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
