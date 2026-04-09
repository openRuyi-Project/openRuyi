# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           vecf64
%define go_import_path  gorgonia.org/vecf64

Name:           go-gorgonia-vecf64
Version:        0.9.0
Release:        %autorelease
Summary:        package vecf64 provides common functions and methods for slices of float64
License:        MIT
URL:            https://github.com/gorgonia/vecf64
#!RemoteAsset
Source0:        https://github.com/gorgonia/vecf64/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(gorgonia.org/vecf64) = %{version}

Requires:       go(github.com/stretchr/testify)

%description
This package provides common functions and methods for slices of float64

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
