# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           cpuid
%define go_import_path  github.com/klauspost/cpuid/v2

Name:           go-github-klauspost-cpuid-v2
Version:        2.3.0
Release:        %autorelease
Summary:        CPU feature identification for Go
License:        MIT
URL:            https://github.com/klauspost/cpuid
#!RemoteAsset
Source0:        https://github.com/klauspost/cpuid/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/klauspost/cpuid/v2) = %{version}

%description
Package cpuid provides information about the CPU running the current
program.

CPU features are detected on startup, and kept for fast access through
the life of the application. Currently x86 / x64 (AMD64/i386) and ARM
(ARM64) is supported, and no external C (cgo) code is used, which should
make the library very easy to use.

You can access the CPU information by accessing the shared CPU variable
of the cpuid library.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
