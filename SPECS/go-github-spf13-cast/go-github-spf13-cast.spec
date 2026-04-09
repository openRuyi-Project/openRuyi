# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           cast
%define go_import_path  github.com/spf13/cast
%define go_test_exclude_glob github.com/spf13/cast/generator*

Name:           go-github-spf13-cast
Version:        1.10.0
Release:        %autorelease
Summary:        safe and easy casting from one type to another in Go
License:        MIT
URL:            https://github.com/spf13/cast
#!RemoteAsset
Source0:        https://github.com/spf13/cast/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# https://sources.debian.org/src/golang-github-spf13-cast/1.10.0-2/debian/patches/0001-Failing-conversions-are-not-tested-correctly-yet.patch
Patch0:         2000-Failing-conversions-are-not-tested-correctly-yet.patch

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/frankban/quicktest)

Provides:       go(github.com/spf13/cast) = %{version}

Requires:       go(github.com/frankban/quicktest)

%description
Cast is a library to convert between different go types in a consistent
and easy way.

Cast provides simple functions to easily convert a number to a string,
an interface into a bool, etc. Cast does this intelligently when an
obvious conversion is possible. It doesn’t make any attempts to guess
what you meant, for example you can only convert a string to an int when
it is a string representation of an int such as “8”. Cast was developed
for use in Hugo (https://gohugo.io), a website engine which uses YAML,
TOML or JSON for meta data.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
