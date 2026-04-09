# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           avo
%define go_import_path  github.com/mmcloughlin/avo
# TODO: test uses go tool asm, generate amd64 SIMD (AVX) only - 251
%define go_test_exclude_glob %{shrink:
    github.com/mmcloughlin/avo/internal/inst*
    github.com/mmcloughlin/avo/tests*
    github.com/mmcloughlin/avo/examples*
    github.com/mmcloughlin/avo/internal/load*
}

Name:           go-github-mmcloughlin-avo
Version:        0.6.0
Release:        %autorelease
Summary:        Generate x86 Assembly with Go
License:        BSD-3-Clause
URL:            https://github.com/mmcloughlin/avo
#!RemoteAsset
Source0:        https://github.com/mmcloughlin/avo/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}
BuildOption(check):  -short

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/arch)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/mmcloughlin/avo) = %{version}

Requires:       go(golang.org/x/arch)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/tools)

%description
Generate x86 Assembly with Go
avo makes high-performance Go assembly easier to write, review and
maintain. The avo package presents a familiar assembly-like interface
that simplifies development without sacrificing performance:

 * **Use Go control structures** for assembly generation; avo programs
   *are* Go programs
 * **Register allocation**: write functions with virtual registers and
   avo assigns physical registers for you
 * **Automatically load arguments and store return values**: ensure
   memory offsets are correct for complex structures
 * **Generation of stub files** to interface with your Go package

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
