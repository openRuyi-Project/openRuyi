# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name iced-x86
%global full_version 1.21.0
%global pkgname iced-x86-1

Name:           rust-iced-x86-1
Version:        1.21.0
Release:        %autorelease
Summary:        Rust crate "iced-x86"
License:        MIT
URL:            https://github.com/icedland/iced
#!RemoteAsset:  sha256:7c447cff8c7f384a7d4f741cfcff32f75f3ad02b406432e8d6c878d56b1edf6b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/block-encoder) = %{version}
Provides:       crate(%{pkgname}/code-asm) = %{version}
Provides:       crate(%{pkgname}/db) = %{version}
Provides:       crate(%{pkgname}/decoder) = %{version}
Provides:       crate(%{pkgname}/encoder) = %{version}
Provides:       crate(%{pkgname}/exhaustive-enums) = %{version}
Provides:       crate(%{pkgname}/fast-fmt) = %{version}
Provides:       crate(%{pkgname}/gas) = %{version}
Provides:       crate(%{pkgname}/instr-info) = %{version}
Provides:       crate(%{pkgname}/intel) = %{version}
Provides:       crate(%{pkgname}/internal-flip) = %{version}
Provides:       crate(%{pkgname}/masm) = %{version}
Provides:       crate(%{pkgname}/mvex) = %{version}
Provides:       crate(%{pkgname}/nasm) = %{version}
Provides:       crate(%{pkgname}/no-d3now) = %{version}
Provides:       crate(%{pkgname}/no-evex) = %{version}
Provides:       crate(%{pkgname}/no-vex) = %{version}
Provides:       crate(%{pkgname}/no-xop) = %{version}
Provides:       crate(%{pkgname}/op-code-info) = %{version}

%description
Source code for takopackized Rust crate "iced-x86"

%package     -n %{name}+default
Summary:        Blazing fast and correct x86/x64 disassembler, assembler and instruction decoder written in Rust - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/block-encoder) = %{version}
Requires:       crate(%{pkgname}/decoder) = %{version}
Requires:       crate(%{pkgname}/encoder) = %{version}
Requires:       crate(%{pkgname}/fast-fmt) = %{version}
Requires:       crate(%{pkgname}/gas) = %{version}
Requires:       crate(%{pkgname}/instr-info) = %{version}
Requires:       crate(%{pkgname}/intel) = %{version}
Requires:       crate(%{pkgname}/masm) = %{version}
Requires:       crate(%{pkgname}/nasm) = %{version}
Requires:       crate(%{pkgname}/op-code-info) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust iced-x86 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+lazy-static
Summary:        Blazing fast and correct x86/x64 disassembler, assembler and instruction decoder written in Rust - feature "lazy_static" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lazy-static-1/default) >= 1.4.0
Provides:       crate(%{pkgname}/lazy-static) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+lazy-static
This metapackage enables feature "lazy_static" for the Rust iced-x86 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "std" feature.

%package     -n %{name}+no-std
Summary:        Blazing fast and correct x86/x64 disassembler, assembler and instruction decoder written in Rust - feature "no_std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lazy-static-1/spin-no-std) >= 1.4.0
Provides:       crate(%{pkgname}/no-std) = %{version}

%description -n %{name}+no-std
This metapackage enables feature "no_std" for the Rust iced-x86 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Blazing fast and correct x86/x64 disassembler, assembler and instruction decoder written in Rust - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.16
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust iced-x86 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
