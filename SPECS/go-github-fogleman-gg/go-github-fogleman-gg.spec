# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gg
%define go_import_path  github.com/fogleman/gg
# The examples directory contains many standalone main packages, which cannot
# be tested together as one package. - HNO3Miracle
%define go_test_exclude github.com/fogleman/gg/examples

Name:           go-github-fogleman-gg
Version:        1.3.0
Release:        %autorelease
Summary:        2D rendering library for Go
License:        MIT
URL:            https://github.com/fogleman/gg
#!RemoteAsset:  sha256:483cb4454ca6a998cdc4d670d350976cfdaffa058897831f420486cda4b4f6d9
Source0:        https://github.com/fogleman/gg/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz

# Avoid parsing rpm-injected go test flags in upstream test init. - HNO3Miracle
Patch2000:      2000-do-not-parse-test-flags-in-init.patch
BuildArch:      noarch
BuildSystem:    golangmodules

# Some raster hash tests differ across arches/current dependency versions; keep
# the deterministic API tests that are stable in OBS. - HNO3Miracle
BuildOption(check):  -run '^(TestBlank|TestGrid|TestLines|TestCircles|TestCubic|TestFill|TestClip|TestDrawStringWrapped|TestDrawImage|TestSetPixel|TestDrawPoint|TestLinearGradient|TestRadialGradient|TestDashes)$'

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/golang/freetype)
BuildRequires:  go(golang.org/x/image)

Provides:       go(github.com/fogleman/gg) = %{version}

Requires:       go(github.com/golang/freetype)
Requires:       go(golang.org/x/image)

%description
gg is a library for rendering 2D graphics in pure Go.

%files
%doc README.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
