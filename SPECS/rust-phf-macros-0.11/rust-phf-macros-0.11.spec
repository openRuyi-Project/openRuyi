# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name phf_macros
%global full_version 0.11.3
%global pkgname phf-macros-0.11

Name:           rust-phf-macros-0.11
Version:        0.11.3
Release:        %autorelease
Summary:        Rust crate "phf_macros"
License:        MIT
URL:            https://github.com/rust-phf/rust-phf
#!RemoteAsset:  sha256:f84ac04429c13a7ff43785d75ad27569f2951ce0ffd30a3321230db2fc727216
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(phf-generator-0.11/default) >= 0.11.1
Requires:       crate(phf-shared-0.11) >= 0.11.2
Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0
Requires:       crate(syn-2/full) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "phf_macros"

%package     -n %{name}+unicase
Summary:        Macros to generate types in the phf crate - feature "unicase"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/unicase-) = %{version}
Requires:       crate(phf-shared-0.11/unicase) >= 0.11.2
Provides:       crate(%{pkgname}/unicase) = %{version}

%description -n %{name}+unicase
This metapackage enables feature "unicase" for the Rust phf_macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicase-
Summary:        Macros to generate types in the phf crate - feature "unicase_"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(unicase-2/default) >= 2.4.0
Provides:       crate(%{pkgname}/unicase-) = %{version}

%description -n %{name}+unicase-
This metapackage enables feature "unicase_" for the Rust phf_macros crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
