# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           backscanner
%define go_import_path  github.com/icza/backscanner
%define commit_id       dff01ac5025040317bf654624506b84cb2f74e29

Name:           go-github-icza-backscanner
Version:        0+git20260716.dff01ac
Release:        %autorelease
Summary:        Scanner for reading lines backwards in Go
License:        Apache-2.0
URL:            https://github.com/icza/backscanner
VCS:            git:https://github.com/icza/backscanner.git
#!RemoteAsset:  sha256:44f02969457f6d8d3492da576ebe54b0e3d438a48a2a092e4e67c37223603008
Source0:        https://codeload.github.com/icza/backscanner/tar.gz/%{commit_id}#/backscanner-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n backscanner-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
# mighty is used only by the test suite.
BuildRequires:  go(github.com/icza/mighty)

Provides:       go(github.com/icza/backscanner) = %{version}

%description
Backscanner is a Go package that scans lines from an input source in reverse
order.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
