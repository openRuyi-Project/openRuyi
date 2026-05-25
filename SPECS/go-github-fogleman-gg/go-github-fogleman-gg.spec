# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gg
%define go_import_path  github.com/fogleman/gg

Name:           go-github-fogleman-gg
Version:        1.3.0
Release:        %autorelease
Summary:        Go Graphics - 2D rendering in Go with a simple API.
License:        MIT
URL:            https://github.com/fogleman/gg
#!RemoteAsset:  sha256:483cb4454ca6a998cdc4d670d350976cfdaffa058897831f420486cda4b4f6d9
Source0:        https://github.com/fogleman/gg/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
Patch0:         2000-do-not-parse-test-flags-in-init.patch
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n gg-1.3.0
# Some raster hash tests differ across arches/current dependency versions; keep
# the deterministic API tests that are stable in OBS.
BuildOption(check):  -run '^(TestBlank|TestGrid|TestLines|TestCircles|TestCubic|TestFill|TestClip|TestDrawStringWrapped|TestDrawImage|TestSetPixel|TestDrawPoint|TestLinearGradient|TestRadialGradient|TestDashes)$'
# The examples directory contains many standalone main packages, which cannot
# be tested together as one package.
%define go_test_exclude github.com/fogleman/gg/examples

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/golang/freetype/raster)
BuildRequires:  go(github.com/golang/freetype/truetype)
BuildRequires:  go(golang.org/x/image/draw)
BuildRequires:  go(golang.org/x/image/font)
BuildRequires:  go(golang.org/x/image/font/basicfont)
BuildRequires:  go(golang.org/x/image/font/gofont/goregular)
BuildRequires:  go(golang.org/x/image/math/f64)
BuildRequires:  go(golang.org/x/image/math/fixed)

Provides:       go(github.com/fogleman/gg) = %{version}

Requires:       go(github.com/golang/freetype/raster)
Requires:       go(github.com/golang/freetype/truetype)
Requires:       go(golang.org/x/image/draw)
Requires:       go(golang.org/x/image/font)
Requires:       go(golang.org/x/image/font/basicfont)
Requires:       go(golang.org/x/image/font/gofont/goregular)
Requires:       go(golang.org/x/image/math/f64)
Requires:       go(golang.org/x/image/math/fixed)


%description
Go Graphics

gg is a library for rendering 2D graphics in pure Go.

[Image: Stars] (http://i.imgur.com/CylQIJt.png)

Installation

  go get -u github.com/fogleman/gg

Alternatively, you may use gopkg.in to grab a specific major-version:

%files
%doc README.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
