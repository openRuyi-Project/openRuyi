# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           math32
%define go_import_path  github.com/chewxy/math32

Name:           go-github-chewxy-math32
Version:        1.11.1
Release:        %autorelease
Summary:        A float32 version of Go's math package
License:        BSD-2-Clause
URL:            https://github.com/chewxy/math32
#!RemoteAsset
Source0:        https://github.com/chewxy/math32/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/chewxy/math32) = %{version}

%description
A float32 version of Go's math package. The majority of code in this
library is a thin float32 wrapper over the results of the math package
that comes in the standard lib.

The original code is lifted from the Go standard library which is
governed by a BSD-style licence which can be found here:
(https://golang.org/LICENSE).

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
