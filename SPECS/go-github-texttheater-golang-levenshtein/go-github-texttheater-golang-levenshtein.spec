# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           golang-levenshtein
%define go_import_path  github.com/texttheater/golang-levenshtein

Name:           go-github-texttheater-golang-levenshtein
Version:        0+git20180516.d188e65
Release:        %autorelease
Summary:        An implementation of the Levenshtein algorithm in Go
License:        MIT
URL:            https://github.com/texttheater/golang-levenshtein
VCS:            git:https://github.com/texttheater/golang-levenshtein.git
#!RemoteAsset:  sha256:656f2a68d9d856e4d4d1dbee36936740fd4b35ca12f4e4c6977b083fe164577a
Source0:        https://github.com/texttheater/golang-levenshtein/archive/d188e65d659e.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n golang-levenshtein-d188e65d659ef53fcdb0691c12f1bba64928b649

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/texttheater/golang-levenshtein) = %{version}

%description
This package provides the github.com/texttheater/golang-levenshtein Go module source.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
