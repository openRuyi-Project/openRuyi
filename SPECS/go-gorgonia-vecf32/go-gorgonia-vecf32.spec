# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           vecf32
%define go_import_path  gorgonia.org/vecf32

Name:           go-gorgonia-vecf32
Version:        0.9.0
Release:        %autorelease
Summary:        Package vecf32 provides common functions and methods for slices of float32
License:        MIT
URL:            https://github.com/gorgonia/vecf32
#!RemoteAsset
Source0:        https://github.com/gorgonia/vecf32/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/chewxy/math32)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(gorgonia.org/vecf32) = %{version}

Requires:       go(github.com/chewxy/math32)
Requires:       go(github.com/stretchr/testify)

%description
This package provides common functions and methods for slices of float32

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
