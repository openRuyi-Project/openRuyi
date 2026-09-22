# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           etree
%define go_import_path  github.com/beevik/etree

Name:           go-github-beevik-etree
Version:        1.1.0
Release:        %autorelease
Summary:        Provides XML services through an Element Tree abstraction
License:        BSD-2-Clause
URL:            https://github.com/beevik/etree
VCS:            git:https://github.com/beevik/etree.git
#!RemoteAsset:  sha256:d1b424a126ce5c46d8e9ba42217e7997cc992bef56d17cc39d1d91525c0dc1de
Source0:        https://github.com/beevik/etree/archive/v1.1.0.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n etree-1.1.0

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/beevik/etree) = %{version}

%description
This package provides the github.com/beevik/etree Go module source.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
