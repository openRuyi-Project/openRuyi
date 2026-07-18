# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-textseg
%define go_import_path  github.com/apparentlymart/go-textseg/v15

Name:           go-github-apparentlymart-go-textseg-v15
Version:        15.0.0
Release:        %autorelease
Summary:        Go implementation of Unicode Text Segmentation
License:        Apache-2.0 OR MIT OR Unicode-DFS-2016
URL:            https://github.com/apparentlymart/go-textseg
#!RemoteAsset:  sha256:d73ee2bce8c1a8e35b0355a8cb66d05cd65a07099b7edaf1e44edc51cf33210d
Source0:        https://github.com/apparentlymart/go-textseg/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/apparentlymart/go-textseg/v15) = %{version}

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
