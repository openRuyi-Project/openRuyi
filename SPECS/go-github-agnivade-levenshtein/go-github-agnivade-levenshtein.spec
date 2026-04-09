# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           levenshtein
%define go_import_path  github.com/agnivade/levenshtein

Name:           go-github-agnivade-levenshtein
Version:        1.2.1
Release:        %autorelease
Summary:        Go implementation to calculate Levenshtein Distance.
License:        MIT
URL:            https://github.com/agnivade/levenshtein
#!RemoteAsset
Source0:        https://github.com/agnivade/levenshtein/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# https://sources.debian.org/data/main/g/golang-github-agnivade-levenshtein/1.2.0-1/debian/patches/0001-remove-benchmark-only-dependencies.patch
Patch0:         2000-remove-benchmark-only-dependencies.patch

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/agnivade/levenshtein) = %{version}

%description
The library is fully capable of working with non-ascii strings. But the
strings are not normalized. That is left as a user-dependant use case.
Please normalize the strings before passing it to the library if you
have such a requirement.

%files
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
