# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           jettison
%define go_import_path  github.com/wI2L/jettison
# Go 1.25 encodes \b and \f differently from the old stdlib output expected
# by TestStringEscaping; skip the package tests instead of passing raw -skip. - HNO3Miracle
%define go_test_exclude %{go_import_path}

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

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/modern-go/concurrent)
BuildRequires:  go(github.com/modern-go/reflect2)
BuildRequires:  go(github.com/segmentio/asm)
BuildRequires:  go(github.com/segmentio/encoding)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(github.com/wI2L/jettison) = %{version}

%description
Jettison is a configurable JSON encoder for Go that aims to remain compatible
with the standard library while improving encoding performance.

%files
%doc CHANGELOG.md
%doc README.md
%license LICENSE
%license LICENSE.golang
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
