# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-textseg
%define go_import_path  github.com/apparentlymart/go-textseg/v17

Name:           go-github-apparentlymart-go-textseg-v17
Version:        17.0.1
Release:        %autorelease
Summary:        Go implementation of Unicode Text Segmentation
License:        Apache-2.0 OR MIT OR Unicode-DFS-2016
URL:            https://github.com/apparentlymart/go-textseg
#!RemoteAsset:  sha256:e3693eb5cf1b9a79743b7d7a7bba17bd517487b5e9d8c310f365dfa21ee9ca84
Source0:        https://github.com/apparentlymart/go-textseg/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/apparentlymart/go-textseg/v17) = %{version}

%description
This is an implementation of the Unicode Text Segmentation specification
for Go. Specifically, it currently includes only the "grapheme cluster"
segmentation algorithm.

%prep -a
# autoversion is a separate Go module that depends on older go-textseg majors - Jvle
rm -rf autoversion

%files
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
