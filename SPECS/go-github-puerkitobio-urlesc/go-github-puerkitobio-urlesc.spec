# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           urlesc
%define go_import_path  github.com/PuerkitoBio/urlesc
%define commit_id       de5bf2ad457846296e2031421a34e2568e304e35

Name:           go-github-puerkitobio-urlesc
Version:        0+git20260922.de5bf2a
Release:        %autorelease
Summary:        URL escaping utilities for Go
License:        BSD-3-Clause
URL:            https://github.com/PuerkitoBio/urlesc
#!RemoteAsset:  sha256:4bf883606155d8ed9c8ca5bd794e412025a16e3532d2b06053ff95f74fc3a9b2
Source0:        https://github.com/PuerkitoBio/urlesc/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/PuerkitoBio/urlesc) = %{version}

%description
URL escaping utilities for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
