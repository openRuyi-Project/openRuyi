# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           httpunix
%define go_import_path  github.com/tv42/httpunix
%define commit_id 2ba4b9c3382c77e7b9ea89d00746e6111d142a22

Name:           go-github-tv42-httpunix
Version:        0+git20260607.2ba4b9c
Release:        %autorelease
Summary:        Go library to talk HTTP over Unix domain sockets
License:        MIT
URL:            https://github.com/tv42/httpunix
#!RemoteAsset:  sha256:cebdb837a242a4f4a50c2a5a834d64ecf0fb35d34c1f37e45b2db34651a87901
Source0:        https://github.com/tv42/httpunix/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/tv42/httpunix) = %{version}

%description
httpunix provides helpers for sending HTTP requests over Unix domain sockets.

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
