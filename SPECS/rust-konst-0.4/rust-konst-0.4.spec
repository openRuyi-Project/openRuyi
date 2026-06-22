# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name konst
%global full_version 0.4.3
%global pkgname konst-0.4

Name:           rust-konst-0.4
Version:        0.4.3
Release:        %autorelease
Summary:        Rust crate "konst"
License:        Zlib
URL:            https://github.com/rodrimati1992/konst/
#!RemoteAsset:  sha256:f660d5f887e3562f9ab6f4a14988795b694099d66b4f5dedc02d197ba9becb1d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(const-panic-0.2/default) >= 0.2.13
Requires:       crate(const-panic-0.2/rust-1-88) >= 0.2.13
Requires:       crate(typewit-1/rust-1-83) >= 1.12.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/cmp) = %{version}
Provides:       crate(%{pkgname}/debug) = %{version}
Provides:       crate(%{pkgname}/docsrs) = %{version}
Provides:       crate(%{pkgname}/iter) = %{version}
Provides:       crate(%{pkgname}/parsing) = %{version}
Provides:       crate(%{pkgname}/rust-latest-stable) = %{version}

%description
Source code for takopackized Rust crate "konst"

%package     -n %{name}+ui
Summary:        Const equivalents of std features: comparison, destructuring, iteration, and parsing - feature "__ui"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rust-latest-stable) = %{version}
Requires:       crate(%{pkgname}/trybuild) = %{version}
Provides:       crate(%{pkgname}/ui) = %{version}

%description -n %{name}+ui
This metapackage enables feature "__ui" for the Rust konst crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+const-panic-derive
Summary:        Const equivalents of std features: comparison, destructuring, iteration, and parsing - feature "const_panic_derive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(const-panic-0.2/derive) >= 0.2.13
Requires:       crate(const-panic-0.2/rust-1-88) >= 0.2.13
Provides:       crate(%{pkgname}/const-panic-derive) = %{version}

%description -n %{name}+const-panic-derive
This metapackage enables feature "const_panic_derive" for the Rust konst crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Const equivalents of std features: comparison, destructuring, iteration, and parsing - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/cmp) = %{version}
Requires:       crate(%{pkgname}/iter) = %{version}
Requires:       crate(%{pkgname}/parsing-proc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust konst crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+konst-proc-macros
Summary:        Const equivalents of std features: comparison, destructuring, iteration, and parsing - feature "konst_proc_macros"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(konst-proc-macros-0.4/default) >= 0.4.1
Provides:       crate(%{pkgname}/konst-proc-macros) = %{version}

%description -n %{name}+konst-proc-macros
This metapackage enables feature "konst_proc_macros" for the Rust konst crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+parsing-proc
Summary:        Const equivalents of std features: comparison, destructuring, iteration, and parsing - feature "parsing_proc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/konst-proc-macros) = %{version}
Requires:       crate(%{pkgname}/parsing) = %{version}
Provides:       crate(%{pkgname}/parsing-proc) = %{version}

%description -n %{name}+parsing-proc
This metapackage enables feature "parsing_proc" for the Rust konst crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+trybuild
Summary:        Const equivalents of std features: comparison, destructuring, iteration, and parsing - feature "trybuild"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(trybuild-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/trybuild) = %{version}

%description -n %{name}+trybuild
This metapackage enables feature "trybuild" for the Rust konst crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
