# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           structtag
%define go_import_path  github.com/alfatraining/structtag

Name:           go-github-alfatraining-structtag
Version:        1.0.0
Release:        %autorelease
Summary:        Struct tag parser for Go static analysis
License:        BSD-3-Clause AND CC-BY-3.0
URL:            https://github.com/alfatraining/structtag
#!RemoteAsset:  sha256:1ca310889612735c7614f4d71a73ae0080d3129fbc33a4be73a2fd474db95307
Source0:        https://github.com/alfatraining/structtag/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go >= 1.22
BuildRequires:  go-rpm-macros

# Export the source module roots and every installed Go package.
Provides:       go(github.com/alfatraining/structtag) = %{version}

%description
Struct tag parser for Go static analysis. This package contains the complete
upstream repository sources and tests.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
