# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           urlesc
%define go_import_path  github.com/PuerkitoBio/urlesc

Name:           go-github-puerkitobio-urlesc
Version:        0+git20170810.de5bf2a
Release:        %autorelease
Summary:        Implements query escaping as per RFC 3986
License:        BSD-3-Clause
URL:            https://github.com/PuerkitoBio/urlesc
VCS:            git:https://github.com/PuerkitoBio/urlesc.git
#!RemoteAsset:  sha256:4bf883606155d8ed9c8ca5bd794e412025a16e3532d2b06053ff95f74fc3a9b2
Source0:        https://github.com/PuerkitoBio/urlesc/archive/de5bf2ad4578.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n urlesc-de5bf2ad457846296e2031421a34e2568e304e35

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/PuerkitoBio/urlesc) = %{version}

%description
This package provides the github.com/PuerkitoBio/urlesc Go module source.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
