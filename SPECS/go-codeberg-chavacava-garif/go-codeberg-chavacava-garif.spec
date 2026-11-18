# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           garif
%define go_import_path  codeberg.org/chavacava/garif

Name:           go-codeberg-chavacava-garif
Version:        0.2.1
Release:        %autorelease
Summary:        Static analysis interchange format library for Go
License:        MIT
URL:            https://codeberg.org/chavacava/garif
#!RemoteAsset:  sha256:276211ca817267b996b107126b6036ec1861acfba38d308928cd5f87b23b39c1
Source0:        https://codeberg.org/chavacava/garif/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n garif

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(codeberg.org/chavacava/garif) = %{version}

%description
Static analysis interchange format library for Go.
This package contains the complete upstream source repository and test data.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
