# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name const_format_proc_macros
%global full_version 0.2.34
%global pkgname const-format-proc-macros-0.2

Name:           rust-const-format-proc-macros-0.2
Version:        0.2.34
Release:        %autorelease
Summary:        Rust crate "const_format_proc_macros"
License:        Zlib
URL:            https://github.com/rodrimati1992/const_format_crates/
#!RemoteAsset:  sha256:1d57c2eccfb16dbac1f4e61e206105db5820c9d26c3c472bc17c774259ef7744
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.19
Requires:       crate(quote-1/default) >= 1.0.7
Requires:       crate(unicode-xid-0.2/default) >= 0.2.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "const_format_proc_macros"

%package     -n %{name}+debug
Summary:        Implementation detail of the `const_format` crate - feature "debug"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(syn-1/extra-traits) >= 1.0.38
Requires:       crate(syn-1/parsing) >= 1.0.38
Requires:       crate(syn-1/proc-macro) >= 1.0.38
Provides:       crate(%{pkgname}/debug) = %{version}

%description -n %{name}+debug
This metapackage enables feature "debug" for the Rust const_format_proc_macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+derive
Summary:        Implementation detail of the `const_format` crate - feature "derive" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/syn) = %{version}
Requires:       crate(syn-1/derive) >= 1.0.38
Requires:       crate(syn-1/parsing) >= 1.0.38
Requires:       crate(syn-1/printing) >= 1.0.38
Requires:       crate(syn-1/proc-macro) >= 1.0.38
Provides:       crate(%{pkgname}/all) = %{version}
Provides:       crate(%{pkgname}/derive) = %{version}

%description -n %{name}+derive
This metapackage enables feature "derive" for the Rust const_format_proc_macros crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "all" feature.

%package     -n %{name}+syn
Summary:        Implementation detail of the `const_format` crate - feature "syn"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(syn-1/parsing) >= 1.0.38
Requires:       crate(syn-1/proc-macro) >= 1.0.38
Provides:       crate(%{pkgname}/syn) = %{version}

%description -n %{name}+syn
This metapackage enables feature "syn" for the Rust const_format_proc_macros crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
