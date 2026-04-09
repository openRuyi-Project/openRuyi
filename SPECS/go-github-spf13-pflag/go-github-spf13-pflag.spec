# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           pflag
%define go_import_path  github.com/spf13/pflag

Name:           go-github-spf13-pflag
Version:        1.0.10
Release:        %autorelease
Summary:        Drop-in replacement for Go's flag package, implementing POSIX/GNU-style --flags.
License:        BSD-3-Clause
URL:            https://github.com/spf13/pflag
#!RemoteAsset
Source0:        https://github.com/spf13/pflag/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/spf13/pflag) = %{version}

%description
pflag is a drop-in replacement for Go's flag package, implementing
POSIX/GNU-style --flags.

pflag is compatible with the GNU extensions to the POSIX recommendations
for command-line options
(http://www.gnu.org/software/libc/manual/html_node/Argument-Syntax.html).
For a more precise description, see the "Command-line flag syntax"
section below.

pflag is available under the same style of BSD license as the Go
language, which can be found in the LICENSE file.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
