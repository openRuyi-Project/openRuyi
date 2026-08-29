# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name mlua_derive
%global full_version 0.11.0
%global pkgname mlua-derive-0.11

Name:           rust-mlua-derive-0.11
Version:        0.11.0
Release:        %autorelease
Summary:        Rust crate "mlua_derive"
License:        MIT
URL:            https://github.com/mlua-rs/mlua
#!RemoteAsset:  sha256:465bddde514c4eb3b50b543250e97c1d4b284fa3ef7dc0ba2992c77545dbceb2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(proc-macro2-1/span-locations) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0
Requires:       crate(syn-2/full) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "mlua_derive"

%package     -n %{name}+itertools
Summary:        Procedural macros for the mlua crate - feature "itertools"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(itertools-0.14/default) >= 0.14.0
Provides:       crate(%{pkgname}/itertools) = %{version}

%description -n %{name}+itertools
This metapackage enables feature "itertools" for the Rust mlua_derive crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+macros
Summary:        Procedural macros for the mlua crate - feature "macros"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/itertools) = %{version}
Requires:       crate(%{pkgname}/once-cell) = %{version}
Requires:       crate(%{pkgname}/proc-macro-error2) = %{version}
Requires:       crate(%{pkgname}/regex) = %{version}
Provides:       crate(%{pkgname}/macros) = %{version}

%description -n %{name}+macros
This metapackage enables feature "macros" for the Rust mlua_derive crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+once-cell
Summary:        Procedural macros for the mlua crate - feature "once_cell"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(once-cell-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/once-cell) = %{version}

%description -n %{name}+once-cell
This metapackage enables feature "once_cell" for the Rust mlua_derive crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+proc-macro-error2
Summary:        Procedural macros for the mlua crate - feature "proc-macro-error2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(proc-macro-error2-2/default) >= 2.0.1
Provides:       crate(%{pkgname}/proc-macro-error2) = %{version}

%description -n %{name}+proc-macro-error2
This metapackage enables feature "proc-macro-error2" for the Rust mlua_derive crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+regex
Summary:        Procedural macros for the mlua crate - feature "regex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-1/default) >= 1.4.0
Provides:       crate(%{pkgname}/regex) = %{version}

%description -n %{name}+regex
This metapackage enables feature "regex" for the Rust mlua_derive crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
