# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-intervals
%define go_import_path  github.com/google/go-intervals

Name:           go-github-google-go-intervals
Version:        0.0.2
Release:        %autorelease
Summary:        Go-intervals is a library for performing set operations on 1-dimensional
License:        Apache-2.0
URL:            https://github.com/google/go-intervals
#!RemoteAsset:  sha256:8a8e2d3d6b831e6e40572040e6ef794a4c2d25ff988a3232378f98cbd24bc729
Source0:        https://github.com/google/go-intervals/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  tzdata

Provides:       go(github.com/google/go-intervals) = %{version}

%description
A golang library for set operations on intervals, such as time ranges.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
