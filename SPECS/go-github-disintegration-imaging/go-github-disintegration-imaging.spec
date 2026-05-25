# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           imaging
%define go_import_path  github.com/disintegration/imaging

Name:           go-github-disintegration-imaging
Version:        1.6.2
Release:        %autorelease
Summary:        Imaging is a simple image processing package for Go
License:        MIT
URL:            https://github.com/disintegration/imaging
#!RemoteAsset:  sha256:ddc0cbbf306630d39ee710ff055bb9503d30598485f76f51564ee3ae13d6611a
Source0:        https://github.com/disintegration/imaging/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n imaging-1.6.2

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/image)
BuildRequires:  go(golang.org/x/image/bmp)
BuildRequires:  go(golang.org/x/image/tiff)

Provides:       go(github.com/disintegration/imaging) = %{version}

Requires:       go(golang.org/x/image)
Requires:       go(golang.org/x/image/bmp)
Requires:       go(golang.org/x/image/tiff)


%description
Imaging

[Image: PkgGoDev]
(https://pkg.go.dev/badge/github.com/disintegration/imaging)
(https://pkg.go.dev/github.com/disintegration/imaging) [Image: Build
Status] (https://travis-ci.org/disintegration/imaging.svg?branch=master)
(https://travis-ci.org/disintegration/imaging) [Image: Coverage Status]
(https://coveralls.io/repos/github/disintegration/imaging/badge.
svg?branch=master&service=github)
(https://coveralls.io/github/disintegration/imaging?branch=master)
[Image: Go Report Card]

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
