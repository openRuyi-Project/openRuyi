# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           stringprep
%define go_import_path  github.com/xdg/stringprep

Name:           go-github-xdg-stringprep
Version:        1.0.3
Release:        %autorelease
Summary:        Legacy stringprep library → use xdg-go/stringprep instead
License:        Apache-2.0
URL:            https://github.com/xdg/stringprep
#!RemoteAsset
Source0:        https://github.com/xdg/stringprep/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/text)

Provides:       go(github.com/xdg/stringprep) = %{version}

%description
This library provides an implementation of the stringprep algorithm
(RFC-3454) in Go, including all data tables.

A pre-built SASLprep (RFC-4013) profile is provided as well.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
