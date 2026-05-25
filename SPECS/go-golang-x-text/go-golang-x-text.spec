# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           text
%define go_import_path  golang.org/x/text
# We only exclude specific tests because can cause build loops.
%global go_test_exclude_glob %{shrink:
    golang.org/x/text/collate/tools/colcmp
    golang.org/x/text/cmd/gotext*
    golang.org/x/text/message/pipeline*
}

Name:           go-golang-x-text
Version:        0.32.0
Release:        %autorelease
Summary:        Go text processing support
License:        BSD-3-Clause
URL:            https://golang.org/x/text
VCS:            git:https://github.com/golang/text
#!RemoteAsset:  sha256:593f4edcbb602157527fbe725ee5ca668cade3d33cd0d12d9f0b13ac1db50f7b
Source0:        https://github.com/golang/text/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# https://sources.debian.org/src/golang-golang-x-text/0.31.0-1/debian/patches/0001-Disable-failed-test-TestCountMallocs.patch
Patch2000:      2000-Disable-failed-test-TestCountMallocs.patch
# https://sources.debian.org/src/golang-golang-x-text/0.31.0-1/debian/patches/0002-Skip-TestLinking-in-language-display.patch
Patch2001:      2001-Skip-TestLinking-in-language-display.patch

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(golang.org/x/text) = %{version}

%description
This repository provides text-related packages, such as character
encodings, text transformations, and locale-specific text handling.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
