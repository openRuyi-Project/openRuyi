# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           float16
%define go_import_path  github.com/x448/float16

Name:           go-github-x448-float16
Version:        0.8.4
Release:        %autorelease
Summary:        float16 provides IEEE 754 half-precision format (binary16) with correct conversions to/from float32
License:        MIT
URL:            https://github.com/x448/float16
#!RemoteAsset
Source0:        https://github.com/x448/float16/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/x448/float16) = %{version}

%description
x448/float16 (https://github.com/x448/float16) package provides IEEE 754
half-precision floating-point format (binary16)
(https://en.wikipedia.org/wiki/Half-precision_floating-point_format)
with
IEEE 754 default rounding for conversions. IEEE 754-2008 refers to this
16-bit floating-point format as binary16.

IEEE 754 default rounding ("Round-to-Nearest RoundTiesToEven") is
considered the most accurate and statistically unbiased estimate of the
true result.

All possible 4+ billion floating-point conversions with this library are
verified to be correct.

Lowercase "float16" refers to IEEE 754 binary16. And capitalized
"Float16" refers to exported Go data type.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
