# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name syn
%global full_version 0.15.44
%global pkgname syn-0.15

Name:           rust-syn-0.15
Version:        0.15.44
Release:        %autorelease
Summary:        Rust crate "syn"
License:        MIT OR Apache-2.0
URL:            https://github.com/dtolnay/syn
#!RemoteAsset:  sha256:9ca4b3b69a77cbe1ffc9e198781b7acb0c7365a883670e8f1c1bc66fba79a5c5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-0.4) >= 0.4.4
Requires:       crate(unicode-xid-0.1/default) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/clone-impls) = %{version}
Provides:       crate(%{pkgname}/derive) = %{version}
Provides:       crate(%{pkgname}/extra-traits) = %{version}
Provides:       crate(%{pkgname}/fold) = %{version}
Provides:       crate(%{pkgname}/full) = %{version}
Provides:       crate(%{pkgname}/parsing) = %{version}
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

%package     -n %{name}+proc-macro
Summary:        Parser for Rust source code - feature "proc-macro"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(proc-macro2-0.4/proc-macro) >= 0.4.4
Requires:       crate(quote-0.6/proc-macro) >= 0.6.0
Provides:       crate(%{pkgname}/proc-macro) = %{version}

%description -n %{name}+proc-macro
This metapackage enables feature "proc-macro" for the Rust syn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+quote
Summary:        Parser for Rust source code - feature "quote" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(quote-0.6) >= 0.6.0
Provides:       crate(%{pkgname}/printing) = %{version}
Provides:       crate(%{pkgname}/quote) = %{version}

%description -n %{name}+quote
This metapackage enables feature "quote" for the Rust syn crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "printing" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
