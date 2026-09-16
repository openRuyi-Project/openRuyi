# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           participle
%define go_import_path  github.com/alecthomas/participle

Name:           go-github-alecthomas-participle
Version:        0.7.1
Release:        %autorelease
Summary:        Parser library for Go
License:        MIT
URL:            https://github.com/alecthomas/participle
#!RemoteAsset:  sha256:02cf63652bd2b6be77dd2a99a1a3d1983c209eaeb999c5c51976b4db29bec064
Source0:        https://github.com/alecthomas/participle/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# lexer.Errorf takes a non-constant format string; Go 1.27 vet rejects it.
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/alecthomas/repr)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/alecthomas/participle) = %{version}

%description
participle constructs parsers from Go struct tags. This is the
unversioned v0 module; github.com/alecthomas/participle/v2 is packaged
separately.

%prep -a
# _examples are sample programs, not the library.
rm -rf _examples

%files
%doc README.md TUTORIAL.md
%license COPYING
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
