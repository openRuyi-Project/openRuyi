# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name      syscalls
%global full_version    0.8.1
%global pkgname         syscalls-0.8

Name:           rust-syscalls-0.8
Version:        0.8.1
Release:        %autorelease
Summary:        Rust crate "syscalls"
License:        BSD-2-Clause
URL:            https://github.com/jasonwhite/syscalls
#!RemoteAsset:  sha256:81c645a4de0d803ced6ef0388a2646aa1ef8467173b5d59a2c33c88de4ab76e7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/aarch64) = %{version}
Provides:       crate(%{pkgname}/arm) = %{version}
Provides:       crate(%{pkgname}/loongarch64) = %{version}
Provides:       crate(%{pkgname}/mips) = %{version}
Provides:       crate(%{pkgname}/mips64) = %{version}
Provides:       crate(%{pkgname}/powerpc) = %{version}
Provides:       crate(%{pkgname}/powerpc64) = %{version}
Provides:       crate(%{pkgname}/riscv32) = %{version}
Provides:       crate(%{pkgname}/riscv64) = %{version}
Provides:       crate(%{pkgname}/s390x) = %{version}
Provides:       crate(%{pkgname}/sparc) = %{version}
Provides:       crate(%{pkgname}/sparc64) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/thumb-mode) = %{version}
Provides:       crate(%{pkgname}/x86) = %{version}
Provides:       crate(%{pkgname}/x86-64) = %{version}

%description
Source code for takopackized Rust crate "syscalls"

%package     -n %{name}+all
Summary:        List of Linux system calls - feature "all"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/aarch64) = %{version}
Requires:       crate(%{pkgname}/arm) = %{version}
Requires:       crate(%{pkgname}/loongarch64) = %{version}
Requires:       crate(%{pkgname}/mips) = %{version}
Requires:       crate(%{pkgname}/mips64) = %{version}
Requires:       crate(%{pkgname}/powerpc) = %{version}
Requires:       crate(%{pkgname}/powerpc64) = %{version}
Requires:       crate(%{pkgname}/riscv32) = %{version}
Requires:       crate(%{pkgname}/riscv64) = %{version}
Requires:       crate(%{pkgname}/s390x) = %{version}
Requires:       crate(%{pkgname}/sparc) = %{version}
Requires:       crate(%{pkgname}/sparc64) = %{version}
Requires:       crate(%{pkgname}/x86) = %{version}
Requires:       crate(%{pkgname}/x86-64) = %{version}
Provides:       crate(%{pkgname}/all) = %{version}

%description -n %{name}+all
This metapackage enables feature "all" for the Rust syscalls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        List of Linux system calls - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust syscalls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+full
Summary:        List of Linux system calls - feature "full"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/all) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/full) = %{version}

%description -n %{name}+full
This metapackage enables feature "full" for the Rust syscalls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        List of Linux system calls - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde-repr) = %{version}
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust syscalls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-repr
Summary:        List of Linux system calls - feature "serde_repr"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-repr-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/serde-repr) = %{version}

%description -n %{name}+serde-repr
This metapackage enables feature "serde_repr" for the Rust syscalls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+with-serde
Summary:        List of Linux system calls - feature "with-serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/serde-repr) = %{version}
Provides:       crate(%{pkgname}/with-serde) = %{version}

%description -n %{name}+with-serde
This metapackage enables feature "with-serde" for the Rust syscalls crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
