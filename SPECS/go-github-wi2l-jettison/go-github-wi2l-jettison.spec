# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           jettison
%define go_import_path  github.com/wI2L/jettison

Name:           go-github-wi2l-jettison
Version:        0.7.4
Release:        %autorelease
Summary:        Highly configurable, fast JSON encoder for Go
License:        MIT
URL:            https://github.com/wI2L/jettison
#!RemoteAsset:  sha256:734d973c14b6b8fae9a0e3f00e5c049bf6c879f335d3ae851bc9496e8c8bc8b9
Source0:        https://github.com/wI2L/jettison/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n jettison-0.7.4
# Go 1.25 encodes \b and \f differently from the old stdlib output expected
# by this upstream compatibility test; the rest of the suite still runs.
BuildOption(check):  -skip TestStringEscaping

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/modern-go/concurrent)
BuildRequires:  go(github.com/modern-go/reflect2)
BuildRequires:  go(github.com/segmentio/asm)
BuildRequires:  go(github.com/segmentio/encoding)
BuildRequires:  go(github.com/segmentio/encoding/json)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/wI2L/jettison) = %{version}


%description
Jettison
Jettison is a fast and flexible JSON encoder for the Go programming
language, inspired by bet365/jingo, with a richer features set, aiming
at 100% compatibility with the standard library.
------------------------------------------------------------------------

Installation

Jettison uses Go modules (https://github.com/golang/go/wiki/Modules).
Releases are tagged according to the *SemVer* format, prefixed with a v,
starting from *0.2.0*. You can get the latest release using the

%files
%doc README.md
%doc CHANGELOG.md
%license LICENSE
%license LICENSE.golang
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
