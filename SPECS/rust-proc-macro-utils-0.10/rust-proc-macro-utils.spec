# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name proc-macro-utils
%global full_version 0.10.0
%global pkgname proc-macro-utils-0.10

Name:           rust-proc-macro-utils-0.10
Version:        0.10.0
Release:        %autorelease
Summary:        Rust crate "proc-macro-utils"
License:        MIT OR Apache-2.0
URL:            https://github.com/ModProg/proc-macro-utils
#!RemoteAsset:  sha256:eeaf08a13de400bc215877b5bdc088f241b12eb42f0a548d3390dc1c56bb7071
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/proc-macro)

%description
Source code for takopackized Rust crate "proc-macro-utils"

%package     -n %{name}+default
Summary:        Low-level utilities on proc-macro and proc-macro2 types - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/parser)
Requires:       crate(%{pkgname}/proc-macro)
Requires:       crate(%{pkgname}/proc-macro2)
Requires:       crate(%{pkgname}/quote)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust proc-macro-utils crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+parser
Summary:        Low-level utilities on proc-macro and proc-macro2 types - feature "parser"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/proc-macro2)
Requires:       crate(%{pkgname}/smallvec)
Provides:       crate(%{pkgname}/parser)

%description -n %{name}+parser
This metapackage enables feature "parser" for the Rust proc-macro-utils crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+proc-macro2
Summary:        Low-level utilities on proc-macro and proc-macro2 types - feature "proc-macro2"
Requires:       crate(%{pkgname})
Requires:       crate(proc-macro2-1.0/default) >= 1.0.106
Provides:       crate(%{pkgname}/proc-macro2)

%description -n %{name}+proc-macro2
This metapackage enables feature "proc-macro2" for the Rust proc-macro-utils crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+quote
Summary:        Low-level utilities on proc-macro and proc-macro2 types - feature "quote"
Requires:       crate(%{pkgname})
Requires:       crate(quote-1.0/default) >= 1.0.45
Provides:       crate(%{pkgname}/quote)

%description -n %{name}+quote
This metapackage enables feature "quote" for the Rust proc-macro-utils crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+smallvec
Summary:        Low-level utilities on proc-macro and proc-macro2 types - feature "smallvec"
Requires:       crate(%{pkgname})
Requires:       crate(smallvec-1.0/const-generics) >= 1.15.1
Requires:       crate(smallvec-1.0/default) >= 1.15.1
Provides:       crate(%{pkgname}/smallvec)

%description -n %{name}+smallvec
This metapackage enables feature "smallvec" for the Rust proc-macro-utils crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
