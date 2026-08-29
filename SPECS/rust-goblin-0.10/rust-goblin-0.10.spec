# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name goblin
%global full_version 0.10.7
%global pkgname goblin-0.10

Name:           rust-goblin-0.10
Version:        0.10.7
Release:        %autorelease
Summary:        Rust crate "goblin"
License:        MIT
URL:            https://github.com/m4b/goblin
#!RemoteAsset:  sha256:17582616a7718cca54cec18e534a76c7c4aec11a8b9a85695712f262fd15a4c8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(plain-0.2/default) >= 0.2.3
Requires:       crate(scroll-0.13) >= 0.13.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/elf32) = %{version}
Provides:       crate(%{pkgname}/elf64) = %{version}

%description
Source code for takopackized Rust crate "goblin"

%package     -n %{name}+alloc
Summary:        Impish, cross-platform, ELF, Mach-o, and PE binary parsing and loading crate - feature "alloc" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/log) = %{version}
Requires:       crate(scroll-0.13/derive) >= 0.13.0
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/archive) = %{version}
Provides:       crate(%{pkgname}/endian-fd) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust goblin crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "archive", and "endian_fd" features.

%package     -n %{name}+default
Summary:        Impish, cross-platform, ELF, Mach-o, and PE binary parsing and loading crate - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/archive) = %{version}
Requires:       crate(%{pkgname}/elf32) = %{version}
Requires:       crate(%{pkgname}/elf64) = %{version}
Requires:       crate(%{pkgname}/endian-fd) = %{version}
Requires:       crate(%{pkgname}/mach32) = %{version}
Requires:       crate(%{pkgname}/mach64) = %{version}
Requires:       crate(%{pkgname}/pe32) = %{version}
Requires:       crate(%{pkgname}/pe64) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/te) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust goblin crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        Impish, cross-platform, ELF, Mach-o, and PE binary parsing and loading crate - feature "log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4) >= 0.4.0
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust goblin crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mach32
Summary:        Impish, cross-platform, ELF, Mach-o, and PE binary parsing and loading crate - feature "mach32" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/archive) = %{version}
Requires:       crate(%{pkgname}/endian-fd) = %{version}
Provides:       crate(%{pkgname}/mach32) = %{version}
Provides:       crate(%{pkgname}/mach64) = %{version}

%description -n %{name}+mach32
This metapackage enables feature "mach32" for the Rust goblin crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "mach64" feature.

%package     -n %{name}+pe32
Summary:        Impish, cross-platform, ELF, Mach-o, and PE binary parsing and loading crate - feature "pe32" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/endian-fd) = %{version}
Provides:       crate(%{pkgname}/pe32) = %{version}
Provides:       crate(%{pkgname}/pe64) = %{version}
Provides:       crate(%{pkgname}/te) = %{version}

%description -n %{name}+pe32
This metapackage enables feature "pe32" for the Rust goblin crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "pe64", and "te" features.

%package     -n %{name}+std
Summary:        Impish, cross-platform, ELF, Mach-o, and PE binary parsing and loading crate - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(scroll-0.13/std) >= 0.13.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust goblin crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
