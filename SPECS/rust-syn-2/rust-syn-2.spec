# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name syn
%global full_version 2.0.117
%global pkgname syn-2

Name:           rust-syn-2
Version:        2.0.117
Release:        %autorelease
Summary:        Rust crate "syn"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/syn
#!RemoteAsset:  sha256:e665b8803e7b1d2a727f4023456bbbbe74da67099c585258af0ad9c5013b9b99
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1) >= 1.0.91
Requires:       crate(unicode-ident-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/clone-impls) = %{version}
Provides:       crate(%{pkgname}/derive) = %{version}
Provides:       crate(%{pkgname}/extra-traits) = %{version}
Provides:       crate(%{pkgname}/fold) = %{version}
Provides:       crate(%{pkgname}/full) = %{version}
Provides:       crate(%{pkgname}/parsing) = %{version}
Provides:       crate(%{pkgname}/test) = %{version}
Provides:       crate(%{pkgname}/visit) = %{version}
Provides:       crate(%{pkgname}/visit-mut) = %{version}

%description
Source code for takopackized Rust crate "syn"

%package     -n %{name}+default
Summary:        Parser for Rust source code - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/clone-impls) = %{version}
Requires:       crate(%{pkgname}/derive) = %{version}
Requires:       crate(%{pkgname}/parsing) = %{version}
Requires:       crate(%{pkgname}/printing) = %{version}
Requires:       crate(%{pkgname}/proc-macro) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust syn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+printing
Summary:        Parser for Rust source code - feature "printing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(quote-1) >= 1.0.35
Provides:       crate(%{pkgname}/printing) = %{version}

%description -n %{name}+printing
This metapackage enables feature "printing" for the Rust syn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+proc-macro
Summary:        Parser for Rust source code - feature "proc-macro"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(proc-macro2-1/proc-macro) >= 1.0.91
Requires:       crate(quote-1/proc-macro) >= 1.0.35
Provides:       crate(%{pkgname}/proc-macro) = %{version}

%description -n %{name}+proc-macro
This metapackage enables feature "proc-macro" for the Rust syn crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
