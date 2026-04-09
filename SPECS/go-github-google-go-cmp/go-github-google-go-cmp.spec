# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-cmp
%define go_import_path  github.com/google/go-cmp

Name:           go-github-google-go-cmp
Version:        0.7.0
Release:        %autorelease
Summary:        Package for comparing Go values in tests
License:        BSD-3-Clause
URL:            https://github.com/google/go-cmp
#!RemoteAsset
Source0:        https://github.com/google/go-cmp/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/google/go-cmp) = %{version}

%description
This package is intended to be a more powerful and safer alternative to
reflect.DeepEqual for comparing whether two values are semantically
equal.

The primary features of cmp are:

 * When the default behavior of equality does not suit the needs of the
   test,
   custom equality functions can override the equality operation.
   For example, an equality function may report floats as equal so long as
   they
   are within some tolerance of each other.
 * Types that have an Equal method may use that method to determine
   equality.
   This allows package authors to determine the equality operation for the
   types
   that they define.
 * If no custom equality functions are used and no Equal method is
   defined,
   equality is determined by recursively comparing the primitive kinds on
   both
   values, much like reflect.DeepEqual. Unlike reflect.DeepEqual,
   unexported
   fields are not compared by default; they result in panics unless
   suppressed
   by using an Ignore option (see cmpopts.IgnoreUnexported) or explicitly
   compared using the AllowUnexported option.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
