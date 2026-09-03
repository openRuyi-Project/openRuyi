# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           logfmt
%define go_import_path  github.com/kr/logfmt
%define commit_id       b84e30acd515aadc4b783ad4ff83aff3299bdfe0

Name:           go-github-kr-logfmt
Version:        0+git20260621.b84e30a
Release:        %autorelease
Summary:        Parse logfmt messages
License:        MIT
URL:            https://github.com/kr/logfmt
#!RemoteAsset:  sha256:64330d721cb3144dafc214200303c1690add04d47f09926425c5f28affe30218
Source0:        https://github.com/kr/logfmt/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/kr/logfmt) = %{version}

%description
logfmt is a Go parser for the logfmt structured logging format.

%files
%doc Readme
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
