# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name syn
%global full_version 2.0.117
%global pkgname syn-2.0

Name:           rust-syn-2.0
Version:        2.0.117
Release:        %autorelease
Summary:        Rust crate "syn"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/syn
#!RemoteAsset:  sha256:e665b8803e7b1d2a727f4023456bbbbe74da67099c585258af0ad9c5013b9b99
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1.0) >= 1.0.106
Requires:       crate(unicode-ident-1.0/default) >= 1.0.24
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/clone-impls)
Provides:       crate(%{pkgname}/derive)
Provides:       crate(%{pkgname}/extra-traits)
Provides:       crate(%{pkgname}/fold)
Provides:       crate(%{pkgname}/full)
Provides:       crate(%{pkgname}/parsing)
Provides:       crate(%{pkgname}/test)
Provides:       crate(%{pkgname}/visit)
Provides:       crate(%{pkgname}/visit-mut)

%description
Source code for takopackized Rust crate "syn"

%package     -n %{name}+default
Summary:        Parser for Rust source code - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/clone-impls)
Requires:       crate(%{pkgname}/derive)
Requires:       crate(%{pkgname}/parsing)
Requires:       crate(%{pkgname}/printing)
Requires:       crate(%{pkgname}/proc-macro)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust syn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+printing
Summary:        Parser for Rust source code - feature "printing"
Requires:       crate(%{pkgname})
Requires:       crate(quote-1.0) >= 1.0.45
Provides:       crate(%{pkgname}/printing)

%description -n %{name}+printing
This metapackage enables feature "printing" for the Rust syn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+proc-macro
Summary:        Parser for Rust source code - feature "proc-macro"
Requires:       crate(%{pkgname})
Requires:       crate(proc-macro2-1.0/proc-macro) >= 1.0.106
Requires:       crate(quote-1.0/proc-macro) >= 1.0.45
Provides:       crate(%{pkgname}/proc-macro)

%description -n %{name}+proc-macro
This metapackage enables feature "proc-macro" for the Rust syn crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
